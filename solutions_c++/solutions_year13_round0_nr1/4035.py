#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int t;
char p[4][5];
bool o,x,k;
inline void wczytaj()
{
    cin.ignore();
    for(int i =0;i<4;i++)
        cin.getline(p[i],5);
}
/*void wypisz()
{
    for(int i =0;i<16;i++)
    {

        if(!(i%4))
            cout << endl;
        cout << p[i/4][i%4];
    }
}*/
inline int ocen()
{
    k=false;
    o=false;
    x=false;
    for(int i=0;i<4;i++)
    {

        for(int j=0;j<4;j++)
        {
            if(p[i][j]=='.')
            {
                k=true;
                o=false;
                x=false;
                goto tutaj;
                //break;
            }
            else if(p[i][j]=='X')
            {
                x=true;
            }
            else if(p[i][j]=='O')
            {
                o=true;
            }
        }
        if(!(x||o))
            continue;
        else if(x&&o)
        {
            x=false;
            o=false;
        }
        else if(x)
            return 0;
        else
            return 1;
        tutaj:
        ;
    }

    o=false;
    x=false;
    for(int i=0;i<4;i++)
    {

        for(int j=0;j<4;j++)
        {
            if(p[j][i]=='.')
            {
                k=true;
                o=false;
                x=false;
                goto tutaj2;
                //break;
            }
            else if(p[j][i]=='X')
            {
                x=true;
            }
            else if(p[j][i]=='O')
            {
                o=true;
            }
        }
        if(!(x||o))
            continue;
        else if(x&&o)
        {
            x=false;
            o=false;
        }
        else if(x)
            return 0;
        else
            return 1;
        tutaj2:
        ;
    }
    o=false;
    x=false;
    for(int j=0;j<4;j++)
        {
            if(p[j][j]=='.')
            {
                k=true;
                o=false;
                x=false;
                goto tutaj3;
                //break;
            }
            else if(p[j][j]=='X')
            {
                x=true;
            }
            else if(p[j][j]=='O')
            {
                o=true;
            }
        }
        if(!(x||o))
            goto tutaj3;
        else if(x&&o)
        {
            x=false;
            o=false;
        }
        else if(x)
            return 0;
        else
            return 1;
        tutaj3:
        ;

    o=false;
    x=false;
    for(int j=0;j<4;j++)
        {
            if(p[j][3-j]=='.')
            {
                k=true;
                o=false;
                x=false;
                goto tutaj4;
                //break;
            }
            else if(p[j][3-j]=='X')
            {
                x=true;
            }
            else if(p[j][3-j]=='O')
            {
                o=true;
            }
        }
        if(!(x||o))
            goto tutaj4;
        else if(x&&o)
        {
            x=false;
            o=false;
        }
        else if(x)
            return 0;
        else
            return 1;
        tutaj4:
        ;

    if(!k)
        return 2;
    return 3;
}
inline void sprawdz(int t)
{
    int wynik=ocen();



    cout << "Case #" << t << ": ";
    switch(wynik)
    {
        case 0:
            cout << "X won\n";
            break;
        case 1:
            cout << "O won\n";
            break;
        case 2:
            cout << "Draw\n";
            break;
        case 3:
            cout << "Game has not completed\n";
            break;
    };
}
int main()
{

    cin >> t;
    for(int i =0;i<t;i++)
    {
       wczytaj();
       sprawdz(i+1);
    }
    return 0;
}
