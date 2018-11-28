#include <cstdio>
#include <cstring>
#include <vector>

#define WELCOME "welcome to code jam"
#define MODULUS 10000

using namespace std;

int main()
{
	const int LEN = sizeof(WELCOME) - 1;
	static const char welcome[] = WELCOME;
	vector<vector<int> > occurrences('z' + 1);
	for (int i = 0; i < LEN; ++i)
		occurrences[welcome[i]].push_back(i);
	int n;
	scanf("%d ", &n);
	for (int idx = 0; idx < n; ++idx)
	{
		int count[LEN + 1];
		count[0] = 1;
		for (int i = 1; i <= LEN; ++i)
			count[i] = 0;
		while (true)
		{
			int c = getchar();
			if (c == '\n')
				break;
			for (int i = 0; i < (int)occurrences[c].size(); ++i)
			{
				int j = occurrences[c][i];
				count[j + 1] += count[j];
				if (count[j + 1] >= MODULUS)
					count[j + 1] -= MODULUS;
			}
		}
		printf("Case #%d: %04d\n", idx + 1, count[LEN]);
	}
	return 0;
}
