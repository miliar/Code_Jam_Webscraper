#include<stdio.h>
#include<string.h>
char a[5][5];
int main()
{
    int test,k,i,j,o,x,t,dot;
    char w;
    int flg;
    freopen("C://Users//Sheemul//Downloads//A-large.in","r",stdin);
    //freopen("E://Anamul Kabir//output.txt","a",stdout);
    scanf("%d",&test);
    for(k=0;k<test;k++)
    {
        for(i=0;i<4;i++) scanf("%s",a[i]);
        flg=0;
        w='N';
        for(i=0;i<4;i++)
        {
            o=x=t=0;
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='O') o++;
                else if(a[i][j]=='X') x++;
                else if(a[i][j]=='T') t++;
            }
            if(o==4||(o==3&&t==1))
            {
                w='O';
                flg=2;
            }
            else if(x==4||(x==3&&t==1))
            {
                w='X';
                flg=2;
            }
            if(flg) break;
            o=x=t=0;
            for(j=0;j<4;j++)
            {
                if(a[j][i]=='O') o++;
                else if(a[j][i]=='X') x++;
                else if(a[j][i]=='T') t++;
            }
            if(o==4||(o==3&&t==1))
            {
                w='O';
                flg=2;
            }
            else if(x==4||(x==3&&t==1))
            {
                w='X';
                flg=2;
            }
            if(flg) break;
        }
        if(!flg)
        {
            o=x=t=0;
            for(i=0;i<4;i++)
            {
                if(a[i][i]=='O') o++;
                else if(a[i][i]=='X') x++;
                else if(a[i][i]=='T') t++;
            }
            if(o==4||(o==3&&t==1))
            {
                w='O';
                flg=2;
            }
            else if(x==4||(x==3&&t==1))
            {
                w='X';
                flg=2;
            }
        }
        if(!flg)
        {
            o=x=t=0;
            for(i=0;i<4;i++)
            {
                if(a[i][3-i]=='O') o++;
                else if(a[i][3-i]=='X') x++;
                else if(a[i][3-i]=='T') t++;
            }
            if(o==4||(o==3&&t==1))
            {
                w='O';
                flg=2;
            }
            else if(x==4||(x==3&&t==1))
            {
                w='X';
                flg=2;
            }
        }
        freopen("E://Anamul Kabir//output.txt","a",stdout);
        if(flg)
        {
            if(w=='O') printf("Case #%d: O won\n",k+1);
            else printf("Case #%d: X won\n",k+1);
        }
        else
        {
            dot=0;
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                if(a[i][j]=='.') dot++;
            }
            if(dot) printf("Case #%d: Game has not completed\n",k+1);
            else printf("Case #%d: Draw\n",k+1);
        }
    }
}
