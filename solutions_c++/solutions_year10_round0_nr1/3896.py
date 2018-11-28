#include <iostream>
#include <fstream>
using namespace std;
long long t=0;

long long s;
long long tr(int m){
     if(m==1) return 1;
    long long f=tr(m-1)*2+1;
    return f;
    }
int main(){
     ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin>>s;
    for(long long i=0;i!=s;i++){
        int a;long long b;
        fin>>a>>b;
        t=tr(a);
        if(((b+1)%(t+1))==0) fout<<"Case #"<<i+1<<": ON"<<endl;
        else fout<<"Case #"<<i+1<<": OFF"<<endl;
        }
     }
