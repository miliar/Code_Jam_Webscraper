#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string.h>
using namespace std;

char g[10][10];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int iCase=0;
    while(T--)
    {
        iCase++;
        for(int i=0;i<4;i++)
           scanf("%s",&g[i]);
        printf("Case #%d: ",iCase);
        bool flag1=false,flag2=false;

        for(int i=0;i<4;i++)
        {
            int t1=0,t2=0;
            for(int j=0;j<4;j++)
            {
                if(g[i][j]=='O'||g[i][j]=='T')t1++;
                if(g[i][j]=='X'||g[i][j]=='T')t2++;
            }
            if(t1==4)
            {
                flag1=true;
                break;
            }
            if(t2==4)
            {
                flag2=true;
                break;
            }
        }
        if(flag1)
        {
            printf("O won\n");
            continue;
        }
        if(flag2)
        {
            printf("X won\n");
            continue;
        }

        for(int i=0;i<4;i++)
        {
            int t1=0,t2=0;
            for(int j=0;j<4;j++)
            {
                if(g[j][i]=='O'||g[j][i]=='T')t1++;
                if(g[j][i]=='X'||g[j][i]=='T')t2++;
            }
            if(t1==4)
            {
                flag1=true;
                break;
            }
            if(t2==4)
            {
                flag2=true;
                break;
            }
        }
        if(flag1)
        {
            printf("O won\n");
            continue;
        }
        if(flag2)
        {
            printf("X won\n");
            continue;
        }
        int t1=0,t2=0;
        for(int i=0;i<4;i++)
        {
            if(g[i][i]=='O'||g[i][i]=='T')t1++;
            if(g[i][i]=='X'||g[i][i]=='T')t2++;
            if(t1==4)
            {
                flag1=true;
                break;
            }
            if(t2==4)
            {
                flag2=true;
                break;
            }
        }
        if(flag1)
        {
            printf("O won\n");
            continue;
        }
        if(flag2)
        {
            printf("X won\n");
            continue;
        }
        t1=0,t2=0;
        for(int i=0;i<4;i++)
        {
            if(g[i][3-i]=='O'||g[i][3-i]=='T')t1++;
            if(g[i][3-i]=='X'||g[i][3-i]=='T')t2++;
            if(t1==4)
            {
                flag1=true;
                break;
            }
            if(t2==4)
            {
                flag2=true;
                break;
            }
        }
        if(flag1)
        {
            printf("O won\n");
            continue;
        }
        if(flag2)
        {
            printf("X won\n");
            continue;
        }
        t1=0;
        for(int i=0;i<4;i++)
          for(int j=0;j<4;j++)
            if(g[i][j]=='.')
              t1++;
        if(t1>0)printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
