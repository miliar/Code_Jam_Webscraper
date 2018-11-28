#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int	T,cs;
	int	n;
	int	k;
	vector <int> v1,v2;
	int	i,j,p,q;

	scanf("%d",&T);

	for(cs = 1; cs <= T; cs++)
	{
		scanf("%d",&n);

		v1.clear();
		v2.clear();

		for(i = 0; i < n; i++)
		{
			scanf("%d",&k);
			v1.push_back(k);
		}

		for(i = 0; i < n; i++)
		{
			scanf("%d",&k);
			v2.push_back(k);
		}

		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());

		i = 0, j = n - 1;
		p = 0, q = n - 1;

		long long m = 0,x,y;

		while(i <= j)
		{
			if(i == j)
				m += (long long)v1[i] * v2[p];
			else
			{
				x = (long long)v1[i] * v2[p] + (long long)v1[j] * v2[q];
				y = (long long)v1[i] * v2[q] + (long long)v1[j] * v2[p];

				if(x < y)
				{
					m += (long long)v1[i] * v2[p];
					p++;
				}
				else
				{
					m += (long long)v1[i] * v2[q];
					q--;
				}
			}

			i++;
		}

		printf("Case #%d: %lld\n",cs,m);
	}

	return 0;
}
