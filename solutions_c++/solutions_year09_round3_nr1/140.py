#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

char buf[201];

int main()
{
	int T;
	int unassigned[] = {0, 2, 3, 4, 5, 6, 7, 8, 9};

	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		set<char> symbols;
		map<char, int> values;

		scanf("%s", buf);
		int len = strnlen(buf, 200);

		for (int i = 0; i < len; ++i)
			symbols.insert(buf[i]);

		int radix = max((int)(symbols.size()), 2);

		values[buf[0]] = 1;

		int j = 0;
		for (int i = 1; i < len; ++i)
			if (values.find(buf[i]) == values.end())
				values[buf[i]] = unassigned[j++];

		long long num = 0;
		long long r = 1;
		for (int i = len-1; i >= 0; i--)
		{
			num += r * values[buf[i]];
			r *= radix;
		}

		printf("Case #%d: %lld\n", t, num);
	}

	return 0;
}
