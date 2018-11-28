#include <iostream>
#include <fstream>
using namespace std;

char tab[4][4];

bool check(int ti, int tj, char c)
{
    if (ti!=-1) //i don't check tj
        tab[ti][tj]=c;

    bool d1f=true, d2f=true;
    for (int i=0; i<4; ++i)
    {
        if (tab[i][i]!=c)
            d1f=false;
        if (tab[3-i][i]!=c)
            d2f=false;
    }
    if (d1f || d2f)
        return true;


    for (int i=0; i<4; ++i)
    {
        bool lf=true, cf=true;
        for (int j=0; j<4; ++j)
        {
            if (tab[i][j]!=c)
                lf=false;
            if (tab[j][i]!=c)
                cf=false;
        }
        if (lf || cf)
            return true;
    }
    return false;
}

bool isFull()
{
    for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
            if (tab[i][j]=='.')
                return false;
    return true;
}

int main()
{
    ifstream inp("A-large.in");
    ofstream outp("outp.out");
    ostream &outt=outp;

    int T;
    inp >> T;
    for (int t=1; t<=T; ++t)
    {
        int ti=-1, tj=-1;
        for (int i=0; i<4; ++i)
            for (int j=0; j<4; ++j)
            {
                inp >> tab[i][j];
                if (tab[i][j]=='T')
                {
                    ti=i;
                    tj=j;
                }
            }


        bool xw=check(ti, tj, 'X');
        bool ow=check(ti, tj, 'O');
        bool full=isFull();

        if (t>1) outt << endl;
        outt << "Case #" << t << ": ";

        if (xw)
            outt << "X won";
        else
        if (ow)
            outt << "O won";
        else
        if (full)
            outt << "Draw";
        else
            outt << "Game has not completed";
    }
}
