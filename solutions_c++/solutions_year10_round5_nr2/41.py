#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)>0?(x):-(x))
#define Bint long long
using namespace std;
Bint L;
int n;
int d[100], c[100000];
deque<int> qu;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	int i, j, k, M;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%lld%d",&L,&n);
		for (i = 0; i < n; i++) scanf("%d",&d[i]);
		M = 0; for (i = 0; i < n; i++) M = max(d[i],M);
		memset(c,-1,sizeof(c));
		qu = deque<int>();
		qu.push_back(0); c[0] = 0;
		while (!qu.empty()) {
			i = qu.front(); qu.pop_front();
			for (j = 0; j < n; j++) {
				k = i+d[j];
				if (k < M) {
					if (c[k] == -1 || c[k] > c[i]+1) {
						qu.push_back(k); c[k] = c[i]+1;
					}
				}
				else {
					k -= M;
					if (c[k] == -1 || c[k] > c[i]) {
						qu.push_front(k); c[k] = c[i];
					}
				}
			}
		}
		if (c[L%M] == -1) printf("IMPOSSIBLE\n");
		else printf("%lld\n",L/M+c[L%M]);
	}
	return 0;
}