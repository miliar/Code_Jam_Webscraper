#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int cases;
    fin>>cases;
    for (int c=1;c<=cases;c++){
        int n,k;
        fin>>n>>k;
        int aux=2;
        for (int i=0;i<n-1;i++) aux*=2;
        fout<<"Case #"<<c<<": ";
        if (k%aux==aux-1||n==0) fout<<"ON"<<endl;
        else fout<<"OFF"<<endl;
    }
}
