#include<stdio.h>
#include<string.h>
int a[111][1111], n, q;
char s[111][1111], s1[1111][111];
int min(int aa, int bb)
{
	if(aa<bb)
		return aa;
	return bb;
}

int func(int x, int y)
{
	if(a[x][y]!=222222222)
		return a[x][y];
	int i;
	if(y>=q)
		return 0;
	if(strcmp(s[x], s1[y])==0)
	{
		int m=222222222;
		for(i=0; i<n; i++)
			if(i!=x)
				m=min(m, func(i, y));
		a[x][y]=m+1;
		return a[x][y];
	}
	a[x][y]=func(x, y+1);
	return a[x][y];
}



int main()
{
	freopen("A-large.in", "r", stdin);
		freopen("a.ans", "w", stdout);

	int res, test, t, i, j;
	scanf("%d\n", &test);
	for(t=0; t<test; t++)
	{
		scanf("%d\n", &n);
		for(i=0; i<n; i++)
			//scanf("%s", s[i]);
			gets(s[i]);

		scanf("%d\n", &q);
		for(i=0; i<q; i++)
			//scanf("%s", s1[i]);
			gets(s1[i]);
		for(i=0; i<=n; i++)
			for(j=0; j<=q; j++)
				a[i][j]=222222222;
		res=222222222;
		for(i=0; i<n; i++)
			res=min(res, func(i, 0));
	//	for(i=0; i<n; i++)
	//	{
	//		for(j=0; j<n; j++)
	//			printf("%d ", a[i][j]);
	//		puts("");
	//	}
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}

