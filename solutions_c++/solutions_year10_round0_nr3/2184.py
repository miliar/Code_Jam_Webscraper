#include <iostream>
using namespace std;

int r, k, n, g[10000005];

void work()
{
	scanf("%d %d %d", &r, &k, &n);
	for(int i=0; i<n; i++)
		scanf("%d", &g[i]);
	int Cnt = 0, cost = 0;
	int total = 0;
	for(int i=0, j=0; j<r; )
	{
		if(Cnt + g[i] <= k && total < n)
		{
			cost += g[i];
			Cnt += g[i];
			total++;
			i++;
			if(i >= n)
				i = 0;
		}
		else
		{
			Cnt = 0;
			total = 0;
			j++;
		}
	}
	cout << cost << endl;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int iCase=1; iCase<=T; iCase++)
	{
		printf("Case #%d: ", iCase);
		memset(g, 0, sizeof(g));
		work();
	}
	return 0;
}
