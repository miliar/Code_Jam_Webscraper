#include<stdio.h>
#include<memory.h>

int N,M,T;
int mask[100][10];

void init()
{
     int i,j,t;
     int x,y;
     scanf("%d",&N);
     scanf("%d",&M);
     memset(mask,-1,sizeof(mask));
     for(i=0;i<M;i++)
     {
        scanf("%d",&t);
        for(j=0;j<t;j++)
        {
           scanf("%d%d",&x,&y);
           x--;
           mask[i][x]=y;
        }
     }
}

int one(int n)
{
    int i;
    int ans=0;
    for(i=0;i<N;i++)
    {
       if(n&(1<<i))
          ans++;
    }
    return ans;
}

bool judge(int n)
{
    int tt[10];
    int i,j;
    int ss=n;
    for(i=0;i<N;i++)
    {
       if(n&(1<<i))
          tt[i]=1;
       else
          tt[i]=0;
    }
    for(i=0;i<M;i++)
    {
       ss=0;
       for(j=0;j<N;j++)
       {
          if(mask[i][j]!=-1&&tt[j]==mask[i][j])
             ss++;
       }
       if(ss==0)
          return false;
    }
    return true;
}
             

void solve()
{
     int i;
     int ans=-1;
     for(i=0;i<(1<<N);i++)
     {
         if(judge(i))
         {
             if(ans==-1||one(i)<one(ans))
                ans=i;
         }
     }
     if(ans==-1)
     {
        printf("IMPOSSIBLE\n");
        return;
     }
     for(i=0;i<N;i++)
     {
       if(ans&(1<<i))
          printf("1 ");
       else
         printf("0 ");
     }
     printf("\n");
}

int main()
{
    int i;
    //freopen("B.in","r",stdin);
    //freopen("B.txt","w",stdout);
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        init();
        printf("Case #%d: ",i);
        solve(); 
    }
    return 0;
}
                       

