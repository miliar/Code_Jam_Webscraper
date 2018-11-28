#include <iostream>

using namespace std;

int main()
{
    char game[5][5];
    int n,rr=1;
    scanf("%d",&n);
    while(n--)
    {
        for (int i=0;i<4;i++)
            scanf("%s",game[i]);
        printf("Case #%d: ",rr++);
        int nf = 0,win = 0;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
            {
                if (game[i][j]=='.') nf = 1;
            }
        if (!win)
            for (int i=0;i<4;i++)
            {
                char tmp;
                tmp = game[i][0];
                if (tmp == 'T') tmp = game[i][1];
                if (tmp == '.') continue;
                int flag = 1;
                for (int j=0;j<4;j++)
                {
                    if (game[i][j]=='T' || game[i][j]==tmp) continue;
                    else flag = 0;
                }
                if (flag) {printf("%c won\n",tmp);win =1;break;}
            }
        if (!win)
            for (int i=0;i<4;i++)
            {
                char tmp;
                tmp = game[0][i];
                if (tmp == 'T') tmp = game[1][i];
                if (tmp == '.') continue;
                int flag = 1;
                for (int j=0;j<4;j++)
                {
                    if (game[j][i]=='T' || game[j][i]==tmp) continue;
                    else flag = 0;
                }
                if (flag) {printf("%c won\n",tmp);win =1;break;}
            }
        if (!win)
        {
            char tmp;
            tmp = game[0][0];
            if (tmp == 'T') tmp = game[1][1];
            if (tmp == '.') tmp = 'L';
            int flag = 1;
            for (int j=0;j<4;j++)
            {
                if (game[j][j]=='T' || game[j][j]==tmp) continue;
                else flag = 0;
            }
            if (flag) {printf("%c won\n",tmp);win =1;}
        }
        if (!win)
        {
            char tmp;
            tmp = game[0][3];
            if (tmp == 'T') tmp = game[1][2];
            if (tmp == '.') tmp = 'L';
            int flag = 1;
            for (int j=0;j<4;j++)
            {
                if (game[j][3-j]=='T' || game[j][3-j]==tmp) continue;
                else flag = 0;
            }
            if (flag) {printf("%c won\n",tmp);win =1;}
        }
        if (!win)
            if (nf) printf("Game has not completed\n");
            else printf("Draw\n");
    }
    return 0;
}
