#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream is("in");
    ofstream os("out");
    int ncase;
    is>>ncase;
    for (int c=0;c<ncase;c++) {
        long long L,P,C;
        is>>L>>P>>C;
        long long count = 0;
        while(1) {
            L*=C;
            if(L>=P)break;
            count++;
        }
        long long res = 0;
        if (count == 0)res = 0;
        else res = (long long)(log2(count))+1;
        os<<"Case #"<<c+1<<": "<<res<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
