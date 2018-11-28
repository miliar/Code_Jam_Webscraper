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

int hits(int cur, int a, int n, int mask) {
    int ret = cur;
    if (mask > 0)
        ret += (n - a + 1) + (n + 1);
    else
        ret += (n - a + 1);
    return ret;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int T;
    scanf("%d\n", &T);
    REP(tests, T) {
        double ans = INF, current = 0;
        int A, B;
        scanf("%d%d", &A, &B);
        int N = 1 << A;
        vector<double> probability (A), ev (N);
        REP(i, A)
            scanf("%lf", &probability[i]);

        REP(i, N) {
            ev[i] = 1;
            int tmp = i;
            REP(j, A) {
                double mult = (tmp % 2 == 1) ? 1 - probability[j] : probability[j];
                ev[i] *= mult;
                tmp /= 2;
            }
        }
/*        REP(i, (N-1)/2) 
            swap(ev[i], ev[N - 2 - i]);*/

/*        REP(i, N)
            //cout << ev[i] << " ";
            printf("%0.3lf ", ev[i]);
        cout << "\n";
*/
        REP(bs, A + 1) {
            current = 0;
            REP(i, N) {
                current += ev[i] * hits(bs, A - bs, B, i & ( (1 << (A - bs)) - 1)/*(i)/pow(2.0, bs)*/);
                //if (tests == 2)
//                    printf("%5d ", hits(bs, A - bs, B, i & ( (1 << (A - bs)) - 1)) );
            }
           // if (tests == 2)
                //cout << current << "\n";            
            ans = min(ans, current);
        }

        ans = min(ans, 1.0*B + 2);
        printf("Case #%d: %.6lf\n", tests + 1, ans);
    }
    return 0;
}