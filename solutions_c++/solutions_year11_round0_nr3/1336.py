/*
 * Author: ZaviOr
 * Created Time:  2011/5/7 14:03:59
 * File Name: C.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>
#include <string>
using namespace std;
#define out(X) cerr << #X << ": " << (X) << endl
#define SZ(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define REP(I,N) for (int I = 0; I < (N); ++I)
#define FOR(I,L,H) for (int I = (L); I < (H); ++I)
#define FORIT(I,V) for (typeof(V.begin()) I = V.begin(); I != V.end(); ++I)
#define MP(X,Y) make_pair((X),(Y))
#define PB push_back
#define ALL(X) X.begin(), X.end()
typedef long long LL;

int val[1010];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, t = 0;
    cin >> T;
    while (t < T) {
        printf("Case #%d: ", ++t);
        int n;
        cin >> n;
        REP(i, n) {
            cin >> val[i];
        }
        LL sum = val[0];
        FOR(i, 1, n) {
            sum ^= val[i];
        }
        if (sum == 0) {
            sort(val, val + n);
            FOR(i, 1, n) {
                sum = sum + val[i];
            }
            cout << sum << endl;
        } else {
            printf("NO\n");
        }
    }
    return 0;
}

