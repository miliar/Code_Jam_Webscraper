#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<utility>
#include<queue>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;

#define MP make_pair
#define PB push_back
#define REP(i, n) for(int i=0, _n=(n); i<_n; ++i)
#define min(a, b) ((a)<(b)?(a):(b))
#define max(a, b) ((a)>(b)?(a):(b))

int mid;
bool can;
int cnt[10], p, c[10], ans[10], v[10], u[10];
bool r[10][10], a[10][10];
int d[10], td[10];
int n, m;

int q[10], hd, tl;
bool go(int x)
{
//	cout << x << endl;
	bool vtd[10];
	memset(vtd, 0, sizeof(vtd));
	hd = -1; tl = 0;
	q[0] = x; vtd[x] = true;
	int e1 = -1, e2 = -1;
	while (hd != tl) {
		x = q[++hd];
		for (int i = 1; i<= n; ++i)
			if (a[x][i] && !vtd[i]) {
				vtd[i] = true;
				if (td[i] != 2) {
					if (e1 == -1) e1 = i;
					else e2 = i;
				}
				else {
					q[++tl] = i; 
				}
		}
	}
	if (e1 == -1 && e2 == -1) {
		for (int i = 0; i <= tl; ++i) {
			for (int j = 0; j <= tl; ++j)
				if (a[q[i]][q[j]]) {
					--td[q[j]]; a[q[i]][q[j]] = 0;
			}
		}
		return true;
	}
	if (e1 > -1 && e2 > -1) 
		if (a[e1][e2]) {
			q[++tl] = e1; q[++tl] = e2;
			for (int i = 0; i <= tl; ++i) {
			for (int j = 0; j <= tl; ++j)
				if (a[q[i]][q[j]]) {
					--td[q[j]]; a[q[i]][q[j]] = 0;
			}
			}
			a[e1][e2] = a[e2][e1] =1;
			++td[e1]; ++td[e2];
			return true;
	}
	return false;
}

bool check()
{
	for (int i = 1; i <= n; ++i) 
		td[i] = d[i];
	memcpy(a, r, sizeof(a));
	bool change = true;
	while (change) {
		change = false;
		for (int i = 1; i <= n; ++i) 
			if (td[i] == 2 && go(i)) {
//				if (i != 1) cout << i << endl;
				bool cl[10];
				memset(cl, 0, sizeof(cl));
				int pp = 0;
				for (int i = 0; i <= tl; ++i) {
					if (!cl[c[q[i]]]) ++pp;
					cl[c[q[i]]] = true;
				//	cout << q[i] << ' ';
				}
				//cout << endl;
				if (pp < mid) return false;
				change = true; break;	
		}
	}
	return true;
}

void dfs(int x)
{
	if (n - x < p) return;
	if (x == n) {
		/*
		for (int i = 1; i <= n; ++i)
			cout << c[i] << ' ';
		cout << endl;
		*/
		if (check()) {
			can = true;
			for (int i = 1; i <= n; ++i)
				ans[i] = c[i];
		}
		return;
	}
	for (int i = 1; i <= mid; ++i) {
		++cnt[i];
		if (cnt[i] == 1) --p;
		c[x + 1] = i;
		dfs(x + 1);
		if (can) return;
		--cnt[i];
		if (cnt[i] == 0) ++p;
	}
}

int main()
{
	freopen("c.in", "rt", stdin);
	freopen("c.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	//T = 1;
	for (int tt = 1; tt <= T; ++tt) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < m; ++i)
			scanf("%d", &u[i]);
		for (int i = 0; i < m; ++i)
			scanf("%d", &v[i]);
		memset(r, 0, sizeof(r));
		for (int i = 1; i <= n; ++i) {
			int x = (i+1>n)?1:(i+1);
			r[i][x] = r[x][i] = 1;
			d[i] = 2;
		}
		for (int i = 0; i < m; ++i) {
			r[u[i]][v[i]] = r[v[i]][u[i]] = 1;
			++d[u[i]], ++d[v[i]];
		}
		int L = 0, R = n;
		memset(cnt, 0, sizeof(cnt));
		//for (int i = 1 ; i <= n; ++i)
			//cout << d[i] << endl;
		//check();
		//if (0)
		while (L <= R) {
			mid = (L + R) / 2;
			can = false;
			p = mid;
			memset(cnt, 0, sizeof(cnt));
//			cout << mid << endl;
			dfs(0);
			if (can) L = mid + 1;
			else R = mid - 1;
		}
		printf("Case #%d: %d\n", tt, L - 1);
		for (int i = 1; i < n; ++i)
			printf("%d ", ans[i]);
		printf("%d\n", ans[n]);
	}
	return 0;
}
