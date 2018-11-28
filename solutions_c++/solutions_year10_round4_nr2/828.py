#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("QB.in");
ofstream fout("QB.out");
long t,p,m[2000],ans;
long a[10][2000];
long x,y;

int main() {
    fin >> t;
    for (int i=0;i<t;i++) {
        fin >> p;
        x=1;
        for (int j=0;j<p;j++) {x*=2;}
        for (int j=0;j<x;j++) {fin >> m[j];}
        x/=2;
        for (int j=0;j<p;j++) {
            for (int k=0;k<x;k++) {
                fin >> a[j][k];
            }
            x/=2;
        }
        x=1;y=1;
        for (int j=0;j<p;j++) {x*=2;}
        ans=0;
        for (int j=0;j<p;j++) {
            for (int k=0;k<y;k++) {
                bool flag=false;
                for (int ii=0;ii<x;ii++) {
                    //fout << k << " " <<  x << " " << ii << " " << m[k*x+ii] << endl;
                    if (m[k*x+ii]<p) {flag=true;}
                }
                if (flag) {
                       for (int ii=0;ii<x;ii++) {m[k*x+ii]++;}
                       ans++;    
                }
            }
            x/=2;
            y*=2;
        }        
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
