#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <cstring>
#include <string>

using namespace std;

const char ar[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z',
't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int n;
char s[1000100];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
	{
		gets(s);
		int m = strlen(s);
		for (int j = 0; j < m; j++)
		{
			if (s[j] == ' ')
			{
				continue;
			}
			s[j] = ar[s[j] - 'a'];
		}
		printf("Case #%d: %s\n", i + 1, s);
	}
	return 0;
}