#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int T;
    char g[4][10];
    int sxr[4],sxc[4];
    int sor[4],soc[4];
    int sx1,sx2,so1,so2;
    freopen("A-large.in","r",stdin);
    freopen("A_output_large.txt","w",stdout);
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        for (int i=0;i<4;i++) scanf("%s",g[i]);
        memset(sxr,0,sizeof(sxr));
        memset(sxc,0,sizeof(sxc));
        memset(sor,0,sizeof(sor));
        memset(soc,0,sizeof(soc));
        sx1=sx2=so1=so2=0;
        int counter=0;
        //row
        for (int i=0;i<4;i++)
        {
            for (int j=0;j<4;j++)
            {
                if (g[i][j]=='.') continue;
                counter++;
                if (g[i][j]=='X')
                {
                    sxr[i]++; sxc[j]++;
                }else if (g[i][j]=='O'){
                    sor[i]++; soc[j]++;
                }else if (g[i][j]=='T'){
                    sxr[i]++; sxc[j]++;
                    sor[i]++; soc[j]++;
                }
            }
            if (g[i][i]=='X' || g[i][i]=='T') sx1++;
            if (g[i][i]=='O' || g[i][i]=='T') so1++;
            if (g[i][3-i]=='X' || g[i][3-i]=='T') sx2++;
            if (g[i][3-i]=='O' || g[i][3-i]=='T') so2++;
        }
        printf("Case #%d: ",cases);
        bool find=false;
        for (int i=0;i<4;i++)
        {
            if (sxr[i]==4 || sxc[i]==4) find=true;
        }
        if (find)
        {
            printf("X won\n"); continue;
        }
        find=false;
        for (int i=0;i<4;i++)
        {
            if (sor[i]==4 || soc[i]==4) find=true;
        }
        if (find)
        {
            printf("O won\n"); continue;
        }
        if (sx1==4 || sx2==4)
        {
            printf("X won\n"); continue;
        }
        if (so1==4 || so2==4)
        {
            printf("O won\n"); continue;
        }
        if (counter<16) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
