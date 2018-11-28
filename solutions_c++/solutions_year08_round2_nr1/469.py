#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

ifstream fin("in.in");
ofstream fout("out.out");
long long A,B,C,D,n,m,x0,y0,x,y,M;
long long T;
long long i,j,k,p;

int main() {
    fin >> T; 
    for (long long t=1;t<=T;t++) {
    vector<long long> X,Y;
    fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    X.push_back(x0); Y.push_back(y0);
    for (i=1;i<n;i++) {
        x0 = ( A * x0 + B ) % M;
        y0 = ( C * y0 + D ) % M;
        X.push_back(x0); Y.push_back(y0);
        }
    cout << "X[]: ";
    for (i=0;i<n;i++) cout << X[i] << " "; cout << endl;
    cout << "Y[]: ";
    for (i=0;i<n;i++) cout << Y[i] << " "; cout << endl;
    
    long long SOL(0);
    for (i=0;i<n;i++)
        for (j=i+1;j<n;j++)
            for (k=j+1;k<n;k++) {
                if ((X[i]+X[j]+X[k])%3==0 && (Y[i]+Y[j]+Y[k])%3==0) SOL++;
                }
    fout << "Case #" << t << ": " << SOL << endl;
    }
    system("pause");
}
