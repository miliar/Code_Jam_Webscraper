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
#define maxn 100005

using namespace std;

int x[maxn], y[maxn];
int n, m;
LL cnt[3][3], cnt2[3][3];

void solvecase() {
	int a, b, c, d, x0, y0;
	scanf("%d%d%d%d%d%d%d%d", &n, &a, &b, &c, &d, &x0, &y0, &m);
	x[0] = x0; y[0] = y0;
	for (int i = 1; i < n; i++) {
		x[i] = (b + (LL)x[i-1] * a) % m;
		y[i] = (d + (LL)y[i-1] * c) % m;	
	}
	CLR(cnt, 0);
	CLR(cnt2, 0);
	//set<pair<int, int> > p;
	//FOR(i, n) p.insert(MP(x[i], y[i]));
	LL res = 0;
	for (int i = 0; i < n; i++) {
		res += cnt2[(3-x[i]%3)%3][(3-y[i]%3)%3];
		FOR(mx, 3) FOR(my, 3) cnt2[(mx+x[i])%3][(my+y[i])%3] += cnt[mx][my];
		cnt[x[i]%3][y[i]%3]++;
	}
/*
	for (int i = 0; i < n; i++)
		for (int j = i+1; j < n; j++)
			for (int k = j+1; k < n; k++) {
				LL xx = x[i] + x[j] + x[k];
				LL yy = y[i] + y[j] + y[k];
				if (xx % 3 == 0 && yy % 3 == 0) {
					//if (p.find(MP(xx/3,yy/3)) != p.end()) 
					res++;
				}
			}
*/
	printf("%lld", res);
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
freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}