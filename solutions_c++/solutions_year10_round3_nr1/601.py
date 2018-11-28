#include <iostream>
#include <vector>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for (int i = a; i < b; i++)

int main() {
    int t, n;
    long long int ans = 0;
    vector<int> a, b;

    cin >> t;
    REP(z,t) {
        cin >> n;
        a.clear(); b.clear(); a.resize(n); b.resize(n);
        REP(i,n) cin >> a[i] >> b[i];

        ans = 0;
        REP(i,n) {
            FOR(j,i+1,n) {
                if ( (a[i] < a[j] && b[i] > b[j]) || (a[i] > a[j] && b[i] < b[j]) )
                    ans++;
            }
        }

        cout << "Case #" << z+1 << ": " << ans << endl;
    }

    return 0;
}
