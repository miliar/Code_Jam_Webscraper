#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

#include <algorithm>
#include <set>
#include <stack>
#include <vector>
#include <queue>

#define MAXN 10000
#define FOR(A, B) for(A=0; A<B; A++)

using namespace std;

int d[MAXN+1], l[MAXN], D, n;
int q[MAXN+1];

int main(int argc, char* argv[])
{
	int i,j,k,m,o,a,b,x,y,z,t,T;
	scanf("%d", &T);
	FOR(t, T) {
		scanf("%d", &n);
		FOR(i, n) {
			q[i] = -1;
			scanf("%d %d", d+i, l+i);
		}
		q[n] = -1;
		scanf("%d", &D);
		d[n] = D;
		for(j = 1; j <= n; j++) if(d[j] <= d[0]+min(d[0], l[0])) q[j] = min(d[j]-d[0], l[j]);
		for(i = 1; i < n; i++)
		{
			for(j = i+1; j <= n; j++)
			{
				if(q[j] == -1 && d[j] <= d[i]+q[i]) q[j] = min(d[j]-d[i], l[j]);
			}
		}
		printf("Case #%d: ", t+1);
		if(q[n] == -1) printf("NO");
		else printf("YES");

		printf("\n");
	}
	return 0;
}