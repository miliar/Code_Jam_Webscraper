#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
using namespace std;

int d[50];

void runtest()
{
	int n;
	scanf("%d\n", &n);
	for (int i = 1; i <= n; i++)
	{
		int z=1;
		for (int j = 1; j <= n; j++)
		{
			char c;
			scanf("%c", &c);
			if (c=='1') z=j;
			d[i]=z;
		}
		scanf("\n");
	}

	int tot=0;

	for (int i = 1; i <= n; i++)
	{
		int j = i;
		while (d[j] > i)
		{
			j++;
		}
		tot += (j-i);
		if (j>i)
		{
			int z = d[j];
			for (int k=j;k>i;k--)
			{
				d[k]=d[k-1];
			}
			d[i]=z;
		}
	}






	printf(" %d\n", tot);
}


int main()
{
	freopen("C:\\a1.txt", "r", stdin);
	freopen("C:\\a1out.txt", "w", stdout);

	int tests;
	scanf("%d\n", &tests);

	for (int te = 1; te <= tests; te++)
	{
		printf("Case #%d:", te);
		runtest();
	}

	return 0;
}
