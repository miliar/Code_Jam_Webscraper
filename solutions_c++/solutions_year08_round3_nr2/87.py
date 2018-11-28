#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T, x[30], N, rez;
string str;

ifstream fin("ugly.in");
ofstream fout("ugly.out");

void calc()
{
    long long nr , sum = 0, prod = 1;

    nr = str[str.length()-1] - '0';

    for ( int i = N-1; i>=0; i--)
    {
        if ( x[i] == 1 )
        {
            prod *= 10;
            nr = nr  + prod*( str[i]  -'0');
        }
        else
        {
            if ( x[i] == 2 )
                sum+= nr;
            else
                sum-=nr;
            nr = str[i] -'0';
            prod=1;
        }
    }
    sum+=nr;
    if ( sum % 2 == 0 || sum % 3 == 0 || sum % 5 == 0 || sum % 7 == 0)
        rez++;
}

void back ( int k )
{
    if ( k == N )
        calc();
    else
    {
        for (int i = 1; i<=3; i++)
        {
            x[k] = i;
            back(k+1);
        }
    }
}

int main()
{
    fin>>T;
    for (int z=1; z<=T; z++)
    {
        rez= 0;
        fin>>str;
        N = str.length()-1;
        back(0);
        fout<<"Case #"<<z<<": "<<rez<<"\n";

    }

    return 0;

}
