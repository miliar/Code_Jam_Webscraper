#include <iostream>
#include <algorithm>
#include <stdio.h>
using namespace std;
int n,m;
char s[1000];
char t[]="welcome to code jam";
int f[600][21];
int L;
int main()
{
    freopen("t2.in","r",stdin);
    freopen("t2.out","w",stdout);
    scanf("%d\n",&n);
    L = strlen(t);
  //  printf("L: %d\n",L);
    int ans;
    for(int i=1;i<=n;i++)
    {
        gets(s);
       // puts(s);
        m=strlen(s);
        memset(f,0,sizeof(f));

        int j,k;
        ans = 0;
        f[0][0]=1;
        for(j=0;j<m;j++)
        {
            for(k=0;k<L;k++)
            {
                f[j+1][k+1]+=(s[j]==t[k])*f[j][k];
                f[j+1][k+1]%=10000;

            }
            for(k=0;k<=L;k++)
            {
                f[j+1][k]+=f[j][k];
            //    printf("%d - %d : %d\n",j+1,k,f[j][k]);
                f[j+1][k]%=10000;

            }
        }
            ans+=f[m][L];
            ans%=10000;
        printf("Case #%d: %04d\n",i,ans%10000);
    }
    return 0;
}
