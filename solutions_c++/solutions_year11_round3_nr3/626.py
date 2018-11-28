#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> a;
int main()
{
	int t;
	int tp = 0;
	int i, j;
	 int temp;
	 int ans;
	 int n, l, h, ye;
	scanf("%d", &t);
	while(t--)
	{
		tp ++;
		a.clear();
		scanf("%d%d%d", &n, &l, &h);
		for(i=0; i<n; ++i)
		{
			scanf("%d", &temp);
			a.push_back(temp);
		}
		if(l <= 1)
		{
			ans = 1;
		}
		sort(a.begin(), a.end());
		ye = 0;
/*		else
		{
		        ye = 0;
			sort(a.begin(), a.end());
			ans = a[a.size()-1];
			for(i=1; ans*i<= h; ++i)
			{
				for(j=0; j<a.size(); ++j)
				{
					if((ans*i) % a[j] != 0)
					{
						break;
					}
				}
				if(j == a.size())
				{
					ans = ans*i;
					ye = 1;
					break;
				}
			}
		}*/
		if(ye == 0)
		{
			for(i=l; i<=h; ++i)
			{
				for(j=0; j<a.size(); ++j)
				{
					if(a[j]%i != 0 && i%a[j] != 0)
					{
						break;
					}
				}
//				printf(">>>for %d, j= %d %d\n", i, j, a.size());
				if(j == a.size())
				{
					ans = i;
					ye = 1;

					break;

				}
			}
		}


		printf("Case #%d: ", tp);
		if(ye == 0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", ans);
		}
	}
	return 0;
}

		
