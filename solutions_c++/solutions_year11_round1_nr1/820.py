#include <stdio.h>
#include <fstream>
using namespace std;

int GCD (int a , int b)
{
    if (b == 0) return a;
    return GCD (b , a%b);
}

int main ()
{
    ifstream fin ("A.in");
    ofstream fout ("A.out");

    int t;

    fin >> t;

    for (int ID=1; ID<=t; ID++)
    {
        long long n;
        int pD,pG;

        fin >> n >> pD >> pG;

        int nD,aD,nG,aG;
        int f = GCD (pD , 100);
        int s = GCD (pG , 100);

        nD = pD / f;
        aD = 100 / f;
        nG = pG / s;
        aG = 100 / s;

        fout << "Case #" << ID << ": ";

        if ((long long)aD > n || (pD != 100 && pG == 100) || (pD != 0 && pG == 0) || (pD == 0 && pG != 0))
            fout << "Broken\n";
        else
            fout << "Possible\n";
    }
}
