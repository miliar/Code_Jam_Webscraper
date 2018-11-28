# include <stdio.h>
# include <string>
# include <algorithm>

using namespace std;

# define inf 100000000

char s[101][100];
char t[1001][100];
int f[1001][101];
int n,m,case_cnt;

void readin()
{
    scanf("%d",&n);
    gets(s[0]);
    for (int i=1;i<=n;i++)
        gets(s[i]);
    scanf("%d",&m);
    gets(t[0]);
    for (int i=1;i<=m;i++)
        gets(t[i]);
}

void process()
{
    for (int i=1;i<=n;i++)
        if (!strcmp(t[1],s[i]))
            f[1][i]=inf;
        else
            f[1][i]=0;
    for (int i=2;i<=m;i++)
        for (int j=1;j<=n;j++) {
            f[i][j]=inf;
            if (strcmp(s[j],t[i])!=0) {
                for (int k=1;k<=n;k++)
                    if (strcmp(s[j],s[k]))
                        f[i][j]=min(f[i][j],f[i-1][k]+1);
                    else
                        f[i][j]=min(f[i][j],f[i-1][k]);
            }
        }
    int ans=inf;
    for (int i=1;i<=n;i++)
        ans=min(ans,f[m][i]);
    printf("Case #%d: %d\n",++case_cnt,ans);
}

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    
    int casen;
    scanf("%d",&casen);
    while (casen--) {
        readin();
        process();
    }
}
