#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
int main()
{
    int t,T,N,K,count;
    fin>>T;
    for (t=1;t<=T;t++)
    {
        fout<<"Case #"<<t<<": ";
        fin>>N>>K;
        count=0;
        while (K%2==1)
        {
           count++;
           K/=2;
        }
        if (count>=N) fout<<"ON"<<endl;
        else fout<<"OFF"<<endl;
    }
    return 0;
}
