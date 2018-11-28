#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;

void Test(int n)
{
	VI d;
	int last = 0;
	map<int, int> s;
	set<int> ans;
	for (int yy = 0; yy < 100; yy++)
	{		
		for (last = 0; last < d.size(); last++)
		{
			if (d[last] == 0)
				break;
		}
		if (last >= d.size())
			d.resize(min(last + 1, n), 0);
		cout << last << '\t';
		for (int i = 0; i < d.size(); i++)
		{
			cout << d[i];
		}
		cout << endl;
		if (last == n)
			ans.insert(yy);
		s[d.size()] ++;
		for (int i = 0; i <= min(last, n - 1); i++)
		{
			d[i] = 1 - d[i];
		}		
	}
	for (map<int, int>::iterator it = s.begin(); it != s.end(); ++it)
	{
		//cout << it->first << ' ' << it->second << endl;
	}
	for(set<int>::iterator it = ans.begin(); it != ans.end(); ++it)
	{
		cout << *it << endl;
	}
}

bool Go()
{
	LL n, k;
	cin >> n >> k;
	LL add = 1 << n;
	LL first = add - 1;
	if (k < first)
		return 0;
	if (k == first)
	{
		return 1;
	}
	k -= first;
	return k % add == 0;
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "A-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif

	//Test(4);
	int t;
	scanf("%d", &t);
	for (int yy = 1; yy <= t; yy++)
	{
		printf("Case #%d: ", yy);
		printf("%s", Go() ? "ON" : "OFF");
		printf("\n");
	}
	return 0;
}