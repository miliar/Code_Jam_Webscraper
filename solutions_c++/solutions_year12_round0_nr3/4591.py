#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <cassert>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstring>
 
using namespace std;
 
#define ll long long
#define point pair<int, int>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define uint unsigned int
//#define double long double
#define merge botva
#define double long double

#ifdef ONLINE_JUDGE
#define olo "%I64d\n"
#define jolo "%011I64d"
#else
#define olo "%Ld\n"
#define jolo "%011Ld"
#endif

#define satan2 atan2
const int maxn = 200000, maxlen = 502 * 502 + 20, consta = 1050, maxi = consta + 4, big = 10000000,
magic = 239, magic1 = 359;
const long long INF = 1000000000;
const char BLANK = '-', FULL = '#';
const char trans[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int last = 1;
int a[maxn];
int where[maxn];

string s[maxn], t[maxn];
char chas[maxn];

int main() {
    //freopen("complexity.in", "r", stdin);
    //freopen("complexity.out", "w", stdout);
    int V, n, af, bf, t, lom, a, b;
    cin >> t;
    for (int fi = 1; fi <= t; ++fi) {
        scanf("%d%d", &a, &b);
        int res = 0;
        for (int i = a; i <= b; ++i)
            for (int j = i + 1; j <= b; ++j) {
                int st = 1;
                for (; ; ) {
                    if (st * 10 > i) break;
                    st *= 10;
                }
                int vi = i;
                bool good = 0;
                for (int la = 0; la < 10; ++la) {
                    vi = (vi % st) * 10 + (vi / st);
                    if (vi == j) good = 1;
                }
                if (good) ++res;
            }
        cout << "Case #" << fi << ": " << res << endl;
    }
    
} 
 
