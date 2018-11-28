#include <stdio.h>
#define N 260
char s[N], m[N][N], u[N][N], r[N];
int main()
{
	int i, j, k, t, ts, n;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(i=0; i<N; i++)
			for(j=0; j<N; m[i][j]=0, u[i][j]=0, j++);
		for(scanf("%d", &n); n--; scanf("%s", s), m[s[0]][s[1]]=s[2], m[s[1]][s[0]]=s[2]);
		for(scanf("%d", &n); n--; scanf("%s", s), u[s[0]][s[1]]=1, u[s[1]][s[0]]=1);
		for(scanf("%d%s", &n, s), j=0, i=0; ; )
			if(j>=2 && m[r[j-2]][r[j-1]]) { r[j-2]=m[r[j-2]][r[j-1]]; j--; }
			else
			{
				for(k=0; k<j && !u[r[k]][r[j-1]]; k++);
				if(k<j) j=0;
				if(i==n) break;
				else r[j++]=s[i++];
			}
		for(printf("Case #%d: [", t+1), i=0; i<j-1; printf("%c, ", r[i]), i++);
		if(j>0) printf("%c", r[i]);
		printf("]\n");
	}
	return 0;
}