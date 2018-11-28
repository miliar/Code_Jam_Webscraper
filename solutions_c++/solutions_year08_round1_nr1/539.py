#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

long long t, n, i, co, it = 0;
vector<long long> a, b;

int main () {
    scanf ("%lld", &t);
    while(it < t) {
        scanf ("%lld", &n);
        a.resize (n);
        b.resize (n);
        for(i = 0; i < n; ++i) { scanf ("%lld", &a[i]); }
        for(i = 0; i < n; ++i) { scanf ("%lld", &b[i]); }
        sort(a.begin(), a.end());
        sort(b.rbegin(), b.rend());
        for(co = i = 0; i < n; ++i) { co += a[i] * b[i]; }
        printf ("Case #%lld: %lld\n", ++it, co);
    }
    return 0;
}
