// GCJ2013_QR_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int main(int argc, char* argv[])
{
    freopen("c:/txt/A-small-attempt0.in","r",stdin);
    freopen("c:/txt/2013-QR-A-small.txt","w",stdout);
    int i, j, k, T;
    scanf("%d",&T);
    char s[4][5]={0};
    int v[256]={0};
    // .:1  X:10  O:100  T:1000
    v['.']=1;
    v['X']=10;
    v['O']=100;
    v['T']=1000;
    for(i=0;i<T;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%s", &s[j]);
        }
        bool Awin=false, Bwin=false;
        for(j=0;j<4;j++)
        {
            int p=0, q=0;
            for(k=0;k<4;k++)
            {
                p+=v[s[j][k]];
                q+=v[s[k][j]];
            }
            if(p==40 || p==1030 || q==40 || q==1030)
            {
                Awin=true;
            }
            if(p==400 || p==1300 || q==400 || q==1300)
            {
                Bwin=true;
            }
        }
        int p=0, q=0;
        for(j=0;j<4;j++)
        {
            p+=v[s[j][j]];
            q+=v[s[j][4-j-1]];
        }
        if(p==40 || p==1030 || q==40 || q==1030)
        {
            Awin=true;
        }
        if(p==400 || p==1300 || q==400 || q==1300)
        {
            Bwin=true;
        }
        if(!Awin && !Bwin)
        {
            int x=0;
            for(j=0;j<4;j++)
            {
                for(k=0;k<4;k++)
                {
                    x+=v[s[j][k]];
                }
            }
            if(x%10)
            {
                printf("Case #%d: Game has not completed\n", i+1);
            }
            else
            {
                printf("Case #%d: Draw\n", i+1);
            }
        }
        else
        {
            if(Awin)
            {
                printf("Case #%d: X won\n", i+1);
            }
            else
            {
                printf("Case #%d: O won\n", i+1);
            }
        }
    }
    return 0;
}

