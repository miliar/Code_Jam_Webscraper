#include <stdio.h>
char s[5][5];
void ctr(int x,int &p,int &t,char c)
{
    for(int i=0;i<4;i++)
    {
        if(s[x][i]==c)p++;
        if(s[x][i]=='T')t++;
    }
}
void ctw(int x,int &p,int &t,char c)
{
    for(int i=0;i<4;i++)
    {
        if(s[i][x]==c)p++;
        if(s[i][x]=='T')t++;
    }
}
void ctd1(int &p,int &t,char c)
{
    for(int i=0;i<4;i++)
    {
        if(s[i][i]==c)p++;
        if(s[i][i]=='T')t++;
    }
}
void ctd2(int &p,int &t,char c)
{
    for(int i=0;i<4;i++)
    {
        if(s[i][3-i]==c)p++;
        if(s[i][3-i]=='T')t++;
    }
}
int main()
{
    //freopen("answer.out","w",stdout);
    int T,p,t,u=0;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",++u);
        int ct=0;
        for(int i=0;i<4;i++)
        {
            scanf("%s",s[i]);
            for(int j=0;j<4;j++)
            if(s[i][j]=='.')ct++;
        }
        int fx=0,fo=0;
        for(int i=0;i<4;i++)
        {
            p=t=0;
            ctr(i,p,t,'X');
            if(p+t==4)fx=1;
            p=t=0;
            ctr(i,p,t,'O');
            if(p+t==4)fo=1;
        }
        for(int i=0;i<4;i++)
        {
            p=t=0;
            ctw(i,p,t,'X');
            if(p+t==4)fx=1;
            p=t=0;
            ctw(i,p,t,'O');
            if(p+t==4)fo=1;
        }
        p=t=0;
        ctd1(p,t,'X');
        if(p+t==4)fx=1;
        p=t=0;
        ctd2(p,t,'X');
        if(p+t==4)fx=1;
        p=t=0;
        ctd1(p,t,'O');
        if(p+t==4)fo=1;
        p=t=0;
        ctd2(p,t,'O');
        if(p+t==4)fo=1;
        if(fx==1)printf("X won\n");
        else if(fo==1)printf("O won\n");
        else if(ct==0)printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}
