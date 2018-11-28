#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d\n" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int main() {
    int tests = GETINT;
    FOR(t, tests) {
        int S = GETINT;
        map< string, int > index;
        FOR(i, S) {
            string p;
            getline(cin, p);
            index[p] = i;
        }
        int Q = GETINT;
        int best[Q+1][S];
        FOR(i, S) best[0][i] = 0;
        FOT(i, 1, Q+1) {
            string p;
            getline(cin, p);
            int what = index[p];
            FOR(j, S) {
                best[i][j] = 1000000;
                if (j == what) ;
                else {
                    FOR(k, S) best[i][j] = min(best[i][j], best[i-1][k] + (j == k ? 0 : 1));
                }
            }
        }
        int ans = 2000000;
        FOR(i, S) ans = min(ans, best[Q][i]);
        printf("Case #%d: %d\n", t + 1, ans);
    }
    return 0;
}
