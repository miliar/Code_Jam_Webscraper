#include <iostream>
#include <fstream>
#include <cassert>

using namespace std;

int main()
{
    int Tlines;

    unsigned int Nsnappers,Ksnaps;
    ifstream fin("in");
    ofstream fout("out");
    fin>>Tlines;
    for(int t=1;t<=Tlines;++t)
    {
        fin>>Nsnappers>>Ksnaps;
        assert(!fin.fail());
        assert(Nsnappers>0);

        assert(Nsnappers<31);
        unsigned int mask=(1<<Nsnappers)-1;
        fout<<"Case #"<<t<<": ";
        if ((Ksnaps & mask)==mask)
            fout<<"ON\n";
        else
            fout<<"OFF\n";
    }
    return 0;
}
