
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

const int inf = (1<<28);
const double pi = (2.0*acos(0.0));
const double eps = 1e-9;

#define _rep( i, a, b, x ) for(  i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )

#define pb push_back
int N , S ,P , tot[150];

int dp[102][102] ;
int solve(int n , int s)
{
    if(s>S) return -inf;
    if(n==N)
    {
        if(s==S) return 0;
        return -inf;
    }
    int &ret = dp[n][s];
    if(ret!=-1) return ret;
    ret=0;
    int i,j,k;
    ret = max(ret,solve(n+1,s));
    for(i=0;i<=10;i++)
    for(j=i;j<=10;j++)
    for(k=j;k<=10;k++)
    {
        if(k-i>2) continue;
        if(i+j+k != tot[n]) continue;

        if(k-i<2 && k>=P)
            ret = max(ret , 1+solve(n+1,s));
        if(k-i==2)
        {
            if(k<P) ret = max(ret ,solve(n+1,s+1));
            if(k>=P)ret = max(ret ,1+solve(n+1,s+1));
        }
    }
    return ret;
}
int main(void)
{
    //freopen("B-large.in","r",stdin);
    //freopen("in.txt","r",stdin);
    //freopen("outbbb.txt","w",stdout);
    int i,j,k,kase=0;
    int t;scanf("%d",&t);
    while(t--)
    {
        scanf("%d %d %d",&N,&S,&P);
        rep(i,N) scanf("%d",&tot[i]);
        memset(dp,-1,sizeof(dp));
        int ans = solve(0,0);
        printf("Case #%d: %d\n",++kase,ans);
    }
    return 0;
}
