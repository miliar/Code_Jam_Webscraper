#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<pair<int, int> > VII;
typedef vector<char> VC;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef map<int, int> MII;
typedef long long int LL;

#define FOR(i,a,b) for (int i=(int)(a); i<(int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,c) for (__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define SORT(c) sort((c).begin(), (c).end());
#define RSORT(c) sort((c).rbegin(), (c).rend());
#define DUMP(x) cerr << #x << "=" << (x) << " ";
#define DUMPLN(x) cerr << #x << "=" << (x) << endl;

void putAnswer(int count) {
    static int i = 1;
    printf("Case #%d: %d\n", i++, count);
}

int rotate(int val, int factor) {
    // factor should be more than 1
    return (val / 10) + ((val % 10) * factor);
}

void solve() {
    int A, B; cin >> A >> B;
    int loglen = log(A) / log(10);
    int factor = 1;
    REP(i, loglen) { factor *= 10; }

    int count = 0;
    for (int i = A; i < B; ++i) {
        set<int> candidate;
        int r = i;
        REP(j, loglen) {
            r = rotate(r, factor);
            if (i < r && r <= B) {
                candidate.insert(r);
            }
        }
        count += candidate.size();
    }

    putAnswer(count);
}

int main() {
    int NUM_CASES; cin >> NUM_CASES;
    REP(i, NUM_CASES) solve();
}
