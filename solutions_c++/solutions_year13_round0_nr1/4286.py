#include <stdio.h>
char a[5][5];
int check(char q)
{
    int tcount=0;
    int no=1;
    for(int i=0;i<4;i++)
    {
        tcount=0;
        no=0;
        for(int j=0;j<4;j++)
        {
            if(a[i][j]=='T')
                tcount++;
            else
            if(a[i][j]!=q)
                no=1;
        }
        if(!no)
        if(tcount<=1)
            return 1;
    }
    for(int i=0;i<4;i++)
    {
        tcount=0;
        no=0;
        for(int j=0;j<4;j++)
        {
            if(a[j][i]=='T')
                tcount++;
            else
            if(a[j][i]!=q)
                no=1;
        }
        if(!no)
        if(tcount<=1)
            return 1;
    }
    tcount=0;
    no=0;
    for(int i=0;i<4;i++)
    {
        if(a[i][i]=='T')
            tcount++;
        else
        if(a[i][i]!=q)
            no=1;
    }
    if(!no)
    if(tcount<=1)
        return 1;

    tcount=0;
    no=0;
    for(int i=0;i<4;i++)
    {
        if(a[i][3-i]=='T')
            tcount++;
        else
        if(a[i][3-i]!=q)
            no=1;
        //printf("%c",a[i][3-i]);
    }
    //printf("%d %d\n",tcount,no);
    if(!no)
    if(tcount<=1)
        return 1;

    return 0;
}
int main()
{
    int total;
    FILE *in=fopen("A-large.in","r");
    FILE *out=fopen("output2.txt","w");
    fscanf(in,"%d",&total);

    for(int o=0;o<total;o++)
    {
        for(int i=0;i<4;i++)
        {
            fscanf(in," %s",a[i]);
        }
        fprintf(out,"Case #%d: ",o+1);
        if(check('X'))
        {
            fprintf(out,"X won");
        }
        else
        if(check('O'))
        {
            fprintf(out,"O won");
        }
        else
        {
            int noend=0;
            for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(a[i][j]=='.' && !noend)
                {
                    fprintf(out,"Game has not completed");
                    noend=1;
                }
            if(!noend)
                fprintf(out,"Draw");
        }
        fprintf(out,"\n");
    }
    return 0;
}
