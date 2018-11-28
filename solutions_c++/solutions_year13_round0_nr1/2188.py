//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int t;
char tab[5][5];

int main()
{
    scanf("%d", &t);

    for(int ti = 1;ti <= t;ti++)
    {
        printf("Case #%d: ", ti);

        int wyn = 0, tmp = 3;
        bool puste = false;

        for(int i = 1;i <= 4;i++)
            for(int j = 1;j <= 4;j++)
            {
                scanf(" %c", &tab[i][j]);
                if(tab[i][j] == '.')
                {
                    tab[i][j] = 0;      // 00
                    puste = true;
                }
                else if(tab[i][j] == 'T') tab[i][j] = 3; // 11
                else if(tab[i][j] == 'X') tab[i][j] = 1; // 01
                else if(tab[i][j] == 'O') tab[i][j] = 2; // 10
            }

        for(int i = 1;i <= 4;i++)
        {
            tmp = 3;
            for(int j = 1;j <= 4;j++) tmp &= tab[i][j];
            if(tmp) wyn = tmp;
        }

        for(int i = 1;i <= 4;i++)
        {
            tmp = 3;
            for(int j = 1;j <= 4;j++) tmp &= tab[j][i];
            if(tmp) wyn = tmp;
        }

        tmp = 3;
        for(int i = 1;i <= 4;i++) tmp &= tab[i][i];
        if(tmp) wyn = tmp;

        tmp = 3;
        for(int i = 1;i <= 4;i++) tmp &= tab[i][4-i+1];
        if(tmp) wyn = tmp;


        if(!wyn && !puste) wyn = 123;

        if(wyn == 0) printf("Game has not completed\n");
        else if(wyn == 123) printf("Draw\n");
        else if(wyn == 1) printf("X won\n");
        else if(wyn == 2) printf("O won\n");
    }
    return 0;
}
