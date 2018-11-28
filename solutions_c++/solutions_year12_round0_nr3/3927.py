#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

inline int toInt(string &s)
{
	int res = 0;
	for (int i= 0 ; i < s.size(); i++)
		res = res * 10 + s[i]-'0';
	return res;
}

inline string toString(int x)
{
	string res;

	while (x)
	{
		res.push_back(x%10 +'0');
		x /= 10;
	}

	reverse(res.begin(), res.end());
	return res;
}

int A, B;
int n;

set< int > S;

inline void solve(int testnum)
{
	scanf("%d%d", &A, &B);
	int ans = 0;
	for (int i = A; i <= B; i++)
	{
		string str = toString(i);
		S.clear();
		for (int q = 0; q < str.size(); q++)
		{
			str.insert(str.begin(), str[str.size()-1]);
			str.erase(str.size()-1, 1);

			if (str[0] != '0')
			{
				int newx = toInt(str);
				if (newx < A || newx > B)
					continue;
				if (newx > i)
					S.insert(newx);
			}
		}

		ans += S.size();
	}

	printf("Case #%d: %d\n", testnum + 1, ans);
};


int main()
{
	freopen("input.txt","r", stdin);
	freopen("output.txt","w", stdout);

	scanf("%d", &n);

	for (int i= 0 ;i < n; i++)
	{
		solve(i);
	}
}