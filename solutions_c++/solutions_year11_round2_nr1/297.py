#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PI;
typedef vector<PI> VPI;
typedef unsigned long long ull;
typedef long long ll;
typedef long double LD;

#define FOR(i, n) for(typeof(n) i=0;i<(n);++i)
#define REP(i,s,n) for(typeof(n) i=s;i<=n;++i)
#define SZ(x) ((int)(x).size())
#define LOOP(i,x) FOR(i,SZ(x))
#define IT(it,x) for(typeof((x).begin()) it = (x).begin();it!=(x).end();++it)
#define ALL(x) (x).begin(), (x).end()
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
#define INF 2000000999

char m[105][105];
LD wp[105], owp[105], oowp[105];

int main() {
	//freopen("sample.txt", "r", stdin);
	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("out-large.txt", "w", stdout);
	
	int T, N;
	scanf("%d", &T);
	
	for(int kase = 1; kase <= T; ++kase) {
		printf("Case #%d:\n", kase);
		scanf("%d", &N);
		FOR(i, N)
			scanf("%s", m[i]);
		
		FOR(i, N) {
			wp[i] = 0;
			int cnt = 0;
			FOR(j, N) {
				wp[i] += (m[i][j] == '1');
				cnt += (m[i][j] != '.');
			}
			wp[i] /= cnt;
		}
		
		FOR(i, N) {
			owp[i] = 0;
			int cnt = 0;
			FOR(j, N) {
				if(m[i][j] == '.') continue;
				++cnt;
				LD cur = 0;
				int curcnt = 0;
				FOR(k, N) {
					if(k == i) continue;
					cur += (m[j][k] == '1');
					curcnt += (m[j][k] != '.');
				}
				cur /= curcnt;
				owp[i] += cur;
			}
			owp[i] /= cnt;
		}
		
		FOR(i, N) {
			oowp[i] = 0;
			int cnt = 0;
			FOR(j, N) {
				if(m[i][j] == '.') continue;
				oowp[i] += owp[j];
				++cnt;
			}
			oowp[i] /= cnt;
		}
		
		cout.precision(10); cout.setf(ios::fixed,ios::floatfield);
		FOR(i, N) {
			//cout << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
			cout << wp[i] / 4 + owp[i] / 2 + oowp[i] / 4 << endl;
		}
	}
	return 0;
}
