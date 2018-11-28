#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define SZ(a) ((int) a.size())
#define pb push_back

#define VAR(a,b) __typeof(b) a=(b)
#define FORE(it,a) for(VAR(it,(a).begin());it!=(a).end();it++)
#define X first
#define Y second
#define DEBUG(x) cout << #x << " = " << x << endl;

#define INF 1000000000

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long ll;

string s;

int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;
    cin >> test;
    FOR (ntest, 1, test+1)
    {
        int n;   
        cin >> n;
        VI a;
        REP (i, n)
        {
            cin >> s;
            int k = -1;
            REP (j, SZ (s))
                if (s[j] == '1')
                    k = j;
            a.pb (k);            
        }              
        cout << "Case #" << ntest << ": ";
        int ans = 0;          
        again:
            REP (i, n)
                if (a[i] > i)
                {
                    for (int j = i+1; j < n; ++j)
                        if (a[j] <= i)
                        {
                            swap (a[j], a[j-1]);
                            ++ans;
                            goto again;
                        }
                }
        cout << ans << endl;
    }    
	return 0;
}
