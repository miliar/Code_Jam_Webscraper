#include <stdio.h>
#include <algorithm>
using namespace std;
#define N 1010
int m[N], p[N];
int main()
{
	int i, j, n, t, ts;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &n), i=0; i<n; scanf("%d", &m[i]), p[i]=m[i], i++);
		for(sort(m, m+n), j=0, i=0; i<n; j+=m[i]!=p[i], i++);
		printf("Case #%d: %d.0\n", t+1, j);
	}
	return 0;
}