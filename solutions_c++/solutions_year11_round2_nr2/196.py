#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cctype>
#include <functional>
#include <numeric>
using namespace std;

typedef long long llong;
typedef pair<int, int> PII;

const int N = 256, M = 1<<20;

int d, n;
int p[N], v[N];
int m, pos[M];

bool judge(double mid)
{
	double beg = pos[0]-mid;
	for(int i = 1; i < m; i++) {
		double last = pos[i] + mid;
		if(last < beg + d) return false;
		beg = max(beg + d, pos[i] - mid);
	}
	return true;
}

int main()
{
	freopen("E:\\B-large.in", "r", stdin);
	freopen("E:\\Blarge.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for(int t = 0; t < T; t++) {
		scanf("%d %d", &n, &d);
		for(int i = 0; i < n; i++) scanf("%d %d", &p[i], &v[i]);
		
		m = 0;
		for(int i = 0; i < n; i++) for(int j = 0; j < v[i]; j++) pos[m++] = p[i];
		
		double lo = 0, hi = 1e14;
		for(int ii = 0; ii < 100; ii++) {
			double mid = (hi+lo)/2;
			if(judge(mid)) hi = mid;
			else lo = mid;
		}
		
		printf("Case #%d: %.12lf\n", t+1, (lo+hi)/2);
	}
	
	return 0;
}
