#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <string>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <bitset>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define dbg(x) {cerr << #x << " " << x << endl;}
#define dbgv(x) {cout << "{ "; for(int i = 0; i < (x).size(); ++i) cout << " " << (x)[i]; cout << " }\n";}
const double eps = 1e-9;
const LD pi = 3.1415926535897932384626433832795;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream


bool check(int n, int k)
{
	int res = 0;
	int m = n;
	set<int> u;
	while(!u.count(n))
	{
		u.insert(n);
		res = 0;
		while(n)
		{
			res += (n % k) * (n % k);
			n /= k;
		}
		n = res;
		if(n == 1)
			return true;
	}
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d\n", &t);
	for(int z = 0; z < t; ++z)
	{
		string s; getline(cin, s);
		iss is(s);
		vector<int> a;
		int b;
		while(is >> b)
			a.pb(b);
		int res = 0;
		for(int i = 2; ; ++i)
		{
			bool fl = true;
			for(int j = 0; j < a.size(); ++j)
				if(!check(i, a[j]))
					fl = false;
			if(fl)
			{
				res = i;
				break;
			}
		}
		cout << "Case #" << z + 1 << ": " << res << endl;

	}

	return 0;
}