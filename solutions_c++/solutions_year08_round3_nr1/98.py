#include <iostream>
#include <fstream>

using namespace std;

#define MAX 1500

int frecv[MAX], P, K, L, poz[MAX];

ifstream fin("letter.in");
ofstream fout("letter.out");

int main()
{
    int T;
    fin>>T;
    for (int z= 1; z<=T; z++)
    {
        fin>>P>>K>>L;
        for (int i =0; i<L; i++)
            fin>>frecv[i];

        sort(frecv, frecv+L);
        reverse(frecv, frecv+L);
        int p = 0;
        for ( int i=0; i<L; i++)
        {
            if ( i % K == 0 )
                p++;
            poz[i] = p;
        }

        long long rez = 0;
        for (int i = 0; i<L; i++)
        {
            rez += (long long) frecv[i] * poz[i];
        }
        fout<<"Case #"<<z<<": "<<rez<<"\n";
    }

    return 0;

}
