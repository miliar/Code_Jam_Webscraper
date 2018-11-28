#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

long long S[501][501];
long long com[51][51];

long long comb(int a, int b) {
	if (com[a][b] != -1)
		return com[a][b];
	if (b == 1)
		return a;
	if (b == a)
		return 1;
	if (b == 0)
		return 1;
	if (a == 0)
		return 0;

	return (com[a][b] = (comb(a-1,b-1) + comb(a-1,b)) % 100003);
}

long long go(int n, int index) {
	if (index == 1)
		return 1;
	if (n <= index)
		return 0;
	if (S[n][index] != -1)
		return S[n][index];

	long long res = 0;

	int i;
	for (i = index-1; i >= 1; --i) {
		if (index - i > n - index)
			break;
		res += go(index, i) * comb(n-index-1, index-i-1);
		//cout << index << ' ' << i << " ÀÇ °ªÀº " << go(index,i) << endl;
		//cout << index-i-1 << ' ' << n - index - 1 << endl;
		res %= 100003;
	}

	return (S[n][index] = res% 100003);
}

void main() {
	memset(S,-1,sizeof(S));
	memset(com,-1,sizeof(com));
	int T,n;
	int i,j;

	scanf("%d", &T);

	REP(i,T) {
		long long res = 0;
		scanf("%d", &n);
		FOR(j,1,n-1) {
			res += go(n,j);
			//cout << n << ' ' << j << ' ' << res << endl;
			res %= 100003;
		}

		cout << "Case #" << (i+1) << ": " << res << endl;
	}
}