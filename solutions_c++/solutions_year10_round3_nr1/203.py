#include <iostream>
using namespace std;

pair<int,int> a[10000];
int n;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++) 
	{
		scanf("%d", &n);
	//	printf("%d\n", n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d", &a[i].first, &a[i].second);
	//		printf("%d %d\n", a[i].first, a[i].second);
		}

		int res = 0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if((a[i].first < a[j].first && a[i].second > a[j].second) ||
				   (a[i].first > a[j].first && a[i].second < a[j].second))
				{
					res++;
				}
			}
		}
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}