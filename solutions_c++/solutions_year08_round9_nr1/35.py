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

#define PII pair<int, int>
#define maxn 5005

using namespace std;

int n;
int a[maxn], b[maxn], c[maxn];

void solvecase() {
	scanf("%d", &n);
	FOR(i, n) scanf("%d%d%d", &a[i], &b[i], &c[i]);
	int res = 0;
	for (int takea = 0; takea <= 10000; takea++) {
		vector<PII> v;
		FOR(i, n) if (a[i] <= takea) v.PB(MP(b[i], c[i]));
		sort(ALL(v));
		int k = SZ(v);
		priority_queue<int> q;
		int have = 10000 - takea;
		FOR(i, k) {
			if (v[i].first > have) break;
			q.push(v[i].second);
			int havec = have - v[i].first;
			while (!q.empty() && q.top() > havec) q.pop();
			res = max(res, SZ(q));
		}

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
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}