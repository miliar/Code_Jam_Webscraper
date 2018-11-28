#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
//#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

void Solve()
{
	int n;
	cin >> n;
	map<int, int> M;
	set<int> in;
	queue<int> q;
	for (int i = 0; i < n; i++)
	{
		int x, y;
		cin >> x >> y;
		M[x] = y;
		if (y > 1)
			q.push(x), in.insert(x);
	}
	int res = 0;
	while (!q.empty())
	{
		int x = q.front();
		q.pop();
		in.erase(x);
		if (M[x] <= 1)
		{
			continue;
		}
		int t = M[x] / 2;
		M[x - 1] += t;
		M[x + 1] += t;
		M[x] -= 2 * t;
		res += t;
		if (M[x - 1] >= 2 && !in.count(x - 1))
			q.push(x - 1), in.insert(x - 1);
		if (M[x + 1] >= 2 && !in.count(x + 1))
			q.push(x + 1), in.insert(x + 1);
	}
	for (map<int, int>::iterator it = M.begin(); it != M.end(); it++)
		if (it->second > 1)
		{
			cerr << "Botva\n";
			exit(0);
		}
	cout << res << "\n";
}

int main()
{
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		cerr << "Testcase " << (it + 1) << "\n";
		Solve();
	}
	return 0;
}
