#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>
#include <queue>
#include <fstream>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, a, b) for (int i = (int)(b); i >= (int)(a); i--)
#define tr(i, a) for (typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair
#define N 1200
typedef long long ll;
int a[N], n;
int solve(){
    int x = 0, s = 0;
    forn(i, n){
        x ^= a[i];
        s += a[i];
    }
    if(x != 0)
        return 0;
    return s - *min_element(a, a + n);
}

int main() {
    int T;
    cin >> T;
    forn(_t, T){
        cin >> n;
        forn(i, n)
            cin >> a[i];
        cout << "Case #" << _t + 1 << ": ";
        int res = solve();
        if(res == 0)
            cout << "NO";
        else
            cout << res;
        cout << endl;
    }
    return 0;
}
