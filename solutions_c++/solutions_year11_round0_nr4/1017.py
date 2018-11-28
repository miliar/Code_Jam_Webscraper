#pragma comment(linker, "/STACK:10000000")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define debug(x) {cerr << #x << " = " << x << endl;}
template<typename T> inline T abs(T a){ return ((a < 0) ? -a : a); }
template<typename T> inline T sqr(T a){ return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = (int)1E9 + 7;
const ld EPS = 1E-9;
const ld PI = 3.1415926535897932384626433832795;

const int NMAX = 2000;
bool calcG[NMAX], calcV[NMAX], calcF[NMAX];
ld g[NMAX], v[NMAX], f[NMAX];

ld G(int n){
    if(n == 0) return 1.0;
    if(n == 1) return 0.0;

    if(calcG[n]) return g[n];    

    calcG[n] = true;
    return g[n] = (1.0 / n) * ( G(n-2) + (n-1) * G(n-1) );
}

ld F(int n){
    if(n == 0 || n == 1) return 1.0;

    if(calcF[n]) return f[n];

    calcF[n] = true;
    return f[n] = F(n-1) * (ld(1) / n);
}

ld T(int n, int k){
    return G(n-k) * F(k);
}                 

ld V(int n, int k){
    if(n == k) return 0.0;
    if(calcV[k]) return v[k];

    calcV[k] = true;

    v[k] = G(n-k);
    fore(i, 1, n-k+1)
        v[k] += (V(n, k+i)+1.0) * T(n-k, i);
    v[k] /= 1.0 - G(n-k);

    return v[k];
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCount;
    cin >> testCount;
    cout.precision(10);
    cout << fixed;

    forn(curTest, testCount){
        printf("Case #%d: ", curTest+1);

        //Place solution here
        memset(calcV, 0, sizeof calcV);
        int n;

        cin >> n;
        vector<int> a(n);
        forn(i, n)
            cin >> a[i];
        vector<int> sa = a;
        sort(all(sa));

        int k = 0;
        forn(i, n)
            k += int(a[i] == sa[i]);

        cout << V(n, k) << endl;
    }
    
    return 0;
}



