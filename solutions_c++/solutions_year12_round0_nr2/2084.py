#include <stdio.h>
#include <algorithm>
using namespace std;

int t,T;
int n;
int a[1000];
int s;
int p;
int i;
int r;

int main()
{
	int k,m;

	freopen("D:\\B-large.in", "r", stdin);
	freopen("D:\\B-large.out", "w", stdout);
	
    scanf("%d", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d%d%d", &n, &s, &p);

		r=0;
		k=0;
		m=0;
		for (i = 0; i<n; i++)
		{
			scanf("%d", &a[i]);
		}
		/*sort(a, a+n);
		reverse(a, a+n);*/

		for (i=0; i<n; i++)
		{
			if (a[i]>=p+max(p-1, 0)*2)
			{
				k++;
			}
			else
			{
				if (a[i]>=p + max(p-2, 0)*2)
				{
					m++;
				}
			}
		}
		printf("Case #%d: %d\n", t, k+min(m,s));
	}

	return 0;
}

/*
1
2 1 1 8 0
*/