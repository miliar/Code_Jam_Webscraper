#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef unsigned long long int ull;
typedef long double ld;

int T,a[2],b[2];

map<pair<int,int>,bool> memo;

bool can_win(int a, int b) {
	if (a == b || a < 1 || b < 1) return false;
	// a > b
	int ta = a, tb = b;
	a = max(ta,tb);
	b = min(ta,tb);

	if (memo.count(MP(a,b))) return memo[MP(a,b)];
	
	int res = false;
	res |= !can_win(b, a % b);
	if ((a % b) + b < a) {
		res |= !can_win(b, (a % b) + b);
	}

	memo[MP(a,b)] = res;
	return res;
}

int solve() {
	int ans = 0;
	for(int i = a[0]; i <= a[1]; i++) {
		for (int j = b[0]; j <= b[1]; j++) {
			int ret = can_win(i,j);
			ans += ret;
			/*
			fprintf(stderr,"%d, %d is %s\n",
				i,j,
				ret? "winning" : "losing"
			);*/
		}
	}
	return ans;
}

int main() {
	cin >> T;
	FOR(t,T) {
		cin >> a[0] >> a[1] >> b[0] >> b[1];
		cout << "Case #" << t+1 << ": " << solve() << endl;
	}
	return 0;
}
