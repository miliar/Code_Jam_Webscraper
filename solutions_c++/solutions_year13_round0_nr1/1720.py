#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
using namespace std;

char Mat[10][10];
int TestCase, T, NrX, NrO, NrT;

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int i, j, k;
    scanf("%i\n", &T);
    for(TestCase = 1; TestCase <= T; ++ TestCase)
    {
        printf("Case #%i: ", TestCase);
        bool WinX = 0, WinO = 0, Draw = 0, NotCompleted = 0;
        for(i = 1; i <= 4; ++ i)
            gets(Mat[i] + 1);
        for(i = 1; i <= 4; ++ i)
        {
            NrX = NrO = NrT = 0;
            for(j = 1; j <= 4; ++ j)
            {
                NrX += Mat[i][j] == 'X';
                NrO += Mat[i][j] == 'O';
                NrT += Mat[i][j] == 'T';
            }
            if(NrX == 4 || (NrX == 3 && NrT == 1)) WinX = 1;
            if(NrO == 4 || (NrO == 3 && NrT == 1)) WinO = 1;

            NrX = NrO = NrT = 0;
            for(j = 1; j <= 4; ++ j)
            {
                NrX += Mat[j][i] == 'X';
                NrO += Mat[j][i] == 'O';
                NrT += Mat[j][i] == 'T';
            }
            if(NrX == 4 || (NrX == 3 && NrT == 1)) WinX = 1;
            if(NrO == 4 || (NrO == 3 && NrT == 1)) WinO = 1;
        }

        NrX = NrO = NrT = 0;
        for(i = 1; i <= 4; ++ i)
        {
            NrX += Mat[i][i] == 'X';
            NrO += Mat[i][i] == 'O';
            NrT += Mat[i][i] == 'T';
        }
        if(NrX == 4 || (NrX == 3 && NrT == 1)) WinX = 1;
        if(NrO == 4 || (NrO == 3 && NrT == 1)) WinO = 1;

        NrX = NrO = NrT = 0;
        for(i = 1; i <= 4; ++ i)
        {
            NrX += Mat[i][4 - i + 1] == 'X';
            NrO += Mat[i][4 - i + 1] == 'O';
            NrT += Mat[i][4 - i + 1] == 'T';
        }
        if(NrX == 4 || (NrX == 3 && NrT == 1)) WinX = 1;
        if(NrO == 4 || (NrO == 3 && NrT == 1)) WinO = 1;

        if(!WinX && !WinO)
        {
            NotCompleted = 0;
            for(i = 1; i <= 4; ++ i)
                for(j = 1; j <= 4; ++ j)
                    if(Mat[i][j] == '.')
                        NotCompleted = 1;
            if(!NotCompleted) Draw = 1;
        }
        if(WinX) printf("X won\n");
        if(WinO) printf("O won\n");
        if(Draw) printf("Draw\n");
        if(NotCompleted) printf("Game has not completed\n");
        gets(Mat[0]);
    }
    return 0;
}
