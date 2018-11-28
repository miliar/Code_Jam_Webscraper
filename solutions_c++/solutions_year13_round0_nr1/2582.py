#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char g[5][5];
char s[5];
int main()
{
    int t,n,i,j;
    freopen("as.in","r",stdin);
    freopen("as.out","w",stdout);
    scanf("%d",&t);
    getchar();
    for(int cnt = 1;cnt<=t;cnt++)
    {
        for(i=0;i<5;i++)
            gets(g[i]);

        //for(i=0;i<4;i++)
        //    puts(g[i]);
        int tr,tc;
        for(i=0;i<4;i++)for(j=0;j<4;j++)
            if(g[i][j]=='T')
            {
                tr = i;
                tc = j;
            }
        int ow = 0, xw = 0;
        g[tr][tc] = 'O';
        for(i=0;i<4;i++)
        {
            if(!strcmp(g[i],"OOOO"))
            {
                ow = 1;
                break;
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                s[j] = g[j][i];
            if(!strcmp(s,"OOOO"))
            {
                ow = 1;
                break;
            }
        }

        for(i=0;i<4;i++)
            s[i] = g[i][i];
        if(!strcmp(s,"OOOO"))
            ow = 1;
        for(i=0;i<4;i++)
            s[i] = g[3-i][i];
        if(!strcmp(s,"OOOO"))
            ow = 1;
        g[tr][tc] = 'X';
        for(i=0;i<4;i++)
        {
            if(!strcmp(g[i],"XXXX"))
            {
                xw = 1;
                break;
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                s[j] = g[j][i];
            if(!strcmp(s,"XXXX"))
            {
                xw = 1;
                break;
            }
        }
        for(i=0;i<4;i++)
            s[i] = g[i][i];
        if(!strcmp(s,"XXXX"))
            xw = 1;
        for(i=0;i<4;i++)
            s[i] = g[3-i][i];
        if(!strcmp(s,"XXXX"))
            xw = 1;
        printf("Case #%d: ",cnt);
        if(ow)
        {
            printf("O won\n");
            continue;
        }

        if(xw)
        {
            printf("X won\n");
            continue;
        }
        int d = 1;
        for(i=0;i<4;i++)for(j=0;j<4;j++)if(g[i][j] == '.')
            d = 0;
        if(d)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}
