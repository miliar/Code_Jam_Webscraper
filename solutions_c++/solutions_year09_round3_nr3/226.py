#include <stdio.h>
#include <algorithm>
using namespace std;
#define N 110
#define M 100000000
int m[N], u[N];
int main()
{
	int i, j, k, n, t, ts, r, q;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &n, &q), i=0; i<q; scanf("%d", &m[i]), m[i]--, i++);
		for(r=M; ; )
		{
			for(i=0; i<n; u[i]=1, i++);
			for(k=0, i=0; i<q; i++)
			{
				for(j=m[i]-1; j>=0 && u[j]; k++, j--);
				for(j=m[i]+1; j<n && u[j]; k++, j++);
				u[m[i]]=0;
			}
			if(k<r) r=k;
			if(!next_permutation(m, m+q)) break;
		}
		printf("Case #%d: %d\n", t+1, r);
	}
	return 0;
}