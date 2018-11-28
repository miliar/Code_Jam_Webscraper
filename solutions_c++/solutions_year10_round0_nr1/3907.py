#include <iostream>
#include <stdio.h>
#include <fstream>
#include <cmath>
using namespace std;
int main()
{
    int T,N,K,temp;
    ifstream fin("Alarge.in");
    ofstream fout("Aans.in");
    fin>>T;
    for (int i=1;i<=T;i++)
    {
          fin>>N>>K;
          temp=pow(2,N);
          if (K%temp == temp-1) fout<<"Case #"<<i<<": ON"<<endl;
          else fout<<"Case #"<<i<<": OFF"<<endl;
    }
    return 0;
}
