#include <iostream>
#define REP(i,a,b) for(int i=a; i<b; i++)
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
    float T,N,K;

    fstream plikIn ("small.in", fstream::in | fstream::out);
    fstream plikOut ("small.out", fstream::in | fstream::out);

    plikIn >> T;

    REP(i,0,T)
    {
        plikIn >> N >> K;
        if(  (int(K+1)%int((pow(2.0,N)))==0) )
        plikOut << "Case #" << i+1 << ": ON" << endl;
        else
        plikOut << "Case #" << i+1 << ": OFF" << endl;
    }

    plikIn.close();
    plikOut.close();
    return 0;
}
