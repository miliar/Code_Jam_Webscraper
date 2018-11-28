#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

char mat[4][4];

int main()
{
    int T ,out=1;
    bool end;
    char winner;
    //freopen("c:\\codejam\\A-small-attempt1.in","r",stdin);
    //freopen("c:\\codejam\\A-small-attempt1.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",out++);
        winner = 'D';
        end = true;
        for(int i=0;i<4;i++)
            scanf("%s",mat[i]);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(mat[i][j] == '.') end = false;
        for(int s=0;s<4;s++)
        {
            int yes = true ;
            for(int i=0;i<4;i++)
                if(mat[s][i] != 'X' && mat[s][i]!= 'T') yes = false;
            if(yes) winner = 'X';

            yes = true ;
            for(int i=0;i<4;i++)
                if(mat[s][i] != 'O' && mat[s][i]!= 'T') yes = false;
            if(yes) winner = 'O';
        }
        for(int s=0;s<4;s++)
        {
            int yes = true ;
            for(int i=0;i<4;i++)
                if(mat[i][s] != 'X' && mat[i][s]!= 'T') yes = false;
            if(yes) winner = 'X';

            yes = true ;
            for(int i=0;i<4;i++)
                if(mat[i][s] != 'O' && mat[i][s]!= 'T') yes = false;
            if(yes) winner = 'O';
        }

        bool yes = true ;
        for(int i=0;i<4;i++)
            if(mat[i][i] != 'X' &&mat[i][i] !='T')
                yes=false;
        if(yes) winner = 'X';

        yes = true ;
        for(int i=0;i<4;i++)
            if(mat[i][i] != 'O' &&mat[i][i] !='T')
                yes=false;
        if(yes) winner = 'O';

        yes = true ;
        for(int i=0;i<4;i++)
            if(mat[i][4-i] != 'X' &&mat[i][i] !='T')
                yes=false;
        if(yes) winner = 'X';

        yes = true ;
        for(int i=0;i<4;i++)
            if(mat[i][3-i] != 'O' &&mat[i][i] !='T')
                yes=false;
        if(yes) winner = 'O';

        if(winner == 'D')
        {
            if(end==true) puts("Draw");
            else puts("Game has not completed");
        }
        else
        {
            printf("%c won\n",winner);
        }
    }
    return 0;
}
