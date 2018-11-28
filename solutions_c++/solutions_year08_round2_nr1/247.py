#include<iostream>
using namespace std;
long long ans,now;
int t,test;
long long s[3][3];
void init()
{
     memset(s,0,sizeof(s));
     int  a,b,c,d,x,y,i,n,m;
     long long xx,yy;
     scanf("%d%d%d%d%d%d%d%d",&n,&a,&b,&c,&d,&x,&y,&m);
     for (i=0;i<n;i++)
     {
         s[x%3][y%3]++;
         xx=x;
         yy=y;
         x=(xx*a+b)%m;
         y=(yy*c+d)%m;
     }
     ans=0;
}

void dfs(int dep,int sx,int sy)
{
     if (dep==3) 
     {
        if ((!sx)&&(!sy)) ans+=now;
        return;
     }
     int i,j;
     for (i=0;i<3;i++)
         for (j=0;j<3;j++)
         if (s[i][j])
         {
            now*=s[i][j];
             s[i][j]--;
             dfs(dep+1,(sx+i)%3,(sy+j)%3);
             s[i][j]++;
             now/=s[i][j];
         }
}

void print()
{
     ans/=6;
     printf("Case #%d: %I64d\n",t,ans);
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&test),t=1;t<=test;t++)
    {
        init();
        now=1;
        dfs(0,0,0);
        print();
    }
}
