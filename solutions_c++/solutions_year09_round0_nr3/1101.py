#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <iostream>

using namespace std;

int res[510][510];
char s[510];
const char welcome[] = "welcome to code jam";

int getAns(int i, int j)
{
	if (i == strlen(s))
	{
		if (j < strlen(welcome))
			return 0;
		else if (j == strlen(welcome))
			return 1;
	}
	else if (j == strlen(welcome))
	{
		return 1;
	}
	else if (res[i][j] >= 0)
		return res[i][j];
	else
	{
		int r, t;
		int count = 0;
		for (r = i; s[r] != 0; r++)
		{
			if (s[r] == welcome[j])
				count = (getAns(r + 1, j + 1) + count) % 10000 ;
		}
		res[i][j] = count;
	}
	return res[i][j];
}

int main()
{
	freopen("3.in", "r", stdin);
	freopen("3.out", "w", stdout);
	int N;

	scanf ("%d", &N);
	getchar();
	int t;
	int i, j;
	for (t = 1; t <= N; t++)
	{
		gets(s);
		for (i = 0; i <= strlen(s); i++)
		{
			for (j = 0; j <= strlen(welcome); j++)
			{
				res[i][j] = -1;
			}
		}
		printf ("Case #%d: %04d\n", t,  getAns(0, 0));
	}

	return 0;
}