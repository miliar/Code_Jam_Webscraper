#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("QA.in");
ofstream fout("QA.out");
long t,n,ans;
long a[2][2000];

int main() {
    fin >> n;
    for (int i=0;i<n;i++) {
        fin >> t;
        for (int j=0;j<t;j++) {
            fin >> a[0][j] >> a[1][j];
        }
        ans=0;
        for (int j=0;j<t;j++) {
            for (int k=j+1;k<t;k++) {
                if ((a[0][j]-a[0][k])*(a[1][j]-a[1][k])<0) {ans++;}
            }
        }
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
