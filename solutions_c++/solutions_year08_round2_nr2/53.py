#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

using namespace std;

LL a, b, p;
bool f[1000005];

void dfs(LL x) {
	if (x<a || x>b || f[x-a]) return;
	f[x-a] = true;
	LL i, t = x;
	for (i = 2; i * i <= t; i++) if (t % i == 0) {
		// i - prime factor
		if (i >= p) {
			dfs(x-i); dfs(x+i);
		}
		while (t % i == 0) t /= i;
	}
	if (t >= p) {
		dfs(x-t); dfs(x+t);
	}	
}

void solvecase() {
	scanf("%lld%lld%lld", &a, &b, &p);
	CLR(f, 0);
	int res = 0;
	for (LL i = a; i <= b; i++) if (!f[i-a]) {
		dfs(i);
		res++;
	}
	printf("%d", res);	
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("x", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}