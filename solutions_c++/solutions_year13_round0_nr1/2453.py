#include<cstdio>
int t;
char s[5][5];
int check()
{
    for(int i=0;i<4;i++)
    {
        int f1 = 1, f2 = 1;
        for(int j=0;j<4;j++)
        {
            if (s[i][j]!='O'&&s[i][j]!='T') f1=0;
        }
        for(int j=0;j<4;j++)
        {
            if (s[i][j]!='X'&&s[i][j]!='T') f2=0;
        }
        //printf("%d %d\n",f1,f2);
        if (f1) return 1;
        if (f2) return 2;
    }
    for(int i=0;i<4;i++)
    {
        int f1 = 1, f2 = 1;
        for(int j=0;j<4;j++)
        {
            if (s[j][i]!='O'&&s[j][i]!='T') f1=0;
        }
        for(int j=0;j<4;j++)
        {
            if (s[j][i]!='X'&&s[j][i]!='T') f2=0;
        }
        if (f1) return 1;
        if (f2) return 2;
    }
    int f1 = 1, f2 = 1;
    for(int i=0;i<4;i++) if (s[i][i]!='O'&&s[i][i]!='T') f1=0;
    for(int i=0;i<4;i++) if (s[i][i]!='X'&&s[i][i]!='T') f2=0;
    if (f1) return 1;
    if (f2) return 2;
    f1=1;f2=1;
    for(int i=0;i<4;i++) if (s[i][3-i]!='O'&&s[i][3-i]!='T') f1=0;
    for(int i=0;i<4;i++) if (s[i][3-i]!='X'&&s[i][3-i]!='T') f2=0;
    if (f1) return 1;
    if (f2) return 2;
    int empty=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if (s[i][j]=='.') empty=1;
    if (empty) return 3;
    return 0;
}
int main()
{
    freopen("Al.in","r",stdin);
    freopen("Al.out","w",stdout);
    scanf("%d",&t);
    for(int mt=1;mt<=t;mt++)
    {
        for(int i=0;i<4;i++) scanf("%s",s[i]);
        int ret=check();
        //printf("%d\n",ret);
        if (ret==0)
        {
            printf("Case #%d: Draw\n",mt);
        }
        if (ret==1)
        {
            printf("Case #%d: O won\n",mt);
        }
        if (ret==2)
        {
            printf("Case #%d: X won\n",mt);
        }
        if (ret==3)
        {
            printf("Case #%d: Game has not completed\n",mt);
        }
    }
}

