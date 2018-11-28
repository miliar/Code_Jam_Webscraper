/*
	Siyao
 	2009.08
*/
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
char str[]="welcome to code jam";
int dp[510][20];
char tmp[510];
int n,i,ii,jj,ans;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("smallout.txt","w",stdout);
    scanf("%d",&n);
    for(i=0;i<n;++i)
    {
            printf("Case #%d: ",i+1);
            while(gets(tmp)&&tmp[0]==0);
            int len=strlen(tmp);
            dp[0][0]=1;ans=0;
            for(ii=1;ii<=len;++ii)
            {
                    dp[ii][0]=1;
                    for(jj=1;jj<20;++jj)
                    {
                          dp[ii][jj]=dp[ii-1][jj];
                          if(tmp[ii-1]==str[jj-1])
                          {
                                dp[ii][jj]+=dp[ii-1][jj-1];
                          }
                         // printf("%d ",dp[ii][jj]);
                          dp[ii][jj]%=10000;
                    }
                  //  printf("\n");
            }
            printf("%04d\n",dp[len][19]);
    }
	return 0;
}
