#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;


typedef pair < int , int > pii;
typedef vector < int > vi;
typedef long long LL;


#define REP(i, a) for (int i = 0; i < a; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define mp make_pair
#define F first
#define S second
#define pb push_back
#define CLEAR(x, val) memset(x, val, sizeof(x))

int poww10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
map < pii, bool > is_used;


int length(int n) {
	if (n < 10)
		return 1;
	else if (n < 100)
		return 2;
	else if (n < 1000)
		return 3;
	else if (n < 10000)
		return 4;
	else if (n < 100000)
		return 5;
	else if (n < 1000000)
		return 6;
	else
		return 7;
}

int get_num(int i, int n, int len) {
	return (n % poww10[i]) * poww10[len - i] + n / poww10[i];
}

LL counts (int l, int h, int n) {
	int len = length(n);
	
	int ret = 0, tmp;
	
	FOR(i, 1, len - 1) {
		tmp = get_num(i, n, len);
		if (tmp != n && tmp >= l && tmp <= h && length(tmp) == length(n)) {
			if (!is_used[mp(tmp, n)]) {
				is_used[mp(tmp, n)] = 1;
				is_used[mp(n, tmp)] = 1;
				ret++;
			}
		}
	}
	return ret;
}

int tc;

int main () {
	
	//cout << get_num(1, 12, 2) << endl;
	
	scanf("%d", &tc);
	
	LL ans = 0, a, b;
	
	FOR(i, 1, tc) {
		ans = 0;
		
		scanf("%lld %lld", &a, &b);
		is_used.clear();
		
		FOR(ii, a, b) {
			ans += counts(a, b, ii);
		}
		
		printf("Case #%d: %lld\n", i, ans);
	}
	
}
