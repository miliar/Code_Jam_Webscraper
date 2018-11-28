#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct bit_s
{
	string data;
	int last_c;
};

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		vector<bit_s> bit;
		int N;
		scanf("%d", &N);
		int i;
		for (i = 0;i < N;i++)
		{
			bit_s b;
			char buf[51];
			scanf("%s", buf);
			b.data = string(buf);
			int j;
			for (j = b.data.size() - 1;j >= 0;j--)
			{
				if (b.data[j] == '1')
					break;
			}
			b.last_c = j;

			bit.push_back(b);
		}

		int j;
		int ans = 0;
		for (i = 0;i < N;i++)
		{
			for (j = i;j < N;j++)
			{
				if (bit[j].last_c <= i)
					break;
			}
			int k;
			for (k = j;k > i;k--)
			{
				ans++;
				swap(bit[k], bit[k - 1]);
			}
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
