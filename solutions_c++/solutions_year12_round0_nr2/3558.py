#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>

#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>	

#include <algorithm>
#include <utility>
#include <cstdlib>
#include <limits>
#include <cmath>

#define rep(i, k, n) for(ll (i)=(k);(i)<(n);++(i))
#define repit(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define all(x) x.begin(), x.end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define sortt(a) sort((a).begin(), (a).end())
#define frr() freopen("test.in", "r", stdin)
#define fro() freopen("test.out", "w", stdout)
#define sqr(x) ((x) * (x))
#define abss(x) (int) abs ((double) x)
#define inf 10e9
using namespace std;

typedef long long ll;
typedef pair <ll, ll> pll;
typedef pair <int, int> pii;
typedef pair <short, short> pss;
typedef unsigned long long ull;
typedef long double lcd;
typedef vector<int> vii;
typedef vector<string> vs;

typedef pair <pll, ll> triple;

int distance1(pii a, pii b)
{
	return (a.first - b.first)*(a.first - b.first) + (a.second - b.second)*(a.second - b.second);
}

int main() 
{
	frr();
	fro();

	int T;
	cin >> T;

	int n, s, p;

	rep (i, 0, T)
	{
		cin >> n >> s >> p;
		vii t(n);

		rep (j, 0, n)
			cin >> t[j];
		int res = 0;
		sort(all(t));
		
		int brk = t.size() - 1;

		while (brk >= 0)
		{
			if (t[brk]/3 >= p)
				{res++, brk--; continue;}

			if ((t[brk] + 2)/3 >= p && (t[brk] + 2)/3 >= 1)
				{res++, brk--; continue;}
			
			if ((t[brk] + 4)/3 >= p && (t[brk] + 4)/3 >= 2 && s > 0)
				{res++, brk--, s--; continue;}

			break;
		}

		cout << "Case #"<<i+1<<": "<<res<<endl;
	}

	return 0;
}