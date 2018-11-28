#include <stdio.h>

int cases, n, m[40], res;

void jump(int pos, int r)
{
	// printf("%d %d\n", pos, r);
	if (r>=res) return;
	if (pos==n) { res=r; return; }
	for(int i=pos; i<n; i++)
		if (m[i]<=pos)
		{
			int dummy=m[i];
			for(int j=i; j>pos; j--)
				m[j]=m[j-1];
			m[pos]=dummy;
			jump(pos+1, r+i-pos);
			for(int j=pos; j<i; j++)
				m[j]=m[j+1];
			m[i]=dummy;
		}
}

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		scanf(" %d", &n);
		for(int i=0; i<n; i++)
		{
			m[i]=0;
			for(int j=0; j<n; j++)
			{
				char dummy;
				scanf(" %c", &dummy);
				if (dummy=='1') m[i]=j;
			}
		}
		res=1000000;
		jump(0, 0);
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}
