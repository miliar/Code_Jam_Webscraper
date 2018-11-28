#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>

#define all(x) (x).begin(),(x).end()
#define nmax 100

using namespace std;

int n,m;

char s[nmax][nmax];
char t[nmax][nmax];
bool solve()
{
	scanf("%d%d\n",&n,&m);
	for (int i = 0; i < n; i ++) 
		scanf("%s",s[i]);
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < m; j ++)
			t[i][j] = '.';
		t[i][m] = 0;
	}
	bool ok = 1;
	do 
	{
		ok = 1;
		for (int i = 0; (i < n) && ok; i ++)
			for (int j = 0; j < m; j ++)
			{
				if (s[i][j] == '#')
				{
					if ((s[i+1][j] != '#') || (s[i][j + 1] != '#') || (s[i+1][j+1] != '#'))
						return false;
					t[i][j] = '/';
					t[i][j+1] = '\\';
					t[i+1][j] = '\\';
					t[i+1][j+1] = '/';
					s[i][j] = s[i + 1][j] = s[i][j + 1] = s[i +1][j + 1] = '.';
					ok = false;
					break;
				}
			}
	}
	while (!ok);
	return 1;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		printf("Case #%d:\n", i);
		if (solve())
		{
			for (int j = 0; j < n; j ++)
				printf("%s\n", t[j]);
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}
