#include <iostream>
#include<fstream>

using namespace std;

ifstream fin("a+.in");
ofstream fout("a+.out");

long int v[31],n,k,t;

struct vektor{
    long int n[10001],k[10001];
} test;

int construct()
{
    v[1]=2;
    for(int i=2;i<=n;i++)
    {
        v[i]=v[i-1]+v[i-1];
    }
    return 0;
}

int main()
{
    fin>>t;
    n=0;
    for(int j=1;j<=t;j++)
    {
        fin>>test.n[j]>>test.k[j];
        test.k[j]++;
        if(test.n[j]>n) n=test.n[j];
    }
    construct();
    for(int j=1;j<=t;j++)
    {
        fout<<"Case #"<<j<<": ";
        if(test.k[j]%v[test.n[j]]==0)
            fout<<"ON"<<"\n";
        else fout<<"OFF"<<"\n";
    }
    return 0;
}
