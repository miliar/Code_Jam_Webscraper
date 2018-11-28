#include<cstdio>
char tab[10][10];

int solve()
{
    for(int i=0;i<4;i++)scanf(" %s",tab[i]);
    //for(int i=0;i<4;i++)printf("#%s#\n",tab[i]);
    int x=0,o=0;
    bool pelne=true;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(tab[i][j]=='X')x+=(1<<(4*i+j));
            if(tab[i][j]=='O')o+=(1<<(4*i+j));
            if(tab[i][j]=='T'){x+=(1<<(4*i+j));o+=(1<<(4*i+j));}
            if(tab[i][j]=='.')pelne=false;
        }

    int w=4369,p1=33825,p2=4680;
    //printf("%d %d\n",x,o);
    //spr x
    for(int i=0;i<16;i+=4)if((x&(15*(1<<i)))== (15*(1<<i)))return 0;
    for(int i=0;i<4;i++)if((x&(w*(1<<i)))== (w*(1<<i)))return 0;
    if((x&p1)==p1)return 0;
    if((x&p2)==p2)return 0;
    //spr o
    for(int i=0;i<16;i+=4)if((o&(15*(1<<i)))== (15*(1<<i)))return 1;
    for(int i=0;i<4;i++)if((o&(w*(1<<i)))== (w*(1<<i)))return 1;
    if((o&p1)==p1)return 1;
    if((o&p2)==p2)return 1;

    return pelne?2:3;
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int k=solve();
        switch(k)
        {
            case 0:
            printf("Case #%d: X won\n",i+1);break;
            case 1:
            printf("Case #%d: O won\n",i+1);break;
            case 2:
            printf("Case #%d: Draw\n",i+1);break;
            case 3:
            printf("Case #%d: Game has not completed\n",i+1);break;
        }
    }
    return 0;
}
