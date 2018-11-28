#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d ", &t);
	string phrase = "welcome to code jam";

	for (int ti = 0; ti < t; ti++)
	{
		char buff[512];
		gets(buff);
		size_t size = strlen(buff);

		vector<int> d(phrase.size() + 1, 0);
		d[0] = 1;

		for (size_t i = 0; i < size; i++)
		{
			for (size_t j = d.size(); j > 0; j--)
			{
				if (buff[i] == phrase[j - 1])
				{
					d[j] += d[j - 1];
					d[j] %= 10000;
				}
			}
		}
		printf("Case #%d: %04d\n", ti + 1, d[phrase.size()]);
	}
	return 0;
}
