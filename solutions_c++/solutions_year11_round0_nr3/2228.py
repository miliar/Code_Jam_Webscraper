#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int  main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int i;
	for(i = 1; i<=T; i++)
	{
		int N;
		scanf("%d", &N);
		int sum_ = 0;
		int j;
		vector<int> v;
		int a;
		for(j = 0; j<N; j++)
		{
			scanf("%d", &a);
			v.push_back(a);
			sum_^=a;
		}
		if(sum_)
		{
			printf("Case #%d: %s\n", i, "NO");
			continue;
		}
		else
		{
			sort(v.begin(), v.end());
			int sum = 0;
			for(j = 1; j<N; j++)
			{
				sum+=v[j];
			}
			printf("Case #%d: %d\n", i, sum);
		}
	}
	return 0;
}