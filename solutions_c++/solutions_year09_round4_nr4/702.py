#include <iostream>
#include <vector>
#include <cmath>
#define x first
#define y second
using namespace std;
typedef pair<int,int> PII;

double dist(PII a, PII b) {
    double x=a.x-b.x;
    double y=a.y-b.y;
    return sqrt(x*x+y*y);
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(7);
    int t; cin >> t;
    for (int z=1;z<=t;++z) {
        int n; cin >> n;
        vector<PII> v(n);
        vector<int> r(n);
        for (int i=0;i<n;++i) cin >> v[i].x >> v[i].y >> r[i];
        cout << "Case #"<<z<<": ";
        if (n==1) cout << double(r[0]) << endl;
        else if (n==2) cout << double(max(r[0],r[1])) << endl;
        else {
            double ans=1e10;
            ans=min(ans, dist(v[0],v[1])+r[0]+r[1]);
            ans=min(ans, dist(v[0],v[2])+r[0]+r[2]);
            ans=min(ans, dist(v[2],v[1])+r[2]+r[1]);
            cout << ans/2. << endl;
        }
    }
}
