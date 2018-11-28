#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

int c, d, n;
char s[] = "QWERASDF";

bool opposite[10][10];
char tform[10][10];
char res[1100000];

int have[10];

int code(char c)
{
	for (int i = 0; i < 8; i ++)
		if (s[i] == c) return i;
}

void solve(int test)
{
	for (int i = 0; i < 8; i ++)
		for (int j = 0; j < 8; j ++)
		{
			opposite[i][j] = false;
			tform[i][j] = 0;
		}
	cin >> c;
	for (int i = 0; i < c; i ++)
	{
		string s;
		cin >> s;
		int u = code(s[0]), v = code(s[1]);
		tform[u][v] = tform[v][u] = s[2];
	}
	cin >> d;
	for (int i = 0; i < d; i ++)
	{
		string s;
		cin >> s;
		int u = code(s[0]), v = code(s[1]);
		opposite[u][v] = opposite[v][u] = true;
	}

	cin >> n;
	string s;
	cin >> s;

	int t = 0;
	for (int i = 0; i < 8; i ++)
		have[i] = 0;
	for (int i = 0; i < n; i ++)
	{
		t ++;
		res[t] = s[i];
		have[code(res[t])] ++;
		if (t >= 2 && tform[code(res[t - 1])][code(res[t])])
		{
			char c = tform[code(res[t - 1])][code(res[t])];
			have[code(res[t - 1])] --;
			have[code(res[t])] --;
			t --;
			res[t] = c;
		} else
		{
			bool good = true;
			for (int i = 0; i < 8 && good; i ++)
				for (int j = i + 1; j < 8 && good; j ++)
					if (have[i] && have[j] && opposite[i][j]) good = false;
			if (!good)
			{
				t = 0;
				for (int i = 0; i < 8; i ++)
					have[i] = 0;
			}
		}
	}

	printf("Case #%d: [", test);
	for (int i = 1; i + 1 <= t; i ++)
		printf("%c, ", res[i]);
	if (t != 0)
		printf("%c", res[t]);
	printf("]\n");
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++)
		solve(i);
	return 0;
}