#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
int main()
{
    ofstream out;
    fstream in;
    in.open("switch.in");
    out.open("switch.out");
    long long mod;
    int K;
    in>>K;
    for(int i=0;i<K;i++)
    {
            mod=1;
            long long k,N;
            in>>N>>k;
            for(int j=0;j<N;j++)mod*=2;
            out<<"Case #"<<i+1<<": ";
            if(k%mod==mod-1)out<<"ON"<<endl;
            else out<<"OFF"<<endl;
    }
};
