#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;
#define xin fin
#define xout fout
#define f(z,a,b) for (z=a;z<=b;z++)

int main(int argc, char *argv[])
{
    int t,n,k;
    register int z;
    ifstream fin("a.in");
    ofstream fout("a.out");
    xin >> t;
    f(z,1,t)
    {
        xin >> n >> k;
        xout << "Case #" << z << ": ";
        if ((k+1) % (1 << n) == 0)
        {
            xout << "ON" << endl;
        }
        else
        {
            xout << "OFF" << endl;
        }
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
