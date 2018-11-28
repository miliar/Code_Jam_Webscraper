#include <cstdio>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

bool intersec(pair<int,int>& x, pair<int,int>& y)
{
	return (x.first > y.first != x.second > y.second);
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n;
		scanf("%d", &n);
		vector<pair<int,int> > vec(n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d %d", &vec[i].first, &vec[i].second);
		}
		int res = 0;
		for (int i = 0; i < n-1; ++i)
		{
			for (int j = i+1; j < n; ++j)
			{
				if ( intersec(vec[i], vec[j]) )
				{
					res++;
				}
			}
		}

		printf("Case #%d: %d\n", t+1, res);

	}



	return 0;
}