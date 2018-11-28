#include <iostream>
#include <algorithm>
using namespace std;
char f[200][200];
char s[200][200];
int n,m;
int main()
{
        freopen("C:/Users/FengJinwen/Desktop/A-large.in", "r", stdin);
    freopen("C:/Users/FengJinwen/Desktop/ans.txt", "w", stdout);
    int t,p,i,j,less,k,pless,ans;
    scanf("%d",&t);
    for (p=1;p<=t;p++)
    {
        ans=0;
        scanf("%d%d",&n,&m);
        for (i=1;i<=n;i++)
        {
            scanf("%s",f[i]);
            less=strlen(f[i]);
            f[i][less]='/';
            f[i][less+1]='\0';
            f[i][0]=' ';
        }
        for (i=1;i<=m;i++)
        {
            scanf("%s",s[i]);
            less=strlen(s[i]);
            s[i][less]='/';
            s[i][less+1]='\0';
            s[i][0]=' ';
        }
        for (i=1;i<=m;i++)
        {
            less=0;
            for (j=1;j<=n;j++)
            {
                pless=0;
                for (k=0;k<strlen(f[j]);k++)
                {
                    if (f[j][k]==s[i][k])
                    {
                        if (f[j][k]=='/')
                            pless++;

                    }
                    else break;
                }
                if (less<pless) less=pless;
            }
            pless=0;
            for (j=0;j<strlen(s[i]);j++)
                if (s[i][j]=='/') pless++;
            if (pless>less)
            {
                n++;
                strcpy(f[n],s[i]);
                ans+=pless-less;
            }
        }
        printf("Case #%d: %d\n",p,ans);
    }
}
