#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;

int t[10][10];
int an[10];

int s[10][10];
int sn[10];

int ttn[10];
bool use[10];

int N,M,T;

void init()
{
     int i;
     int a,b;
     memset(an,0,sizeof(an));
     memset(ttn,0,sizeof(ttn));
     scanf("%d",&N);
     for(i=0;i<N-1;i++)
     {
        scanf("%d%d",&a,&b);
        a--,b--;
        t[a][an[a]++]=b;
        t[b][an[b]++]=a;
     }
     scanf("%d",&M);
     for(i=0;i<M-1;i++)
     {
       scanf("%d%d",&a,&b);
       a--,b--;
       ttn[a]++,ttn[b]++;
     }
     sort(ttn,ttn+N);
}

bool judge(int n)
{
     int i,j;
     memset(sn,0,sizeof(sn));
     for(i=0;i<N;i++)
     {
       if(n&(1<<i))
       {
       for(j=0;j<an[i];j++)
       {
          if(n&(1<<t[i][j]))
             sn[i]++;
       }
       }
       }
     sort(sn,sn+N);
     for(i=0;i<N;i++)
     {
        if(sn[i]!=ttn[i])
           return false;
     }
     return true;
}

void solve()
{
     int i;
     for(i=0;i<(1<<N)-1;i++)
     {
        if(judge(i))
        {
           printf("YES\n");
           return;
           }
           }
     printf("NO\n");
     }

int main()
{
    int i;
    //freopen("D.in","r",stdin);
    //freopen("D.txt","w",stdout);
    scanf("%d",&i);
    for(T=1;T<=i;T++)
    {
       init();
       printf("Case #%d: ",T);
       solve();
       }
    //system("PAUSE");
    return 0;
}
    
    


       
