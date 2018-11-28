#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int f[5000][2], fn=0;

int cmp(const void *p, const void *q)
{
	if( ((int *)p)[0] != ((int *)q)[0] )
		return ((int *)p)[0] - ((int *)q)[0];
	else
		return ((int *)p)[1] - ((int *)q)[1];
}

int solve(int a, int b)
{
	int i, j, k;
	int l;
	int res = 0;
	int r, count;
	char s[20];
	
	sprintf(s,"%d",a);

	l = strlen(s) - 1;

	fn=0;
	for(i=a; i<=b; i++)
	{
		sprintf(s, "%d", i);
		for(j=1;j<=l;j++)
		{
			s[l+j] = s[j-1];
			s[l+j+1] = '\0';

			sscanf(&s[j], "%d", &r);
			if (r>=a && r<=b && r!=i)
			{
				res++;
				f[fn][0] = i < r? i : r;
				f[fn][1] = i < r? r : i;
				fn++;
			}
		}
	}
	
	qsort(f,fn,sizeof(f[0]),cmp);
	count=0;
	if (fn>0) count=1;
	else count=0;
	for(i=1;i<fn;i++)
	{
		if(f[i][0]!=f[i-1][0] || f[i][1]!=f[i-1][1])
			count++;
	}

	return count;
}

int main()
{
	int t, test = 1;
	int a, b;
	int res;
	scanf("%d", &t);
	while(t--)
	{
		scanf("%d%d", &a, &b);
		res = solve(a, b);
		printf("Case #%d: %d\n", test++, res);
	}
	return 0;
}