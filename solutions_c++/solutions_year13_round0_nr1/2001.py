#include <cstdio>
#include <cctype>

using namespace std;

int main(void)
{
    int t, i, j, sx, so, tc=0, chk[10][4]={{0,1,2,3},{4,5,6,7},{8,9,10,11},{12,13,14,15},{0,4,8,12},{1,5,9,13},{2,6,10,14},{3,7,11,15},{0,5,10,15},{3,6,9,12}};
    char chr[20];
    bool vx, vo, ve;
    for (scanf("%d", &t);t--;)
    {
        ve=0;
        for (i=0;i<4;i++)
        {
            scanf("%s", chr+(i<<2));
            for (j=0;j<4;j++)
                ve|=(chr[(i<<2)+j]=='.');
        }
        sx=so=0;
        for (i=0;i<10;i++)
        {
            vx=vo=1;
            for (j=0;j<4;j++)
            {
                vx&=(toupper(chr[chk[i][j]])=='T' || toupper(chr[chk[i][j]])=='X');
                vo&=(toupper(chr[chk[i][j]])=='T' || toupper(chr[chk[i][j]])=='O');
            }
            sx+=vx;
            so+=vo;
        }
        printf("Case #%d: ", ++tc);
        if (sx!=so)
           printf("%s\n", (sx>so) ? ("X won") : ("O won"));
        else
           printf("%s\n", (ve) ? ("Game has not completed") : ("Draw"));
    }
    return 0;
}
