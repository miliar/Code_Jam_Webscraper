#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cctype>
#include <functional>
using namespace std;

typedef pair<int, int> PII;

const int N = 1024;

int next(int *a, int *b, int n, int index)
{
	int l = lower_bound(b, b+n, a[index]) - b;
	return l;
}

vector<int> readData()
{
	int a[N], b[N], n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		int e; scanf("%d", &e);
		a[i] = b[i] = e;
	}
	sort(b, b+n);
	vector<int> res;
	bool vst[N] = { false };
	for(int i = 0; i < n; i++) if(!vst[i]) {
		vst[i] = true;
		int cc = 1;
		for(int j = next(a, b, n, i); j != i; j = next(a, b, n, j)) { cc++; vst[j] = true; }
		res.push_back(cc);
	}
	return res;
}

double dp[N], p[N], fact[N];

double go(int n)
{
	if(n <= 1) return 0;
	if(dp[n] > -1e10) return dp[n];
	dp[n] = 0;
	for(int i = 1; i <= n; i++) dp[n] += go(n-i) * p[n-i] / fact[i];
	dp[n] = (dp[n]+1)/(1-p[n]);
	return dp[n];
}

int main()
{
	freopen("G:\\D-large.in", "r", stdin);
	freopen("G:\\D.out", "w", stdout);
	
	for(int i = 0; i < N; i++) dp[i] = -1e200;
	fact[0] = 1;
	for(int i = 1; i < N; i++) fact[i] = fact[i-1] * i;
	// p[n] = \sum_{i=0}^{n}(-1)^i/i!
	double f = 1;
	p[0] = 1;
	for(int i = 1; i < N; i++) {
		f *= -1.0/i;
		p[i] = p[i-1] + f;
	}
	
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++) {
		vector<int> lnx = readData();
		double res = 0;
		for(int i = 0; i < lnx.size(); i++) res += go(lnx[i]);
		printf("Case #%d: %.6lf\n", t+1, res);
	}
	
	return 0;
}
