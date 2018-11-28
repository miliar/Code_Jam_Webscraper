#include<iostream>
#include<fstream>

using namespace std;
ifstream fin("QB.in");
ofstream fout("QB.out");
long long l,p,c;
long t,x,y,z,a,b,ans,counter;

int main() {
    fin >> t;
    for (int i=0;i<t;i++) {
        fin >> l >> p >> c;
        counter=0;
        while (l<p) {
              l*=c;
              counter++;
        }
        x=1;
        ans=0;
        while (x<counter) {
              x*=2;
              ans++;
        }
        fout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
