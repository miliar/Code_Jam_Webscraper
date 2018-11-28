#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

string str;

short form[26][26];
bool opp[26][26];
int count[26];

int stsize;
int st[110];


char tolower(char c)
{
	if ('A' <= c && c <= 'Z')
		c = c - 'A' + 'a';
	return c;
}

void init()
{
	for (int i = 0; i < 26; ++i)
		for (int j = 0; j < 26; ++j)  {
			form[i][j] = -1;
			opp[i][j] = false;
		}
	for (int i = 0; i < 26; ++i)
		count[i] = 0;
	stsize = 0;
}

void add(short cur)
{
	if (stsize == 0)
	{
		st[stsize++] = cur;
		count[cur]++;
	}
	else
	{
		int curtop = st[stsize-1];
		if (form[cur][curtop] != -1)
		{
			count[curtop]--;
			stsize--;
			add(form[cur][curtop]);
		}
		else
		{
			for (int i = 0; i < 26; ++i)
			{
				if (opp[cur][i] && count[i])
				{
					stsize = 0;
					for (int j = 0; j < 26; ++j)
					{
						count[j] = 0;
					}
					return;
				}
			}
			count[cur]++;
			st[stsize++] = cur;
		}
	}
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		init();

		int c;
		cin >> c;
		for (int i = 0; i < c; ++i)
		{
			cin >> str;
			short x = tolower(str[0]) - 'a';
			short y = tolower(str[1]) - 'a';
			short z = tolower(str[2]) - 'a';
			form[x][y] = form[y][x] = z;
		}

		int d;
		cin >> d;
		for (int i = 0; i < d; ++i)
		{
			cin >> str;
			short x = tolower(str[0]) - 'a';
			short y = tolower(str[1]) - 'a';
			opp[x][y] = opp[y][x] = true;
		}

		int n;
		cin >> n;
		cin >> str;
		for (int i = 0; i < n; ++i)
		{
			str[i] = tolower(str[i]);
			str[i] -= 'a';
		}
		for (int i = 0; i < n; ++i)
		{
			add(str[i]);
		}
		cout << "Case #" << t << ": " << "[";
		for (int i = 0; i < stsize; ++i)
		{
			if (i) cout << ", ";
			cout << char(st[i] + 'A');
		}
		cout << "]" << endl;
	}
	return 0;
}