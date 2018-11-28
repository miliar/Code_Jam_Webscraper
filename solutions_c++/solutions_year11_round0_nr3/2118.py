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

int a[1005];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int ntc;
	scanf("%d", &ntc);
	rep(T, ntc) {
		int n;
		scanf("%d", &n);
		int sxor = 0, sum = 0;
		rep(i, n) {
			scanf("%d", &a[i]);
			sxor ^= a[i];
			sum += a[i];
		}
		printf("Case #%d: ", T+1);
		if (sxor != 0) printf("NO\n");
		else {
			int mini = a[0];
			fori(i, 1, n-1) if (mini > a[i])
				mini = a[i];
			printf("%d\n", sum - mini);
		}
	}
	return 0;
}
