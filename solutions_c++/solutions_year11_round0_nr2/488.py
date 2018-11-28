#include <iostream>
#include <string>
using namespace std;

char comb[128][128];
bool flag[128][128];
int c, d, n;
char stack[103];
string s;

void init()
{
	memset(comb, 0, sizeof(comb));
	for (cin >> c; c && (cin >> s); --c) comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
	memset(flag, 0, sizeof(flag));
	for (cin >> d; d && (cin >> s); --d) flag[s[0]][s[1]] = flag[s[1]][s[0]] = 1;
}

void work()
{
	int i, j, k;

	cin >> n >> s;
	for (i = j = 0; i < s.size(); ++i)
	{
		if (j && comb[s[i]][stack[j]]) stack[j] = comb[s[i]][stack[j]];
		else
		{
			for (k = 1; k <= j; ++k)
				if (flag[s[i]][stack[k]]) break;
			if (k <= j) j = 0;
			else stack[++j] = s[i];
		}
	}
	for (i = 1; i <= j; ++i)
	{
		cout << stack[i];
		if (i < j) cout << ", ";
	}
	cout << "]" << endl;
}

int main()
{
	int i, t;

//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	for (cin >> t, i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": [";
		init();
		work();
	}
	return 0;
}