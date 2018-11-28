#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    int n,noc,p,i=1;
    long long k;

    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin>>noc;
    while(i<=noc)
    {
        fin>>n>>k;
        p=(long long)pow(2,n)-1;
        if(k%(p+1)==p)
        fout<<"Case #"<<i<<": ON"<<endl;
        else
        fout<<"Case #"<<i<<": OFF"<<endl;
        i++;
    }

}
