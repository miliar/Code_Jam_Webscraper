#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("Mage.out");
    long n,k,t,j;
    fin>>t;
    unsigned long a[31];
    a[0]=1;
    for(int i=1;i<=30;i++){
        a[i]=a[i-1]*2;
    }
    unsigned long b[31];
    b[1]=1;
    for(int i=2;i<=30;i++){
        b[i]=b[i-1]+a[i-1];
    }
    for(int i=0;i<t;i++){
        fin>>n>>k;
        fout<<"Case #"<<i+1<<": ";
        if(k<b[n]){fout<<"OFF"<<endl;}
        else{
            if(k%(b[n]+1)==b[n]){fout<<"ON"<<endl;}
            else {fout<<"OFF"<<endl;}
        }
    }
}
