#include <stdio.h>
#define N 510
#define L 19
char s[N], t[]="welcome to code jam";
int d[N][L+5];
int main()
{
	int i, j, n, ts, tst, mod=10000;
	for(gets(s), sscanf(s, "%d", &tst), ts=0; ts<tst; printf("Case #%d: %04d\n", ts+1, d[n][L]), ts++)
	{
		for(gets(s), n=0; s[n]; n++);
		for(i=0; i<=n; i++)
			for(j=0; j<=L; d[i][j]=0, j++);
		for(d[0][0]=1, i=1; i<=n; i++)
			for(j=0; j<=L; d[i][j]=((s[i-1]==t[j-1]?d[i-1][j-1]:0)+d[i-1][j])%mod, j++);
	}
	return 0;
}