#include <stdio.h>
#include <algorithm>

int T, n, i, j, ans;

int a[100];
char str[100][100];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int cas=0;
	scanf("%d", &T);
while (T--)
{
	scanf("%d", &n);
	for (i=0; i<n; i++)
	  scanf("%s", str[i]);
	for (i=0; i<n; i++)
	{
		for (j=n-1; j>=0; j--)
		  if (str[i][j]=='1') break;
		a[i]=j;  
	}
	
	
	ans=0;
	for (i=0; i<n-1; i++)
	{
		for (j=i; j<n; j++)
		  if (a[j]<=i) break;
		while (j>i)
		{
			swap(a[j], a[j-1]);
			j--;
			ans++;
		}
		  
	}
	printf("Case #%d: %d\n", ++cas, ans);
}
	return 0;
}
