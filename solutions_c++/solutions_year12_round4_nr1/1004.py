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
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define LL long long
#define pii pair<int, int>
#define x first
#define y second
#define gcd(x, y) __gcd((x), (y))
#define countbit(x) __builtin_popcount(x)

using namespace std;

int main(int argc, char **argv){
    int T;
    cin >> T;
    FOR(ca, 1, T+1){
        printf("Case #%d: ", ca);
        int N;
        cin >> N;
        vi d(N), l(N);
        FOR(i, 0, N) cin >> d[i] >> l[i];
        int D;
        cin >> D;
        int swing[N];
        memset(swing, -1, sizeof(swing));
        swing[0] = min(d[0], l[0]);
        FOR(i, 1, N)
            FOR(j, 0, i)
                if (swing[j] + d[j] >= d[i]){
                    swing[i] = max(swing[i], min(l[i], d[i]-d[j]));
                }
        bool ok = 0;
        FORc(i, 0, N, !ok) if (swing[i] != -1) ok = d[i] + swing[i] >= D;
        puts(ok?"YES":"NO");
    }
	return 0;
}
