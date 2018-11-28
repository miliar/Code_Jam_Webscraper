
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int caseNum;
	long long ans;
	int r, k, n;
	int x, y, tmp;
	long long z;
	int num[1000];
	int used[1000];
	long long tans[1000];

	cin >> caseNum;

	for (int crtCase=1; crtCase<caseNum+1; crtCase++)
	{
		cin >> r >> k >> n;
		z = 0;
		for (int i=0; i<n; i++)
		{
			cin >> num[i];
			z+=num[i];
		}

		if (z<=k)
		{
			ans = z*r;
		}
		else
		{
			memset(used,0,sizeof(used));
			x = 0;
			y = 0;
			ans = 0;

			while ((x != r)&&(used[y] == 0))
			{
				x++;
				used[y] = x;
				tans[y] = ans;
				z = 0;
				tmp = y;
				while ((z+num[y]<=k))
				{
					z += num[y];
					y++;
					if (y == n)
					{
						y = 0;
					}
				}
				ans += z;
			}

			z = (r-x)/(x+1-used[y]);
			x += z*(x+1-used[y]);
			ans += z*(ans-tans[y]);

			while (x != r)
			{
				x++;
				z = 0;
				while (z+num[y] <= k)
				{
					z += num[y];
					y++;
					if (y == n)
					{
						y = 0;
					}
				}
				ans += z;
			}
		}

		cout << "Case #" << crtCase << ": ";
		cout << ans << endl;
	}
	return 0;
}
