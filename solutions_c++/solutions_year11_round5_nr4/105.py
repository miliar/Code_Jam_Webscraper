#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <bitset>
#include <set>
#include <sstream>
#include <stdlib.h>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define forit(X,Y) for(typeof((Y).begin()) X = (Y).begin(); X != (Y).end(); ++X)

#define debug(x) cout << '>' << #x << ':' << x << endl;

typedef long long int64;

typedef vector <int> vi;
typedef vector < vi > vvi;

bool bit(int64 mask, int k) {
    return ((1LL << k) & mask) != 0;
}

bool isSquare(int64 n) {
    int64 sq = sqrt((long double)n);
    while (sq * sq < n) ++sq;
    while (sq * sq > n) --sq;
    return sq * sq == n;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int testCount;
    cin >> testCount;
    for (int testNumber = 1; testNumber <= testCount; ++testNumber) {
        cerr << "Case #" << testNumber << "..." << endl;
        
        string s;
        cin >> s;
        int nq = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) if (s[i] == '?') ++nq;
        for (int64 mask = 0; mask < (1LL << nq); ++mask) {
            int k = 0;
            int64 num = 0;
            for (int i = 0; i < n; ++i) {
                num *= 2;
                if (s[i] == '1') ++num;
                if (s[i] == '?') {
                    if (bit(mask, k)) ++num;
                    ++k;
                }
            }
            if (isSquare(num)) {
                k = 0;
                for (int i = 0; i < n; ++i) {
                    if (s[i] == '?') {
                        s[i] = bit(mask, k) ? '1' : '0';
                        ++k;
                    }
                }
            }
        }



        /*printf("Case #%d:\n", testNumber);
        for (int i = 0; i < sz(res); ++i) {
            printf("%.8lf\n", res[i]);
        }*/
        cout << "Case #" << testNumber << ": " << s << endl;
    }

    return 0;
}