// Template begins

#pragma comment (linker, "/STACK:214721677")
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <ctime>

using namespace std;

#define REP(i,n) for (int i=0, _n=(n)-1; i <= _n; ++i)
#define REPD(i,n) for (int i=(n)-1; i >= 0; --i)
#define FOR(i,a,b) for (int i=(a), _b=(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i=(a), _b=(b); i >= _b; --i)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sz(a) ((int) ((a).size()))
template < class T > T sqr (T a) { return (a) * (a); }
template < class T > T abs (T a) { return (a < 0) ? -(a) : (a); }
const double Pi = acos(-1.0);
const double eps = 1e-10;
const int INF = 1000*1000*1000;
const double phi = 0.5 + sqrt(1.25);
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

// Template ends

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T,N,S,p;
    scanf("%d\n", &T);
    REP(tests, T) {
        scanf("%d%d%d", &N, &S, &p);
        vector <int> total (N);
        REP(i, N)
            scanf("%d", &total[i]);

      sort(total.begin(), total.end());

        int quantity = 0;
        vector <int> less;
            REP(i, N)
                if ( (total[i]+2)/3 >= p )
                    quantity++;
                else
                    less.pb(total[i]);

            for (int i = 0; i < sz(less) && S > 0; ++i)
                if ( (less[i]+4)/3 >= p && less[i] >= 2 && less[i] <= 28) {
                    quantity++;
                    S--;
                }

        printf("Case #%d: %d\n", tests + 1, quantity);
    }
    return 0;
}