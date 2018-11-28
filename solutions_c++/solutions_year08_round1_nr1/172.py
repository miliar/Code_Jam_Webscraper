#include <stdio.h>
#include <algorithm>
using namespace std;

int tests, w;
__int64 a[1024], b[1024];
__int64 cur, r1, r2;
int n;


int main () {
	int i;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	for (scanf("%d", &tests), w=1; w<=tests; w++) {
		scanf("%d", &n);
		for (i=1; i<=n; i++)
			scanf("%I64d", &a[i]);
		for (i=1; i<=n; i++)
			scanf("%I64d", &b[i]);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		reverse(b+1,b+n+1);

//
		r1=0;
		for (i=1; i<=n; i++)
			r1+=a[i]*b[i];

/*
		r2=r1;
		do {
			cur=0;
			for (i=1; i<=n; i++)
				cur+=a[i]*b[i];
			r2=min(cur,r2);
		} while (next_permutation(a+1,a+n+1));
*/
		printf("Case #%d: ", w);
		//if (r1!=r2)
			//printf("SHIT!!!\n");
		//else
			printf("%I64d\n",r1);
	}
	return 0;
}