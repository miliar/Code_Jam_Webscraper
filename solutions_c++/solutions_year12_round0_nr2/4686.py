#include <iostream>
#include <string.h>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <map>
#define pb push_back
#define MAXN 1
#define MAXM 1
#define INF (1<<30)
#define PI 3.1415926535898
#define esp 10e-6
const int dx[4]={1,0,-1,0};
const int dy[4]={0,-1,0,1};
using namespace std;
int n,p,s,ans;
int score[101];
class Point
{
      public:
             int x;
             int y;
};

int check(int x,int y,int z)
{
    if (x-y==2 || x-z==2 ||y-z==2||x-y==-2 ||x-z==-2||y-z==-2)
       return 1;
    return 0;
}

int calc(int x,int y,int z)
{
    if (x-y>2||x-z>2||y-z>2||y-x>2||z-x>2||z-y>2) return 0;
    return 1;
}

int dfs(int dep,int tot,int sum)
{
    if (tot>s) return 0;
    if (dep>=n) 
       {
       if (tot==s)
          if (sum>ans) ans=sum;
       return 0;
       }
    for (int i=0;i<11;++i)
        for (int j=0;j<11;++j)
            for (int k=0;k<11;++k)
                if (i+j+k==score[dep] && calc(i,j,k)!=0)
                   {
                   if (check(i,j,k))
                      if (i>=p||j>=p||k>=p)
                      dfs(dep+1,tot+1,sum+1);
                      else
                      dfs(dep+1,tot+1,sum);
                   else
                      if (i>=p||j>=p||k>=p)
                      dfs(dep+1,tot,sum+1);
                      else
                      dfs(dep+1,tot,sum);
                   }
}

int work()
{
    scanf("%d",&n);
    scanf("%d",&s);
    scanf("%d",&p);
    for (int i=0;i<n;++i)
        scanf("%d",&score[i]);
    ans=0;
    dfs(0,0,0);
    printf("%d\n",ans);
    return 0;
}

int main()
{
    freopen("B-small-attempt3.in","r",stdin);freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int i=1;i<=T;++i)
        {
        printf("Case #%d: ",i);
        work(); 
        } 
    return 0;
}
