#include <fstream>
#include <iostream>
#include <string>

#define INF 0x3f3f3f3f

using namespace std;

string sir[150];
int query[1000], a[1001][101];
int N,S,Q;
ifstream fin ("univ.in");
ofstream fout("univ.out");

int strtoint(  string s )
{
    for ( int i = 0; i<S; i++)
        if ( s == sir[i] )
            return i;
}

void calc()
{
    for (int i = 0; i<S; i++)
        if ( i != query[0] )
            a[0][i] = 0;
        else
            a[0][i] = INF;

    for ( int i = 1; i<Q; i++)
    {
        int min = INF;
        for ( int k = 0; k<S; k++)
                if ( a[i-1][k] + 1 < min )
                    min = a[i-1][k] + 1;

        for ( int j = 0; j < S; j++)
        {
            if ( query[i] == j )
            {
                a[i][j] = INF;
                continue;
            }
            if ( a[i-1][j] < min )
                a[i][j] = a[i-1][j];
            else
                a[i][j] = min;
        }
    }
}

void afis_mat()
{
    for (int i = 0; i<Q; i++)
    {
        for (int j = 0; j<S; j++)
            cout<<a[i][j]<<"     ";
        cout<<"\n";
    }
}

int main()
{
    fin>>N;
    for (int z = 1 ; z<=N; z++)
    {
        fin>>S;
        getline(fin, sir[0]);
        for ( int i = 0; i<S; i++)
            getline(fin, sir[i]);
        fin>>Q;
        string aux;
        getline(fin,aux);
        for ( int i = 0; i<Q; i++)
        {
            getline(fin,aux);
            query[i] = strtoint(aux);
        }
        calc();
        //afis_mat();
        int rez = INF;
        for (int i = 0; i<S; i++)
            if ( a[Q-1][i] < rez )
                rez = a[Q-1][i];
        fout<<"Case #"<<z<<": "<<rez<<"\n";
    }

    return 0;

}
