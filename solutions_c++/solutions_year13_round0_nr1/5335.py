#include<stdio.h>
#include<stdlib.h>
char grd[10][10];
int sv;
void rw(int i)
{
    char f=grd[i][0];
    for(int j=1;j<4;j++)
    if(grd[i][j] != f)
        return;
    if(f == '.')
        return;
    printf("%c won\n",f);
    sv=1;
    return;
}
void prn()
{
    int i,j;
    for(i=0;i<4;i++)
    {
    for(j=0;j<4;j++)
        printf("%c",grd[i][j]);
        printf("\n");
    }
}

void cl(int j)
{
    char f=grd[0][j];
    for(int i=1;i<4;i++)
    if(grd[i][j] != f)
    {
        /*if(j == 0)
        {
            prn();
            printf("in row %d grd %c f %c \n",i,grd[i][j],f);
        }*/
        return;
    }
    if(f == '.')
        return;        
    printf("%c won\n",f);
    sv=1;
    return;
}
void dgrt()
{
    char f=grd[0][3];
    for(int i=1;i<4;i++)
    if(grd[i][3-i] != f)
        return;
    if(f == '.')
        return;        
    printf("%c won\n",f);
    sv=1;
    return;
}
void dg()
{
    dgrt();
    char f=grd[0][0];
    for(int i=1;i<4;i++)
    if(grd[i][i] != f)
        return;
    if(f == '.')
        return;
    printf("%c won\n",f);
    sv=1;
    return;
}
void gvtry()
{
    dg();
    for(int i=0;i<4;i++)
    {
        if(sv == 1)
            break;
        rw(i);
        if(sv == 1)
            break;
        cl(i);  
    }
}
char str[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int i,j,ti,tj,t;
    scanf("%d",&t);
    for(int a=1;a<=t;a++)
    {
        sv=0;
        ti=-1;
        tj=-1;
        printf("Case #%d: ",a);
        for(i=0;i<4;i++)
        {
            scanf("%s",grd[i]);
            for(j=0;j<4;j++)
            {
                if(grd[i][j] == 'T')
                {
                    ti=i;
                    tj=j;
                }
            }
        }
        if(ti!=-1)
        {
            grd[ti][tj]='X';
            gvtry();
            if(sv == 1)
                continue;
            grd[ti][tj]='O';
            gvtry();        
            if(sv == 1)
                continue;
        }
        else
        {
            gvtry();
            if(sv == 1)
                continue;
        }
        for(i=0;i<4 && sv == 0;i++)
        for(j=0;j<4 && sv == 0;j++)        
        if(grd[i][j] == '.')
        {
            printf("Game has not completed\n");
            sv=1;
        }
        if(sv == 1)
            continue;
        printf("Draw\n");
        //scanf("%s",str);
    }

    
}
