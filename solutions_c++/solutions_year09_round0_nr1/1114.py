#include<cstdio>
#include<cstring>
#include<cstdlib>
#define MAXL 20
#define MAXD 5010
#define MAXN 510
int L,D,N;
bool now[MAXL][26];
char dict[MAXD][MAXL];
int CaseNum;
int ans;
void init()
{
     int i,j;
     for (i=1;i<=D;i++)
     {
        for (j=1;j<=L;j++)scanf("%c",&dict[i][j]);
        scanf("\n");
     }
}
void solve()
{
    int i=1,j;
    bool MUL=false;
    char tmp;
    memset(now,0,sizeof(now));
    ans=0;
    while (i<=L)
    {
        scanf("%c",&tmp);
        if (tmp=='(')MUL=true;
        if (tmp==')'){MUL=false;i++;}
        if ('a'<=tmp&&tmp<='z')
        {
            now[i][tmp-'a']=true;
            if (!MUL)i++;
        }
    }
    scanf("\n");
    bool flag;
    for (i=1;i<=D;i++)
    {
        flag=true;
        for (j=1;j<=L;j++)
        if (!now[j][dict[i][j]-'a'])
        {
            flag=false;
            break;
        }
        if (flag)ans++;
    }
}
void print()
{
    printf("Case #%d: %d\n",CaseNum,ans);
}
int main()
{
    scanf("%d%d%d\n",&L,&D,&N);
    init();
    int i;
    for (i=1;i<=N;i++)
    {
        CaseNum++;
        solve();
        print();
    }
    return 0;
}
