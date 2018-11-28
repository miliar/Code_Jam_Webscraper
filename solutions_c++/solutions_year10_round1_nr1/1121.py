#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cmath>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>

#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<ctype.h>

using namespace std;

#define oo          (1<<30)
#define PI          3.141592653589793
#define pi          2*acos(0)
#define ERR         1e-5
#define PRE         1e-8
#define SZ          size()
#define PB          push_back
#define LL          long long
#define ISS         istringstream
#define OSS         ostringstream
#define VS          vector<string>
#define VI          vector<int>
#define VD          vector<double>
#define VLL         vector<long long>
#define SII         set<int>::iterator
#define SI          set<int>
#define mem(a,b)    memset(a,b,sizeof(a))
#define fi(i,a,b)   for(i=a;i<b;i++)
#define fd(i,a,b)   for(i=a;i>b;i--)
#define fii(a,b)    for(i=a;i<b;i++)
#define fdi(a,b)    for(i=a;i>b;i--)
#define fij(a,b)    for(j=a;j<b;j++)
#define fdj(a,b)    for(j=a;j>b;j--)
#define fik(a,b)    for(k=a;k<b;k++)
#define fdk(a,b)    for(k=a;k>b;k--)
#define fil(a,b)    for(l=a;l<b;l++)
#define fdl(a,b)    for(l=a;l>b;l--)
#define ri(i,a)     for(i=0;i<a;i++)
#define rd(i,a)     for(i=a;i>-1;i--)
#define rii(a)      for(i=0;i<a;i++)
#define rdi(a)      for(i=a;i>-1;i--)
#define rij(a)      for(j=0;j<a;j++)
#define rdj(a)      for(j=a;j>-1;j--)
#define rik(a)      for(k=0;k<a;k++)
#define rdk(a)      for(k=a;k>-1;k--)
#define ril(a)      for(l=0;l<a;l++)
#define rdl(a)      for(l=a;i>-1;l--)
#define EQ(a,b)     (fabs(a-b)<ERR)
#define all(a,b,c)  for(int I=0;I<b;I++)    a[I] = c
#define CROSS(a,b,c,d)  ((b.x-a.x)*(d.y-c.y)-(d.x-c.x)*(b.y-a.y))

typedef struct{int x,y;}P;

int dp[52][52][4];
int bb[52][52];
char b[52][52];

void FF(int n,int d)
{
    int i,j;
    rii(n)rij(n)
        if(bb[i][j]==d)
        {
            dp[i][j][0] = dp[i][j][1] = dp[i][j][2] = dp[i][j][3] =1;
            if(i>0) dp[i][j][0] = dp[i-1][j][0]+1;  //  |


            if(i>0&&j>0) dp[i][j][1] = dp[i-1][j-1][1]+1;  //  \


            if(i>0) dp[i][j][2] = dp[i-1][j+1][2]+1;  //  /


            if(j>0) dp[i][j][3] = dp[i][j-1][3]+1;  //  -

        }
}

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int r,ks=1,T,n,K,i,j,k,l,B,R,m;

    scanf("%d",&T);

    while(T--)
    {

        scanf("%d%d",&n,&K);
        rii(n)  scanf("%s",b[i]);

        memset(bb,0,sizeof(bb));

        for(k=0,i=n-1;i>-1;i--,k++)
        {
            l=0;
            for(j=n-1;j>-1;j--)
            {
                if(b[i][j]=='B')    bb[k][l++] = 1;
                else if(b[i][j]=='R')    bb[k][l++] = 2;

            }

        }


        memset(dp,0,sizeof(dp));
        B=0;

        FF(n,1);
        m=0;

        rii(n)rij(n)rik(4)  m = max(m,dp[i][j][k]);
        if(m>=K)    B=1;

        memset(dp,0,sizeof(dp));
        R=0;

        FF(n,2);
        m=0;
        rii(n)rij(n)rik(4)  m = max(m,dp[i][j][k]);

        if(m>=K)    R=1;

        if(B && R)    printf("Case #%d: Both\n",ks++);
        else if(B)  printf("Case #%d: Blue\n",ks++);
        else if(R)  printf("Case #%d: Red\n",ks++);
        else  printf("Case #%d: Neither\n",ks++);
    }
    return 0;
}
