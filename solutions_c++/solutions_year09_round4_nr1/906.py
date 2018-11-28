#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <map>
#include <cstdio>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory>
#include <queue>
#include <sstream>

using namespace std;

typedef long double ld;
typedef long long int64;

#define forn(i,n) for(int i = 0; i < (int)n; i++)

deque<deque<int> > d;

int n;
int tests;

char buff[100];

int main(int argc, char * argv[])
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	cin >> tests;
	forn(test, tests)
	{
		int n;
		cin >> n;
		d = deque<deque<int> >(n, deque<int>(n, 0));
		for (int i = 0; i < n; i++)
		{
			string s;
			scanf("%s", buff);
			s = buff;
			for (int j = 0; j < n; j++)
				d[i][j] = s[j] - '0';
		}
		int ans = 0;
		while (d.size() > 1)
		{
			int res = -1;
			forn(i, d.size())
			{
				int idx = 0;
				forn(j, d.size())
					if (d[i][j] == 1)
						idx = j;
				if (idx == 0)
				{
					res = i;
					break;
				}
			}
			while (res > 0)
			{
				++ans;
				swap(d[res], d[res - 1]);
				--res;
			}
			d.pop_front();
			forn(i, d.size())
				d[i].pop_front();
		}
		cout << "Case #" << test + 1 << ": " << ans << endl;
	}

	return 0;
}

