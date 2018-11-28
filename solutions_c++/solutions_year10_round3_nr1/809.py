#include <iostream>
#include <fstream>
using namespace std;
#define FOR(i, a, b) for(int i=int(a); i<=int(b); ++i)
#define FORD(i, a, b) for(int i=int(a); i>=int(b); ++i)
int main() {
    freopen("A.in2", "r", stdin);
    freopen("A.ou2", "w", stdout);
    int t;
    cin >> t;
    FOR(test, 1, t) {
        int res = 0;
        int n, a[1001], b[1001];
        cin >> n;
        FOR(i, 1, n) cin >> a[i] >> b[i];
        FOR(i, 1, n-1) FOR(j, i+1, n)
            if ((a[i] < a[j] && b[i] > b[j]) || ((a[i] > a[j] && b[i] < b[j]))) res++;
        cout << "Case #" << test <<": " << res << endl;
    }
}
