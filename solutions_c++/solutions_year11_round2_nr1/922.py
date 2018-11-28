#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;
#define REP(i,n) for (int i=0;i<int(n);++i)
int main() {
    cout.setf(ios::fixed);
    cout.precision(9);
    int ncas; cin >>ncas;
    for(int cas=1;cas<=ncas;++cas) {
        int n; cin >> n;
        vector<string> v(n);
        REP(i,n) cin >> v[i];
        vector<double> wp(n,0),owp(n,0),oowp(n,0);
        REP(i,n) {
            int a=0,b=0;
            REP(j,n) {
                if (v[i][j]=='0' or v[i][j]=='1') ++b;
                if (v[i][j]=='1') ++a;
            }
//            cerr << "wp " << i << " : " << a << " " << b << endl;
            wp[i]=double(a)/b;
        }
        
        REP(i,n) {
            vector<double> wpx(n,-1);
            REP(j,n) if (v[i][j]=='0' or v[i][j]=='1') { //si he jugat contra akest equip:
                int a=0,b=0;
                REP(k,n) if (k!=i) {
                    if (v[j][k]=='0' or v[j][k]=='1') ++b;
                    if (v[j][k]=='1') ++a;
                }
                wpx[j]=double(a)/b;
            }
            int r=0;
            double s=0;
            REP(j,n) if (wpx[j]>-1) {
                s+=wpx[j];
                ++r;
            }
            owp[i] = s/=double(r);
        }
        
        REP(i,n) {
            int r=0;
            double s=0;
            REP(j,n) if (v[i][j]=='0' or v[i][j]=='1') {
                s+=owp[j];
                ++r;
            }
            oowp[i]=s/double(r);
        }
        
        cout << "Case #" << cas << ":" << endl;
        REP(i,n) cout << double(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]) << endl;
    }
}
