#include <stdio.h>

#define MAX 1001

int R,K,N;
int group[MAX];
int visited[MAX];
struct
{
    int groupnum;
    long long  sumsofar;
}queue[MAX];
struct
{
    int next;
    int value;
}F[MAX];




void cacuFi(int i)
{
    int sum,tsum=0,t=i,times=0;
    while(sum=tsum,(tsum+=group[i])<=K)
    {
        i=(i+1)%N;
        times++;
        if(times==N) 
        {
            sum=tsum;
            break;
        }
    }
    F[t].value=sum;
    F[t].next=i;
}

void init()
{
    int i;
    for(i=0;i<N;i++)
    {
        cacuFi(i);
        visited[i]=0;
    }
}

long long  money()
{
    int cycle,outcycle,moneytimes;
    int i=0,times=0,j,t;
    long long sum=0,cyclesum;
    init();
    while(1)
    {
        if(visited[i]==1) break;
        visited[i]=1;
        sum+=F[i].value;
        queue[times].groupnum=i;
        queue[times].sumsofar=sum;
        times++;
        i=F[i].next;
    }
    for(j=times-1;j>=0;j--)
    {
        if(queue[j].groupnum==i)
        {
            cycle=times-j;
            outcycle=j;
            cyclesum=queue[times-1].sumsofar-queue[j].sumsofar+F[i].value;
            break;
        }
    }
    
    if(R<=outcycle) return queue[R-1].sumsofar;
    else
    {
        moneytimes=(R-outcycle)/cycle;
        t=(R-outcycle)%cycle;
        return queue[t+outcycle-1].sumsofar+moneytimes*cyclesum;
    }
}

int main()
{
   // freopen("C-large.in","r",stdin);
   // freopen("C-large.out","w",stdout);

    int T;
    int i,j;

    scanf("%d",&T);

    for(i=0;i!=T;i++)
    {
        scanf("%d%d%d",&R,&K,&N);
        for(j=0;j<N;j++)
            scanf("%d",&group[j]);
        printf("Case #%d: %I64d\n",i+1,money());
    }
}
