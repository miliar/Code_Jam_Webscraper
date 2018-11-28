#include <iostream>

using namespace std;
int queue[20005];
int g[1005];
int r,k,n;
int sum;
int ans;
int tans[5000005];
bool used[1005];
int length[1005];
int xunhuan;
void bfs()
{
    int cnt=0;
    int head=0,pos,t,p;
    memset(used,0,sizeof(used));
    int xunhuanans=0;
    int i;
    while(1)
    {
        if(used[head])
        {
            for(i=length[head]+1;i<=cnt;i++)
            {
                xunhuanans+=tans[i];
            }
            xunhuan=cnt-length[head];
            break;
        }
        used[head]=1;
        length[head]=cnt;
        pos=head;
        t=0;
        while(t<=k)
        {
            p=t;
            t+=g[pos];
            pos++;
            pos%=n;
        }
        cnt++;
        tans[cnt]=p;
        pos--;
        pos=(pos+n)%n;
        head=pos;
    }
    for(i=1;i<=min(length[head],r);i++)
    {
        ans+=tans[i];
    }
    int tcnt=r-length[head];
    if(tcnt<=0)
        return;
    ans+=(tcnt/xunhuan)*xunhuanans;
    tcnt%=xunhuan;
    pos=1;
    for(i=1;i<=tcnt;i++)
    {
        ans+=tans[length[head]+i];
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("tout.txt","w",stdout);
    int t;
    int cas=1;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        sum=0;
        int i;
        scanf("%d%d%d",&r,&k,&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",g+i);
            sum+=g[i];
        }
        if(k>=sum)
        {
            //printf("%d\n",r*sum);
            printf("Case #%d: %d\n",cas++,r*sum);
            continue;
        }
        bfs();
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
