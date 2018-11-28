#include	<cstdio>
#include	<iostream>
char	ss[100][101];
char	sss[101];
int		js[100];
int main()
{
	int		n , s, q, i, j, k, min, t;
	//freopen("A-large.in", "r", stdin);
	//freopen("out.txt", "w", stdout);
	scanf("%d", &n);
	for (i=1; i<=n; ++i) {
		memset(js, 0, sizeof(js));
		scanf("%d", &s);
		gets(sss);
		for (j=0; j<s; ++j) gets(ss[j]);
		scanf("%d", &q);
		gets(sss);
		t=0;
		min=0;
		for (j=0; j<q; ++j) {
			gets(sss);
			for (k=0; k<s; ++k)
				if (strcmp(sss, ss[k])==0) {
					if (js[k]==0) t++;
					js[k]++;
					if (t==s) { memset(js, 0, sizeof(js)); min++; t=1; js[k]=1; }
				}
		}
		printf("Case #%d: %d\n", i, min);
	}
}
