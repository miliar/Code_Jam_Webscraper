#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int gcd(int a, int b)
{
	while(b != 0)
	{
		int c = a % b;
		a = b;
		b = c;
	}
	return a;
}

int main()
{
	freopen("d:\\downloads\\B-small-attempt0.in", "r", stdin);
	freopen("d:\\downloads\\output.txt", "w", stdout);

	int z;
	scanf("%d", &z);
	for(int c = 0; c < z; ++c)
	{
		int n;
		scanf("%d", &n);
		vector<int> inp;
		while(n--)
		{
			int t;
			scanf("%d", &t);
			inp.push_back(t);
		}
		sort(inp.begin(), inp.end());
		int g = inp[1] - inp[0];
		for(int i = 1; i < inp.size(); ++i)
		{
			int gap = inp[i] - inp[i-1];
			g = gcd(g, gap);
		}

		if (inp[0] % g != 0)
			printf("Case #%d: %d\n", c + 1, g - (inp[0] % g));
		else
			printf("Case #%d: %d\n", c + 1, 0);
	}
}
