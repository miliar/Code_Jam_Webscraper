#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <set>
#include <map>



#define for0(i,n) for (int i = 0; i < n; i++)
#define for1(i,n) for (int i = 1; i <= n; i++)
#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

int gcd (int a, int b) {
	return b ? gcd (b, a % b) : a;
}

int main () {
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    
    int c;
    cin >> c;
    for (int k = 0; k < c; ++k) {
        int n;
        cin >> n;
        vector <int64> t(n);
        for (int i = 0; i < n; ++i)
            cin >> t[i];
        sort (all(t));
        vector <int64> a(n-1);
        for (int i = 0; i < n-1; ++i)
             a[i] = t[i+1] - t[i];
        int64 res = a[0];
        for (int i = 1; i < n-1; ++i)
            if (a[i] != 0)
               res = gcd (res, a[i]);
        if (t[0] % res == 0) cout << "Case #" << k + 1 << ": " << 0 << endl;
        else cout << "Case #" << k + 1 << ": " << res - (t[0] % res) << endl;
    }
    return 0;
}
