#include<stdio.h>
#include<string>
#include<iostream>
#include<string.h>
using namespace std;
int a,b,c,d,e,f,g,ful;
string s;
int zz[10][10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        memset(zz,-1,sizeof(zz));
        ful=1;
        for (c=1;c<=4;c++)
        {
            cin >> s;
            for (d=0;d<4;d++)
            {
                if (s[d]=='X')
                    zz[c][d+1]=1;
                else if (s[d]=='O')
                    zz[c][d+1]=2;
                else if (s[d]=='T')
                    zz[c][d+1]=3;
                else ful=0;
            }
        }
        g=-1;
        for (c=1;c<=4;c++)
        {
            f=0;
            e=zz[c][1];
            if (e==3) e=zz[c][2];
            if (e==-1) continue;
            for (d=1;d<=4;d++)
                if (zz[c][d]!=e && zz[c][d]!=3)
                {
                    f=1;
                    break;
                }
            if (f==0)
            {
                g=e;
                break;
            }
        }
        for (d=1;d<=4;d++)
        {
            f=0;
            e=zz[1][d];
            if (e==3) e=zz[2][d];
            if (e==-1){continue;}
            for (c=1;c<=4;c++)
                if (zz[c][d]!=e && zz[c][d]!=3)
                {
                    f=1;
                    break;
                }
            if (f==0)
            {
                g=e;
                break;
            }
        }
        f=0;
        e=zz[1][1];
        if (e==3) e=zz[2][2];
        if (e!=-1)
        {
            for (c=1;c<=4;c++)
                if (zz[c][c]!=e && zz[c][c]!=3)
                {
                    f=1;
                    break;
                }
            if (f==0)
                g=e;
        }
        f=0;
        e=zz[1][4];
        if (e==3) e=zz[2][3];
        if (e!=-1)
        {
            for (c=1;c<=4;c++)
                if (zz[c][4-c+1]!=e && zz[c][4-c+1]!=3)
                {
                    f=1;
                    break;
                }
            if (f==0)
                g=e;
        }
        printf("Case #%d: ",b);
        if (g!=-1)
        {
            if (g==1)
                printf("X won\n");
            else
                printf("O won\n");
        }
        else
        {
            if (ful)
                printf("Draw\n");
            else
                printf("Game has not completed\n");
        }
    }
    return 0;
}
