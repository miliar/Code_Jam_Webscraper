#include <stdio.h>

int t, r, b, k, n;
char a[50][50];

int main()
{
	scanf(" %d", &t);
	for(int cs=1; cs<=t; cs++)
	{
		r=b=0;
		scanf(" %d %d", &n, &k);
		for(int i=n-1; i>=0; i--)
			for(int j=n-1; j>=0; j--)
				scanf(" %c", &a[j][i]);
		for(int i=0; i<n; i++)
		{
			int pos=0;
			for(int j=0; j<n; j++)
			{
				if (a[j][i]!='.')
				{
					a[pos][i]=a[j][i];
					if (j>pos) a[j][i]='.';
					pos++;
				}
			}
		}
#if 0
		for(int j=n-1; j>=0; j--)
		{
			for(int i=0; i<n; i++)
				printf("%c", a[j][i]);
			printf("\n");
		}
#endif
		for(int i=0; i<=n; i++)
			for(int j=0; j<=n; j++)
			{
				int r1, b1;
				if (j<=n-k)
				{
					r1=b1=1;
					for(int l=0; l<k; l++)
					{
						if (a[j+l][i]!='R') r1=0;
						if (a[j+l][i]!='B') b1=0;
					}
					if (r1) r++;
					if (b1) b++;
				}
				if (i<=n-k)
				{
					r1=b1=1;
					for(int l=0; l<k; l++)
					{
						if (a[j][i+l]!='R') r1=0;
						if (a[j][i+l]!='B') b1=0;
					}
					if (r1) r++;
					if (b1) b++;
				}
				if ((i<=n-k) && (j<=n-k))
				{
					r1=b1=1;
					for(int l=0; l<k; l++)
					{
						if (a[j+l][i+l]!='R') r1=0;
						if (a[j+l][i+l]!='B') b1=0;
					}
					if (r1) r++;
					if (b1) b++;
				}
				if ((i<=n-k) && (j>=k-1))
				{
					r1=b1=1;
					for(int l=0; l<k; l++)
					{
						if (a[j-l][i+l]!='R') r1=0;
						if (a[j-l][i+l]!='B') b1=0;
					}
					if (r1) r++;
					if (b1) b++;
				}
			}
		if (r && b) printf("Case #%d: Both\n", cs);
		if (r && !b) printf("Case #%d: Red\n", cs);
		if (!r && b) printf("Case #%d: Blue\n", cs);
		if (!r && !b) printf("Case #%d: Neither\n", cs);
	}
}
