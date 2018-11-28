#include <iostream>
#include <string>
#include <stack>
#include <cstdlib>
#include <cstdio>

using namespace std;

int TEST_CASES;

char scacchiera[20][20];

void stampa_scacchiera()
{
    for (int i = 0; i < 4; i++)
            printf("%s\n",scacchiera[i]);

}
int controlla_scacchiera()
{
    int cont = 0;
    for (int i = 0; i < 4; i++)
    {
        cont = 0;
        for (int j = 0; j < 4; j++)
            if (scacchiera[i][j] == 'O' || scacchiera[i][j] == 'T')
                cont++;
        if (cont == 4)
            return 1;
    }
    cont = 0;
    for (int i = 0; i < 4; i++)
    {
        cont = 0;
        for (int j = 0; j < 4; j++)
            if (scacchiera[j][i] == 'O' || scacchiera[j][i] == 'T')
                cont++;
    if (cont == 4)
        return 1;
    }

    cont = 0;
    for (int i = 0; i < 4; i++)
        if (scacchiera[i][i] == 'O' || scacchiera[i][i] == 'T')
                cont++;
    if (cont == 4)
        return 1;
    cont = 0;
    for (int i = 0; i < 4; i++)
        if (scacchiera[4-i-1][i] == 'O' || scacchiera[4-i-1][i] == 'T')
                cont++;
    if (cont == 4)
        return 1;

    cont = 0;
    for (int i = 0; i < 4; i++)
    {
        cont = 0;
            for (int j = 0; j < 4; j++)
            if (scacchiera[i][j] == 'X' || scacchiera[i][j] == 'T')
                cont++;
    if (cont == 4)
        return 2;
    }

    cont = 0;
    for (int i = 0; i < 4; i++)
    {
        cont = 0;
            for (int j = 0; j < 4; j++)
            if (scacchiera[j][i] == 'X' || scacchiera[j][i] == 'T')
                cont++;
    if (cont == 4)
        return 2;
    }

    cont = 0;
    for (int i = 0; i < 4; i++)
        if (scacchiera[i][i] == 'X' || scacchiera[i][i] == 'T')
                cont++;
    if (cont == 4)
        return 2;
    cont = 0;
    for (int i = 0; i < 4; i++)
        if (scacchiera[4-i-1][i] == 'X' || scacchiera[4-i-1][i] == 'T')
                cont++;
    if (cont == 4)
        return 2;


    cont = 0;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (scacchiera[j][i] == '.')
                cont++;
    if (cont != 0)
        return 0; //Non finito
    return 3; //pareggio

}

int main()
{
    scanf("%d",&TEST_CASES);
    for (int c = 0; c < TEST_CASES; c++)
    {
        char temp[10];
        for (int i = 0; i < 4; i++)
            scanf("%s",scacchiera[i]);
        //scanf("%s",temp);
        //stampa_scacchiera();
        int ris = controlla_scacchiera();
        if (ris == 1)
            cout << "Case #" << c+1 << ": " << "O won" << endl;
        if (ris == 2)
            cout << "Case #" << c+1 << ": " << "X won" << endl;
        if (ris == 0)
            cout << "Case #" << c+1 << ": " << "Game has not completed" << endl;
        if (ris == 3)
            cout << "Case #" << c+1 << ": " << "Draw" << endl;

    }
    return 0;
}
