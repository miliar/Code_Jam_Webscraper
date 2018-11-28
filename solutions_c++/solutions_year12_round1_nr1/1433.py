#include<cstring>
#include<cstdio>
#include<iostream>
using namespace std;
const int N = 1e5 + 100;
int n, m;
double p[N], cp[N];
double calOption12()
{
	double ret = 0x7fffffff;
	for (int i=0; i<=n; i++)
	{
		ret = min(ret, (cp[n - 1 - i] * (m - n + 1 + 2 * i)) + (1.0 - cp[n - 1 - i]) * (m - n + 1 + 2 * i + m + 1));	}
	return ret;
}
int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("A.out", "w", stdout);
	int cases, T = 1;
	scanf("%d", &cases);
	while(cases--)
	{
		scanf("%d %d", &n, &m);
		for (int i=0; i<n; i++) {
			scanf("%lf", &p[i]);
			cp[i] = (i==0) ? p[0] : (cp[i - 1] * p[i]);
		}
		double ret = calOption12();
		ret = min(ret, 2.0 + m);
		printf("Case #%d: %.6f\n", T++, ret);
	}
	return 0;
}