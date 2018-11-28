#include<iostream>
#include<cstring>
using namespace std;
#define MAXN 512
const char str[]={"welcome to code jam"};
const int lstr=19;
char buf[MAXN];
int lbuf;

int solve (   )
{
    int i,j,k,res,dp[MAXN][21];

    memset(dp,0,sizeof(dp));
    dp[0][0]=1;
    for ( i=1 ; i<=lbuf; i++ )
    {
        for ( j=1 ; j<=lstr ; j++ )
        {
            if ( buf[i-1]==str[j-1] )
             for ( k=0 ; k<i ; k++ )
                 dp[i][j]=(dp[i][j]+dp[k][j-1])%10000;
        }
    }
    for ( res=0,i=1 ; i<=lbuf  ; i++ )
        res=(res+dp[i][lstr])%10000;
    return res;
}

int main ( )
{
    int n,res,k;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    while ( scanf("%d",&n)!=EOF )
    {
        getchar();
        for ( k=1 ; k<=n ; k++ )
        {
            gets(buf);
            lbuf=strlen(buf);
            res=solve();
            printf("Case #%d: %04d\n",k,res);
        }
    }
}
