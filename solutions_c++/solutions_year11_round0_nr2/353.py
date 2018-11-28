#include <iostream>
#include <string>

using namespace::std;

char map[256][256];
bool flag[256][256];

void work()
{
	bool find;
	int n, i;
	char ch, ch1, ch2, ch3;
	string s;

	memset(map, -1, sizeof(map));
	memset(flag, false, sizeof(flag));
	for (scanf("%d", &n); n; --n)
	{
		scanf("%c%c%c%c", &ch1, &ch1, &ch2, &ch3);
		map[ch1][ch2] = map[ch2][ch1] = ch3;
	}
	for (scanf("%d", &n); n; --n)
	{
		scanf("%c%c%c", &ch1, &ch1, &ch2);
		flag[ch1][ch2] = flag[ch2][ch1] = true;
	}
	s = "";
	for (scanf("%d%c", &n, &ch); n; --n)
	{
		scanf("%c", &ch);
		if (s != "" && map[s[s.size() - 1]][ch] != -1) s[s.size() - 1] = map[s[s.size() - 1]][ch];
		else
		{
			find = false;
			for (i = 0; i < s.size(); ++i)
				if (flag[s[i]][ch]) 
				{
					s = "";
					find = true;
					break;
				}
			if (!find) s += ch;
		}
	}
	printf("[");
	for (i = 0; i + 1< s.size(); ++i)
		cout << s[i] << ", ";
	if (s.size()) cout << s[s.size() - 1];
	cout << "]" << endl;
}

int main()
{
	int test, t;

	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (scanf("%d", &test), t = 1; t <= test; ++t)
	{
		printf("Case #%d: ", t);
		work();
	}

	return 0;
}