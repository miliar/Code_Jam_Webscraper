#include<stdio.h>
#include<cstring>
#include<algorithm>
#include<string.h>
int main ()
{
    int t;
    freopen ("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    char winner='n';
    bool winner1=0,winner2=0,flag1,flag2;
    char c1='.',c2='.';
    char Tic[5][5];
    bool end=1;
    scanf ("%d",&t);
    int T=1;
    while (t--)
    {
        c1='.';c2='.';
        winner='n';
        winner1=0,winner2=0;
        end=1;
        for (int i=0;i<4;i++)
            scanf("%s",Tic[i]);

        for (int i=0;i<4;i++)
        {
            if (winner1&&c1!='.')
                winner=c1;
            if (winner2&&c2!='.')
                winner=c2;
            winner1=1;
            winner2=1;
            flag1=0,flag2=0;
            for (int c=0;c<4;c++)
            {
                if (Tic[i][c]=='.'||Tic[c][i]=='.')
                    end=0;
                if (!flag1)
                    c1=Tic[i][c];
                if (!flag2)
                    c2=Tic[c][i];

                if (c1!='T')
                    flag1=1;
                if (c2!='T')
                    flag2=1;

                if (flag1&&c1!=Tic[i][c]&&Tic[i][c]!='T')
                    winner1=0;
                if (flag2&&c2!=Tic[c][i]&&Tic[c][i]!='T')
                    winner2=0;
            }
        }
        if (winner1&&c1!='.')
            winner=c1;
        if (winner2&&c2!='.')
            winner=c2;
        flag1=0,flag2=0;
        winner1=1,winner2=1;
        for (int i=0;i<4;i++)
        {
            if (!flag1)
                c1=Tic[i][i];
            if (!flag2)
                c2=Tic[i][3-i];
            if (c1!='T')
                flag1=1;
            if (c2!='T')
                flag2=1;
            if (flag1&&c1!=Tic[i][i]&&Tic[i][i]!='T')
                winner1=0;
            if (flag2&&c2!=Tic[i][3-i]&&Tic[i][3-i]!='T')
                winner2=0;
        }
        if (winner1&&c1!='.')
            winner=c1;
        if (winner2&&c2!='.')
            winner=c2;
        printf("Case #%d: ",T);
        if (winner=='X')
            printf("X won\n");
        else if (winner=='O')
            printf("O won\n");
        else if (winner=='n'&&!end)
            printf("Game has not completed\n");
        else if (winner=='n'&&end)
            printf("Draw\n");
        T++;
    }
}
