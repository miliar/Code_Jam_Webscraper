#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define for1(i, n) for(int i = 1; i <= int(n); ++i)
#define ford(i, n) for(int i = int(n) - 1; i >= 0; --i)
#define fore(i, l, r) for(int i = int(l); i < int(r); ++i)
#define sz(v) int((v).size())
#define X first
#define Y second
#define all(v) (v).begin(), (v).end()
#define mp(q, p) make_pair(q, p)
#define sqr(a) ((a) * (a))
#define pb push_back
#define ensure(a) assert(a)

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const int INF = 1E9 + 7;
const int NMAX = 1E3 + 7;
const ld EPS = 1E-9;

string text;
string wcj = "welcome to code jam";

const int MOD = 10000;

int d[40][1000];

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int N;
    scanf("%d\n", &N);
    for1(T, N){
        printf("Case #%d: ", T);
        getline(cin, text);
        memset(d, 0, sizeof(d));
        forn(pos1, sz(text)){
            if(text[pos1] == wcj[0]) d[0][pos1] = 1;
            if(pos1 == 0) continue;
            for1(pos2, sz(wcj) - 1){
                if(text[pos1] == wcj[pos2]){
                    d[pos2][pos1] += accumulate(d[pos2 - 1], d[pos2 - 1] + sz(text), 0);                   
                    d[pos2][pos1] %= MOD;
                }
            }
        }

        int ans = accumulate(d[sz(wcj) - 1], d[sz(wcj) - 1] + sz(text), 0) % MOD;
        string s;
        forn(i, 4){
            s += ((ans % 10) + '0');
            ans /= 10;
        }
        reverse(all(s));
        cout << s << endl;
    }
    return 0;
}
