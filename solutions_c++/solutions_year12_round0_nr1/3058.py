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

void putCase() {
    static int i = 1;
    printf("Case #%d: ", i++);
}

//----------------------------------------------------
int NUM_CASES = 0;

char MAP['z'];

char change(char ch) {
    if (ch == ' ') return ch;
    return MAP[ch];
}

void solve() {
    string line;
    while (getline(cin, line)) {
        putCase();
        REP(i, line.size()) {
            cout << change(line[i]);
        }
        cout << endl;
    }
}


int main() {
    string line;
    getline(cin, line);
    NUM_CASES = atoi(line.c_str());

    const char* m1 = "abcdefghijklmnopqrstuvwxyz";
    const char* m2 = "ynficwlbkuomxsevzpdrjgthaq";
    REP(i, 26) {
        MAP[m2[i]] = i + 'a';
    }

    REP(i, NUM_CASES) solve();
}
