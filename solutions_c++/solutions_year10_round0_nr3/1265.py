#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	freopen("C.in", "r", stdin);	
	freopen("C.out", "w", stdout);
	int i, ii, j, g[1005][4]={{0}}, r, k, n, c, rr, kk, st, q, p;
	long long m;
	scanf("%d\n", &c);
	for(ii=1; ii<=c; ii++)
	{
		m=0;
		scanf("%d %d %d\n", &r, &k, &n);
		for(i=1; i<=n; i++)
		{
			scanf("%d", &g[i][1]);
			g[i][0]=i+1;
		}
		g[n][0]=1;
		rr=0;
		q=0;
		for(i=1; i<=n; i++)
		{
			st=i;
			kk=g[i][1];
			j=g[i][0];
			while(kk+g[j][1]<=k && j!=st)
			{
				kk+=g[j][1];
				j=g[j][0];
			}
			g[i][2]=j;
			g[i][3]=kk;
		}
		i=1;
		while(rr<r)
		{
			rr++;
			m+=g[i][3];
			i=g[i][2];
		}
		cout << "Case #" << ii << ": " << m << '\n';
	}
	return 0;
}