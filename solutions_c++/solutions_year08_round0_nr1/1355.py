#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <iostream>
#include <sstream>
#include <cmath>
#include <cstdio>
using namespace std;
 
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
 
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,a) for(int i=0;i<(a);i++)
#define FOREACH(i,x) for(__typeof((x).begin()) i=(x.begin()); i!=(x).end(); ++i)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define INF 1000000000

int A[1000], B[100];

int main () {
	int t;
	scanf("%d\n",&t);
	REP(c,t) {
		map <string, int> M;
		int s,q;
		scanf("%d\n",&s);
		char tmp[200];
		REP(i,s) {
			gets(tmp);
			M[tmp] = i;
		}
		scanf("%d\n",&q);
		REP(i,q) {
			gets(tmp);
			A[i] = M[tmp];
		}

		int res = INF;
		REP(i,q) {
			int cur = 0, j = i;
			while (j < q) {
				memset(B,0,sizeof(B));
				int left = s;
				while (left && j < q) {
					if (!B[A[j]]) {
						left--;
						B[A[j]] = 1;
					}
					if (left) j++;
				}
				if (!left) cur++;
			}
			j = i - 1;
			while (j > 0) {
				memset(B,0,sizeof(B));
				int left = s;
				while (left && j >= 0) {
					if (!B[A[j]]) {
						left--;
						B[A[j]] = 1;
					}
					if (left) j--;
				}
				if (!left) cur++;
			}
			if (i) cur++;
			res <?= cur;
		}
		if (q) printf("Case #%d: %d\n", c + 1, res); else printf("Case #%d: 0\n", c + 1);
	}

	return 0;
}

