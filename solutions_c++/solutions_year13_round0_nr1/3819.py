#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int testy,x,mxx,mxo,o;
char t[10][10];
bool kr;

void X ()
{
    mxx = 0;
    for (int i=1; i<=4; i++)
    {
        x = 0;
        for (int j=1; j<=4; j++)
            if (t[i][j] == 'X' || t[i][j] == 'T')
                x ++;
        mxx = max (mxx, x);
    }
    
    for (int i=1; i<=4; i++)
    {
        x = 0;
        for (int j=1; j<=4; j++)
            if (t[j][i] == 'X' || t[j][i] == 'T')
                x ++;
        mxx = max (mxx, x);
    }
    
    x = 0;
    int j = 1;
    for (int i=1; i<=4; i++)
    {
        if (t[i][j] == 'X' || t[i][j] == 'T')
            x ++;
        j ++;
        mxx = max (mxx, x);
    }
    
    x = 0;
    j = 4;
    for (int i=1; i<=4; i++)
    {
        if (t[i][j] == 'X' || t[i][j] == 'T')
            x ++;
        j --;
        mxx = max (mxx, x);
    }
}

void O ()
{
    mxo = 0;
    for (int i=1; i<=4; i++)
    {
        o = 0;
        for (int j=1; j<=4; j++)
            if (t[i][j] == 'O' || t[i][j] == 'T')
                o ++;
        mxo = max (mxo, o);
    }
    
    for (int i=1; i<=4; i++)
    {
        o = 0;
        for (int j=1; j<=4; j++)
            if (t[j][i] == 'O' || t[j][i] == 'T')
                o ++;
        mxo = max (mxo, o);
    }
    
    o = 0;
    int j = 1;
    for (int i=1; i<=4; i++)
    {
        if (t[i][j] == 'O' || t[i][j] == 'T')
            o ++;
        j ++;
        mxo = max (mxo, o);
    }
    
    o = 0;
    j = 4;
    for (int i=1; i<=4; i++)
    {
        if (t[i][j] == 'O' || t[i][j] == 'T')
            o ++;
        j --;
        mxo = max (mxo, o);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin >> testy;
    
    for (int k=1; k<=testy; k++)
    {
        kr = false;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
            {
                cin >> t[i][j];
                if (t[i][j] == '.')
                    kr = true;
            }
        
        X ();
        O ();
        
        if ((mxx == mxo && mxx == 4) || (kr == false && mxx != 4 && mxo != 4))
            cout <<  "Case #" << k << ": Draw\n";

        if (mxx == 4 && mxo != 4)
            cout <<  "Case #" << k << ": X won\n";
        
        if (mxo == 4 && mxx != 4)
            cout <<  "Case #" << k << ": O won\n";
            
        if (mxx != 4 && mxo != 4 && kr == true)
            cout <<  "Case #" << k << ": Game has not completed\n";
    }

cin.ignore(2);
return 0;
}
            
