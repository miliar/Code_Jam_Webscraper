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

int len;
int ten[] = {1, 10, 100, 1000, 10000, 100000, 1000000};

inline int shift(int n, int l)
{
	return (n % ten[l]) * ten[len - l] + n / ten[l];
}

int Solution()
{
	int a, b;
	cin >> a >> b;

	int x = a;
	len = 0;
	while(x)
	{
		len ++; x /= 10;
	}

	int res = 0;
	for(int i = a; i <= b; ++i)
	{
		set<int> s;
		for(int j = 1; j < len; ++j)
		{
			int now = shift(i, j);
			if(i < now && now <= b)
				s.insert(now);
		}
		res += s.size();
	}
	cout << res;
	return 0;
}

#define debug 1

int main()
{
#ifdef debug
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
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
