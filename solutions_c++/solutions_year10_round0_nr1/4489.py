#include <iostream>
#include <fstream>
#include <string>

using namespace std;
long long t=0;
bool ind[30];
long long shu[30];
int s;
long long tr(int m){
    if(ind[m]) return shu[m];
    ind[m]=true;
    shu[m]=tr(m-1)*2+1;
    return shu[m];
    }
int main(){
    for(int i=0;i!=30;i++) ind[i+1]=false;
    ind[1]=true;shu[1]=1;
    ifstream fin("A-small.in");
    ofstream fout("A-small.out");
    fin>>s;
    for(int i=0;i!=s;i++){
        int a;long long b;
        fin>>a>>b;
        t=tr(a);
        if(((b+1)%(t+1))==0) fout<<"Case #"<<i+1<<": ON"<<endl;
        else fout<<"Case #"<<i+1<<": OFF"<<endl;
        }
     }
