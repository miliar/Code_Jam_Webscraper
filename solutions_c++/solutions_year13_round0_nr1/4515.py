#include<cstdio>
int T,cs,dot;char g[5][5],tmp[5],winer;
char check(char *a)
{
    int j,t=0,o=0,x=0;
    for(j=0;j<4;j++)
    {
        if(a[j]=='X')x++;
        else if(a[j]=='O')o++;
        else if(a[j]=='T')t++;
        else dot++;
    }
    if((t==1 && x==3) || x==4)winer='X';
    if((t==1 && o==3) || o==4)winer='O';
    return winer;
}
int main()
{
    int i,j;
    freopen("tic.txt","r",stdin);
    freopen("ticans.txt","w",stdout);
    scanf("%d",&T);getchar();
    while(T--)
    {
        for(i=0;i<4;i++)gets(g[i]);dot=0;winer='A';

        for(i=0;i<4 && winer=='A';i++)
        {
            for(j=0;j<4;j++)tmp[j]=g[i][j];tmp[j]=0;
            winer=check(tmp);
        }
         for(i=0;i<4 && winer=='A';i++)
        {
            for(j=0;j<4;j++)tmp[j]=g[j][i];tmp[j]=0;
            winer=check(tmp);
        }
        if(winer=='A')
        {
            for(i=0;i<4;i++)tmp[i]=g[i][i];tmp[i]=0;
            winer=check(tmp);

        }
        if(winer=='A')
        {
            for(i=0;i<4;i++)tmp[i]=g[i][3-i];tmp[i]=0;
            winer=check(tmp);
        }
        //printf("%d\n",dot);
        printf("Case #%d:",++cs);
        if(winer=='X')puts(" X won");
        else if(winer=='O')puts(" O won");
        else if(dot==0)puts(" Draw");
        else puts(" Game has not completed");
        gets(tmp);
    }
    return 0;
}

