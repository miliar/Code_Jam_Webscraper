#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
const int MAXN=800;
long long s(0);
int x[MAXN],y[MAXN];
int i,j,k,ii,t,n;
int main(){
    ifstream fin("A-small.in");
    ofstream fout("A-small.out");
    fin>>t;
    for(ii=1;ii<=t;ii++){
        fin>>n;
        s=0;
        for(i=0;i<n;i++) fin>>x[i];
        for(i=0;i<n;i++) fin>>y[i];
        sort(x,x+n);
        sort(y,y+n);
        for(i=0;i<n;i++)
            s+=x[i]*y[n-1-i];
        fout<<"Case #"<<ii<<": "<<s<<endl;
    }
}        
