#include <vector>     
#include <map>     
#include <set>     
#include <deque>     
#include <algorithm>     
#include <utility>     
#include <sstream>     
#include <iostream>     
#include <cstdio>     
#include <cmath>     
#include <cstdlib>     

using namespace std;

#define SZ(a) ((int)(a).size())
#define pii pair<int,int>
#define mp make_pair
#define ll long long
template<class A, class B> A convert(B x) {stringstream s; s << x; A r; s >> r; return r;}

int solve(vector <string> q, set <string> e)
{
	int cnt = 0;
	set <string> eCopy = e;

	for (int i = 0; i < SZ(q); ++i)
	{
			if (e.find(q[i]) != e.end())
			{
				if (SZ(e) == 1) { ++cnt; e = eCopy; }
				e.erase(e.find(q[i]));
			}
	}
	return cnt;
}
int main()
{
	set<string> engines;
	vector <string> q;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testCnt;
	cin >> testCnt;
	for (int i = 1; i <= testCnt; ++i)
	{
		engines.clear();
		q.clear();
		int n;
		cin >> n;
		for (int j = 0; j < n; ++j)
		{
			string s = "";
			while (SZ(s) == 0)
			{
				getline(cin, s);
			}
			engines.insert(s);
		}
		cin >> n;
		for (int j = 0; j < n; ++j)
		{
			string s = "";
			while (s.length() == 0)
			{
				getline(cin, s);
			}
			q.push_back(s);
		}
		cout << "Case #" << i << ": " << solve(q, engines) << endl;
	}
	return 0;
}