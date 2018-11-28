#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++){
		int n, m, s;
		scanf("%d%d%d", &n, &m, &s);
		int i, j, k, q;
		int a = max(n, m);
		int b = min(n, m);
		for (i = 0; i <= a - 1 && i * min(i, b) < s; i++);
		for (q = 0; q <= b - 1 && i * q < s; q++);
		if (a != n)
			swap(i, q);
		s -= i * q;
		s = -s;
		if (s < 0){
			printf("Case #%d: IMPOSSIBLE\n",ti);
			continue;
		}
		if (s == 0){
			j = 0;
			k = 0;
			goto ok;
		}
		for (j =1; j <= m; j++)
			if (s % j ==0 && s / j <= n){
				k = s / j;
				goto ok;
			}
		printf("Case #%d: IMPOSSIBLE\n",ti);
		continue;
ok:
		printf("Case #%d: 0 0 %d %d %d %d\n", ti, i, j, k, q);
	}
	return 0;
}