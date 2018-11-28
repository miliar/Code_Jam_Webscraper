#include <stdio.h>
#include <string.h>


bool is_debug = false;
int cas = 0;
int	T;
int	n;

int a[1001], b[1001];


int main()
{
	if (!is_debug)
	{
		freopen("in.in", "r", stdin);
		freopen("out.out", "w", stdout);
	}

	int i, j, k;

	scanf("%d", &T);	
	while (T--)
	{		
		scanf("%d", &n);
		for (i=0; i<n; i++)
			scanf("%d %d", a+i, b+i);

		int cnt = 0;
		for (i=0; i<n; i++)
			for (j=i+1; j<n; j++)
			{
				if (a[i] < a[j] && b[i] > b[j])
					cnt++;
				if (a[i] > a[j] && b[i] < b[j])
					cnt++;
			}

		printf("Case #%d: %d\n", ++cas, cnt);		
	}
	return 0;
}