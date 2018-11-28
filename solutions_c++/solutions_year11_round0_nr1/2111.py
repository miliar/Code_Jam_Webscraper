#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i,n) for( int i = 0, _n = (n); i < _n; i++ )
#define fori(i,a,b) for( int i = (a), _n = (b); i <= _n; i++ )
#define ford(i,a,b) for( int i = (a), _n = (b); i >= _n; i-- )
#define tr(it,c) for( __typeof((c).begin()) it = (c).begin(); it != (c).end(); it++ )

#define debug(x) cout << ">>" << #x << " = " << x << endl;

#define two(x) (1<<(x))
#define contain(S,x) (((S)&two(x)) > 0)
#define twoll(x) (1LL<<(x))
#define containll(S,x) (((S)&twoll(x))>0)

#define pb push_back
#define mp make_pair

#define st first
#define nd second

typedef pair<int, int> ii;

int n;
vector<ii> seq;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int ntc;
	scanf("%d", &ntc);
	rep(T, ntc) {
		scanf("%d", &n);
		seq.clear();
		rep(i, n) {
			char str[2];
			int btnNum;
			scanf("%s %d", str, &btnNum);
			if (str[0] == 'O')
				seq.pb(ii(0, btnNum));
			else
				seq.pb(ii(1, btnNum));
		}
		int staO = 1, staB = 1;
		int timeO = 0, timeB = 0;
		
		int mtime = 0;
		rep(i, seq.size()) {
			if (seq[i].st == 0) {
				int timeSpan = abs(staO - seq[i].nd);
				staO = seq[i].nd;
				timeO += timeSpan + 1;
				if (timeO <= mtime) {
					mtime = mtime+1;
					timeO = mtime;
				}
				else mtime = timeO;
			}
			else {
				int timeSpan = abs(staB - seq[i].nd);
				staB = seq[i].nd;
				timeB += timeSpan + 1;
				if (timeB <= mtime) {
					mtime = mtime+1;
					timeB = mtime;
				}
				else mtime = timeB;
			}
		}
		
		printf("Case #%d: %d\n", T+1, mtime);
	}
	return 0;
}
