#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int abs(int x)
{
    if (x>=0)
        return x;
    else
        return 0-x;
}

int main()
{
    int P, i, x, o, b, t, T, tb, to, N, CASE;
    char L;

fin >> N;
for (CASE=1; CASE <= N; CASE++)
{

    fin >> P;
    o=1; b=1; t=0; T=0; tb=0; to=0;
    for (i=1; i<=P; i++)
    {
        t=0;
        fin >> L >> x;
        if (L=='B')
        {
            t=abs(b-x)+1-tb;
            tb=0; b=x;
            if (t>0)
                to+=t;
            else
                to+=1;
        }
        else if (L=='O')
        {
            t=abs(o-x)+1-to;
            to=0; o=x;
            if (t>0)
                tb+=t;
            else
                tb+=1;
        }
        if (t>=1)
            T+=t;
        else
            T+=1;
    }

    fout << "Case #" << CASE << ": " << T << endl;

}
    return 0;
}
