#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define mp make_pair
#define pb push_back

typedef long long lint;
typedef vector<int> vi;
typedef vector<string> vs;
const int INF = 0x7fffffff;

// max surprise mark = (score + 4) / 3
// max not-surprise mark = (score + 2) / 3

int Solution()
{
	int n, s, p;
	cin >> n >> s >> p;
	vi cnt(31, 0);
	for(int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		cnt[x] ++;
	}

	int res = 0;
	for(int i = 30; i > 0; --i)
	{
		if((i + 2) / 3 >= p)
			res += cnt[i];
		else if ((i + 4) / 3 >= p)
		{
			int now = min(s, cnt[i]);
			res += now;
			s -= now;
		}
	}
	if(p == 0)
		res += cnt[0];
	cout << res;

	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	int n;
	cin >> n;
	getchar();
	for(int i = 1; i <= n; ++i)
	{
		printf("Case #%d: ", i);
		Solution();
		printf("\n");
	}
	return 0;
}
