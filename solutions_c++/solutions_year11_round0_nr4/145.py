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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define LL long long
#define pii pair<int, int>
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define countbit(X) __builtin_popcount(X)
#define gcd(x, y) __gcd(x, y)

using namespace std;

int par[1001];

void make(int N){ FOR(i, 0, N) par[i] = i;}
int find(int x){ return par[x]==x?x:(par[x]=find(par[x]));}
bool same(int x, int y){ return find(x) == find(y);}
void join(int x, int y){ int rx = find(x), ry = find(y); if (rx != ry) par[rx] = ry;}

int main(int argc, char **argv){
        int T;
        cin >> T;
        FOR(Ca, 1, T+1){
                printf("Case #%d: ", Ca);
                int N;
                cin >> N;
                int t;
                make(N);
                FOR(i, 0, N) cin >> t, join(i, --t);
                int seen[N];
                memset(seen, 0, sizeof(seen));
                FOR(i, 0, N) seen[find(i)]++;
                double res = 0;
                FOR(i, 0, N) if (seen[i] > 1) res += seen[i];
                printf("%.10f\n", res);
        }
        return 0;
}
