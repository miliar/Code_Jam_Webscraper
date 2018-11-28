#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


int v[100], x[100];
vector<int> a;
bool good[100];


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);
	for(int test = 0; test < T; test++)
	{
		int n, k, b, t;
		a.clear();
		memset(good, false, sizeof(good));
		scanf("%d%d%d%d", &n, &k, &b, &t);
		for(int i = 0; i < n; i++)
			scanf("%d", &x[i]);
		for(int i = 0; i < n; i++)
			scanf("%d", &v[i]);
		for(int i = 0; i < n; i++)
			if(b - x[i] <= t * v[i])
				good[i] = true;
		for(int i = 0; i < n; i++)
			if(good[i])
			{
				int X = 0;
				for(int j = i + 1; j < n; j++)
					if(!good[j] && ((b - x[i]) * v[j]) < ((b - x[j]) * v[i]))
						X++;
				a.push_back(X);
			}
		sort(a.begin(), a.end());
		printf("Case #%d: ", test + 1);
		if(a.size() < k)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			int ans = 0;
			for(int i = 0; i < k; i++)
				ans += a[i];
			printf("%d\n", ans);
		}
	}
}