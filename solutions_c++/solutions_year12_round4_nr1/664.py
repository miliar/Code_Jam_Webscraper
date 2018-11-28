#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
//#include <conio.h>

using namespace std;

#define X first
#define Y second
#define pb push_back
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define oo 1000000000
#define MAXN 10005
#define mp make_pair

typedef pair<int, int> PII;
typedef vector<int> VI;
map <PII, int> mm;

int ntest, n, d[MAXN], l[MAXN];

bool process() {
    queue <PII> Q;
    mm.clear();
    if (d[1] > l[1]) return false;
    Q.push(mp(1, d[1]));
    while (!Q.empty()) {
        PII X = Q.front();
        Q.pop();
        FOR(i, X.X + 1, n) {
            if (X.Y >= d[i] - d[X.X]) {
                int ll = min(d[i] - d[X.X], l[i]);
                if (mm[mp(i, ll)]) continue;
                Q.push(mp(i, ll));
                mm[mp(i, ll)] = 1;
                //cout << i << ' ' << d[i] - d[X.X] << endl;
                if (i == n) return true;
            }
        }
    }
    return false;
}

int main () {
    freopen("A-small.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> ntest;
    FOR(test, 1, ntest) {
        cin >> n;
        FOR(i, 1, n) cin >> d[i] >> l[i];
        n++;
        cin >> d[n];
        l[n] = oo;
        if (process()) printf("Case #%d: YES\n", test);
        else printf("Case #%d: NO\n", test);
    }
    return 0;
}
