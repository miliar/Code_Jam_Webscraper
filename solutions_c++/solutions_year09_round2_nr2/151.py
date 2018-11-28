const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;
const string FILENAME = "gcj";

int nn,n;
char s[1000];

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &nn);
	gets(s);
	for (int ii=1; ii<=nn; ++ii)
	{
		printf("Case #%d: ", ii);
		gets(s);
		int m = (int)strlen(s);
		if (next_permutation(&s[0], &s[m]))
			puts(s);
		else
		{
			int t[10];
			memset(t, 0, sizeof t);
			for (int i=0; i<m; ++i)
				++t[s[i]-'0'];
			int len = 0;
			for (int i=1; i<10; ++i)
				if (t[i])
				{
					--t[i];
					s[len++] = '0'+i;
					s[len++] = '0';
					break;
				}
			for (int i=0; i<10; ++i)
				for (int j=0; j<t[i]; ++j)
					s[len++] = '0'+i;
			s[len] = 0;
			puts(s);
		}

	}

	return 0;
} 