#include <stdio.h>
#define N 5100
#define L 20
char m[N][L], s[N], u[L][30];
int main()
{
	int i, j, k, n, l, q, t, r;
	for(scanf("%d%d%d", &l, &n, &q), i=0; i<n; scanf("%s", m[i]), i++);
	for(i=0; i<q; printf("Case #%d: %d\n", i+1, r), i++)
	{
		scanf("%s", s);
		for(t=0, j=0; j<l; j++)
		{
			for(k=0; k<26; u[j][k]=0, k++);
			if(s[t]=='(')
				for(t++; s[t]!=')'; u[j][s[t]-'a']=1, t++);
			else u[j][s[t]-'a']=1;
			t++;
		}
		for(r=0, j=0; j<n; r+=k==l, j++)
			for(k=0; k<l && u[k][m[j][k]-'a']; k++);
	}
	return 0;
}