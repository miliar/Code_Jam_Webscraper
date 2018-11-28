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


int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int T;
    scanf("%d\n", &T);
    for1(Q, T){
        printf("Case #%d: ", Q);
        string s;
        getline(cin, s);
        map<char, int> idx;
        string num;
        num.resize(sz(s));
        idx[s[0]] = 1;
        forn(i, sz(s)){
            if(!idx.count(s[i])){
                if(sz(idx) > 1)
                    idx[s[i]] = sz(idx);
                else
                    idx[s[i]] = 0;
            }
            num[i] = idx[s[i]];
        }
        int base = max(2, sz(idx));
        li ans = 0;
        li mul = 1;
        ford(i, sz(num)){
            ans += mul * num[i];
            mul *= base;
        }
        cout << ans << endl;
    }
    return 0;
}
