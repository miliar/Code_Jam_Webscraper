#include<iostream>
#include<fstream>

using namespace std;
long t,n,k,x,y,z;
ifstream fin("A.in");
ofstream fout("A.out");

int main() {
    fin >> t;
    for (int i=0;i<t;i++) {
        fin >> n >> k;
        x=1;
        for (int j=0;j<n;j++) {
            x*=2;
        }
        k=k%x;
        x--;
        if (x==0) {x=1;}
        fout << "Case #" <<  i+1 << ": ";
        if (k==x) {fout << "ON" << endl;}
        else {fout << "OFF" << endl;}
    }
    return 0;
}
