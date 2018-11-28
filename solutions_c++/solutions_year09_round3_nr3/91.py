#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cctype>
#include <cmath>
#include <numeric>
#include <sstream>
using namespace std;
typedef long long ll;

typedef vector<int> VI;
typedef vector<VI> VVI; 

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))

int p, n;
int q[200];
int cache[200][200];
int dp( int first, int second ) {
	if( first > second ) return 0;
	int &ret = cache[first][second];
	if(ret!=-1) return ret;
	ret = 987654321;
	for(int i=first;i<=second;++i) {
		ret <?= dp(first,i-1) + dp(i+1,second) + q[second+1] - q[i] - 1 + q[i] - q[first-1] - 1;
	}
	return ret;
}

int main() {
	freopen("d:\\incomming\\C-large.in","r",stdin);
	int tn;
	cin >> tn;
	REP(cc,tn) {
		CLEAR(cache,-1);
		cin >> p >> n;
		REP(i,n) {
			cin >> q[i+1];
		}
		q[0] = 0;
		q[n+1] = p+1;
		sort(q,q+n+1);
		printf("Case #%d:", cc+1);
		printf(" %d\n", dp(1,n));
	}
}


