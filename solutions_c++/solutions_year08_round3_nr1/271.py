#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int numCase;
	int t;
	int p, k, l;
	__int64 ans = 0;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	vector<int> freq;
	scanf("%d", &numCase);
	for(int cases = 0; cases < numCase; cases++)
	{
		ans = 0;
		freq.clear();
		scanf("%d%d%d", &p, &k, &l);
		for(int i = 0; i < l; i++)
		{
			scanf("%d", &t);
			freq.push_back(t);
		}
		sort(freq.begin(), freq.end());

		t = freq.size();
		for(int i = 0; i < p; i++)
		{
			for(int j = 0; j < k; j++)
			{
				if(t > 0)
				{
					ans += freq[t - 1] * (i + 1);
					t--;
				}
				else
					goto pend;
			}
		}
pend:
		cout << "Case #" << cases + 1 << ": " << ans << endl;
	}

	return 0;
}