#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
#define fil(a, b) memset(a,b,sizeof(a))
bool can[20000];
bool And[20000];
int d[20000][2];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++){
		int n, v;
		scanf("%d%d", &n, &v);
		fil(d,127);
		for (int i = 1; i <= n/2; i++){
			int t1, t2;
			scanf("%d%d", &t1, &t2);
			And[i] = t1;
			can[i] = t2;
		}
		for (int i = n/2 + 1; i <= n; i++){
			int t;
			scanf("%d", &t);
			d[i][t] = 0;
		}
		for (int i = n/2; i >= 1; i--){
			for (int v1 = 0; v1 <= 1; v1++)
			if (d[i * 2][v1] < n)
			for (int v2 = 0; v2 <= 1; v2++)
			if (d[i * 2 + 1][v2] < n)
			for (int val = 0; val <= 1; val++){
				int c,cv;
				if (And[i]){
					c = v1 && v2;
					cv = v1 || v2;
				} else {
					c = v1 || v2;
					cv = v1 && v2;
				}
				int t = d[i * 2][v1] + d[i * 2 + 1][v2];
				if (c != val){
					if (can[i] && cv == val)
						t++;
					else
						continue;
				}
				if (t < d[i][val])
					d[i][val] = t;
			}
		}
		if (d[1][v] <= n)
			printf("Case #%d: %d\n", ti, d[1][v]);
		else
			printf("Case #%d: IMPOSSIBLE\n", ti);
	}
	return 0;
}