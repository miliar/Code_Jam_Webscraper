#include<cstdio>
#include<cstdlib>
#include<cstring>
#define MAXL 510
int N;
int CaseNum;
char tmp[]="welcome to code jam";
char now[MAXL];
int f[MAXL][19];
int L;
int ans;
void solve()
{
    memset(f,0,sizeof(f));
    memset(now,0,sizeof(now));
    int i,j,k;
    gets(now);
    L=strlen(now);
    for (i=0;i<L;i++)
    if (now[i]=='w')f[i][0]=1;

    for (i=1;i<19;i++)
    {
        for (j=1;j<L;j++)
        if (now[j]==tmp[i])
        {
            for (k=0;k<j;k++)
            if (now[k]==tmp[i-1])
            {
                f[j][i]+=f[k][i-1];
                f[j][i]%=10000;
            }
        }
    }
    ans=0;
    for (i=0;i<L;i++)
    if (now[i]==tmp[18])
    {
        ans+=f[i][18];
        ans%=10000;
    }
}
void print()
{
    CaseNum++;
    printf("Case #%d: %.4d\n",CaseNum,ans);
}
int main()
{
//    freopen("C-large.in","r",stdin);
//    freopen("C-large.out","w",stdout);
    scanf("%d\n",&N);
    int i;
    for (i=1;i<=N;i++)
    {
        solve();
        print();
    }
    return 0;
}
