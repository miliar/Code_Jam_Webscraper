#include<iostream>
#include<fstream>
using namespace std;

unsigned long pow2(int n)
{
    return 1<<n;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A.out");
    
    int t;
    int n;
    unsigned long k;
    fin>>t;
    
    for(int i=1;i<=t;i++)
    {
         fin>>n;
         fin>>k;
         fout<<"Case #"<<i<<": ";
         if((k+1)%pow2(n)==0)
             fout<<"ON"<<endl;
         else
             fout<<"OFF"<<endl;
    }
}
