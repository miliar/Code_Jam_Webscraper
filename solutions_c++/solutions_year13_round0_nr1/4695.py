#include <iostream>
#include <cstdio>

using namespace std;

char boa[4][5];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i, j, T, cas = 1;
    cin>>T;
    while(T--)
    {
        for(i = 0; i < 4; i++)
            cin>>boa[i];
        int pX = 0, pO = 0, E = 0;
        int X, O, T;
        for(i = 0; i < 4; i++)
        {
            X = 0, O = 0, T = 0;
            for(j = 0; j < 4; j++)
                switch(boa[i][j])
                {
                case 'X' :
                    X++;
                    break;
                case 'O' :
                    O++;
                    break;
                case 'T' :
                    T++;
                    break;
                case '.' :
                    E++;
                    break;
                }
            if(X + T == 4)
                pX++;
            if(O + T == 4)
                pO++;
        }
        for(i = 0; i < 4; i++)
        {
            X = 0, O = 0, T = 0;
            for(j = 0; j < 4; j++)
                switch(boa[j][i])
                {
                case 'X' :
                    X++;
                    break;
                case 'O' :
                    O++;
                    break;
                case 'T' :
                    T++;
                    break;
                case '.' :
                    E++;
                    break;
                }
            if(X + T == 4)
                pX++;
            if(O + T == 4)
                pO++;
        }
        X = 0, O = 0, T = 0;
        for(i = 0; i < 4; i++)
            switch(boa[i][i])
            {
            case 'X' :
                X++;
                break;
            case 'O' :
                O++;
                break;
            case 'T' :
                T++;
                break;
            case '.' :
                E++;
                break;
            }
        if(X + T == 4)
            pX++;
        if(O + T == 4)
            pO++;
        X = 0, O = 0, T = 0;
        for(i = 0; i < 4; i++)
            switch(boa[i][3 - i])
            {
            case 'X' :
                X++;
                break;
            case 'O' :
                O++;
                break;
            case 'T' :
                T++;
                break;
            case '.' :
                E++;
                break;
            }
        if(X + T == 4)
            pX++;
        if(O + T == 4)
            pO++;
        cout<<"Case #"<<cas++<<": ";
        if(pO > pX)
            cout<<"O won\n";
        else if(pO < pX)
            cout<<"X won\n";
        else if(E != 0)
            cout<<"Game has not completed\n";
        else
            cout<<"Draw\n";
    }
}
