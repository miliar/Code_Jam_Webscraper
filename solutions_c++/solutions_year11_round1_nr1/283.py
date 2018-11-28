#include <iostream>
#include <cmath>
using namespace std;

long long n, pd, pg;
long long d, wd, g, wg;
bool isSolve;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout<<"Case #"<<i<<": ";
        cin >> n >> pd >> pg;
        if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0)) {
            cout << "Broken" << endl;
            continue;
        }
        isSolve = false;
        if(n > 100) n = 100;
        for(int d = 1; d <= n; d++){
            if(pd * d % 100 == 0) isSolve = true;
        }
        if (!isSolve) cout << "Broken" << endl;
        else cout << "Possible" << endl;
    }
    return 0;
}
