#include<stdio.h>

FILE *in=fopen("input.in","r");
FILE *out=fopen("output.out","w");
char x[4][5];
int q;

int checkr()
{
    int i,j;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
            if(x[i][j]=='O'||x[i][j]=='.')
                break;
        if(j==4)
        {
            fprintf(out,"Case #%d: X won\n",q);
            return 0;
        }
        for(j=0; j<4; j++)
            if(x[i][j]=='X'||x[i][j]=='.')
                break;
        if(j==4)
        {
            fprintf(out,"Case #%d: O won\n",q);
            return 0;
        }
    }
    return 1;
}

int checkc()
{
    int i,j;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
            if(x[j][i]=='O'||x[j][i]=='.')
                break;
        if(j==4)
        {
            fprintf(out,"Case #%d: X won\n",q);
            return 0;
        }
        for(j=0; j<4; j++)
            if(x[j][i]=='X'||x[j][i]=='.')
                break;
        if(j==4)
        {
            fprintf(out,"Case #%d: O won\n",q);
            return 0;
        }
    }
    return 1;
}

int checkd()
{
    int i;
        for(i=0; i<4; i++)
            if(x[i][i]=='O'||x[i][i]=='.')
                break;
        if(i==4)
        {
            fprintf(out,"Case #%d: X won\n",q);
            return 0;
        }
        for(i=0; i<4; i++)
            if(x[i][i]=='X'||x[i][i]=='.')
                break;
        if(i==4)
        {
            fprintf(out,"Case #%d: O won\n",q);
            return 0;
        }
        for(i=0; i<4; i++)
            if(x[i][3-i]=='O'||x[i][3-i]=='.')
                break;
        if(i==4)
        {
            fprintf(out,"Case #%d: X won\n",q);
            return 0;
        }
        for(i=0; i<4; i++)
            if(x[i][3-i]=='X'||x[i][3-i]=='.')
                break;
        if(i==4)
        {
            fprintf(out,"Case #%d: O won\n",q);
            return 0;
        }
        return 1;
}

int checke()
{
    int i,j;
    for(i=0; i<4; i++)
        for(j=0; j<4; j++)
            if(x[i][j]=='.')
            {
                fprintf(out,"Case #%d: Game has not completed\n",q);
                return 0;
            }
    return 1;
}

void check()
{
    int f=1;
    if(f) f=checkr();
    if(f) f=checkc();
    if(f) f=checkd();
    if(f) f=checke();
    if(f) fprintf(out,"Case #%d: Draw\n",q);
    return;
}

int main()
{
    int j,n;
    fscanf(in,"%d",&n);
    for(q=1; q<=n; q++)
    {
        for(j=0;j<4;j++)
            fscanf(in,"%s",x[j]);
        check();
    }
    return 0;
}
