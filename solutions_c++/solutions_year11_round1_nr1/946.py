#include <vector>
#include <cmath>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <cctype>
#include <stack>

using namespace std;

#define fe(i,a,n) for(int i = a, __n = n; i < __n; i++)
#define fi(i,a,n) for(int i = a, __n = n; i <= __n; i++)
#define LL long long
#define ULL unsigned long long
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define SI stack<int>
#define SS stack<string>
#define SD stack<double>
#define ERRO 1e-10
#define INF 1e+99
#define tr(i,s) for(typeof(s.begin()) i = s.begin(); i != s.end(); i++)
#define all(v) v.begin(), v.end()

ULL gcd(ULL u, ULL v) {
    int shift;
    if (u == 0 || v == 0)
        return u | v;
    /* Let shift := lg K, where K is the greatest power of 2
     dividing both u and v. */
    for (shift = 0; ((u | v) & 1) == 0; ++shift) {
        u >>= 1;
        v >>= 1;
    }
    while ((u & 1) == 0)
        u >>= 1;

    /* From here on, u is always odd. */
    do {
        while ((v & 1) == 0) /* Loop X */
            v >>= 1;

        /* Now u and v are both odd, so diff(u, v) is even.
         Let u = min(u, v), v = diff(u, v)/2. */
        if (u < v) {
            v -= u;
        } else {
            ULL diff = u - v;
            u = v;
            v = diff;
        }
        v >>= 1;
    } while (v != 0);

    return u << shift;
}

int main() {
    int a;
    cin >> a;
    fe(i,0,a) {

        string ret = "Possible";
        ULL x, y, z;
        cin >> x >> y >> z;
        //cout << x << " " << y << " " << z << endl;
        if (x < 1 || y < 0 || z < 0) {
            ret = "Broken";
        } else if (z == 0 && y != 0) {
            ret = "Broken";
        } else if (z == 100 && y != 100) {
            ret = "Broken";
        } else {
            ULL g = gcd(y, 100);
            //cout << g << endl;
            ULL h = 100 / g;
            //cout << h << endl;
            if (h > x) {
                ret = "Broken";
            }
        }

        if (i != a - 1) {
            cout << "Case #" << i + 1 << ": " << ret << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << ret;
        }

    }
    return 0;
}
