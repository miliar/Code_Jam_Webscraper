#include"stdio.h"
int cas;
char a[5][5],win,x;
int chkh()
{
    int c;
    for(int i=0;i<4;i++)
    {
        x=a[i][0];
        if(x=='T')
            x=a[i][1];
        if(x=='.')
            continue;
        c=1;
        for(int j=0;j<4;j++)
            if(a[i][j]==x||a[i][j]=='T')
                c++;
            else
                break;
        if(c==5)
        {
            win=x;
            return 1;
        }
    }
    return 0;
}
int chkv()
{
    int c;
    for(int j=0;j<4;j++)
    {
        x=a[0][j];
        if(x=='T')
            x=a[1][j];
        if(x=='.')
            continue;
        c=1;
        for(int i=0;i<4;i++)
            if(a[i][j]==x||a[i][j]=='T')
                c++;
            else
                break;
        if(c==5)
        {
            win=x;
            return 1;
        }
    }
    return 0;
}
int chkd()
{
    int c;
    int b=1;

    x=a[0][0];
    while(b++==1&&x!='.')
    {
        if(x=='T')
            x=a[1][1];
        if(x=='.')
            break;

        c=1;
        for(int i=0;i<4;i++)
            if(a[i][i]==x||a[i][i]=='T')
                c++;
            else
                break;
        if(c==5)
        {
            win=x;
            return 1;
        }
    }
    b=1;
    x=a[0][3];
    while(b++==1&&x!='.')
    {
        if(x=='T')
            x=a[1][2];

        if(x=='.')
            break;

        c=1;
        for(int i=0;i<4;i++)
            if(a[i][3-i]==x||a[i][3-i]=='T')
                c++;
            else
                break;
        if(c==5)
        {
            win=x;
            return 1;
        }
    }
    return 0;
}
main()
{
    FILE *p1, *p2;
    p1=fopen("A-large.in","r");
    p2=fopen("hii2.in","w");
    char sp;
    fscanf(p1,"%d",&cas);
    for(int k=1;k<=cas;k++)
    {
        int n,m,end=1;
        win='A';
        for(int i=0;i<4;i++)
        {
            fscanf(p1,"%s",a[i]);
            for(int j=0;j<4;j++)
                if(a[i][j]=='.')
                    end=0;
        }
        if(chkv()==0)
        {
            //printf("hi");
            if(chkh()==0)
            {
                //printf("hi");
                chkd();
            }
        }

        fprintf(p2,"Case #%d: ",k);
        if(win!='A')
            fprintf(p2,"%c won\n",win);
        else
            if(end==0)
                fprintf(p2,"Game has not completed\n");
            else
                fprintf(p2,"Draw\n");
        fscanf(p1,"%c",&sp);
    }
}
