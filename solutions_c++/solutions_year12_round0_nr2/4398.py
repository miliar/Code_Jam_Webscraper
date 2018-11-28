//Seikang

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <stdlib.h>
#include <utility>

#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>

#include <cmath>
#include <complex>
#include <algorithm>

#include <ctime>
#define gtime clock()

using namespace std;

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, lo, hi) for(int i = (lo); i <= (hi); i++)
#define FORD(i, hi, lo) for(int i = (hi); i >= (lo); i--)
#define FE(it, cont) for(typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define ALL(cont) (cont).begin(), (cont).end()
#define SZ(cont) (int)((cont).size())
#define PB  push_back
#define MP  make_pair

template<class T> vector<T> split(const string &s){stringstream ss(s);vector<T> a;T t;while(ss >> t)a.PB(t);return a;}
template<class T> T parse(const string &s){stringstream ss(s);T e;ss >> e;return e;}
template<class T> string toString(const T &e){stringstream ss();ss << e;return ss.str();}

typedef long long int64;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo = (1ll << 30);
const int MAXN = (int)1e3 + 1;
const int mod = (int)1e9;
const double eps = 1e-9;
const double pi = acos(-1);

int main()
{
//	freopen ("b_large.in", "rt", stdin);
//	freopen ("b_large.out", "wt", stdout);
	int c = 1;
	int T;cin >> T;
while(T--)
{
	int n, k, m;
	cin >> n >> k >> m;
	vi p(n);
	REP(i, n)
		cin >> p[i];
	sort(ALL(p));
	int ans = 0;
	REP(i, n)
	{
		if(3*m <= p[i])
		{
			ans++;
		}
		else if(3*m - 2 <= p[i] && m - 1 >= 0)
		{
			ans++;
		}
		else if((k > 0) && ((3 * m - 4) <= p[i]) && m - 2 >= 0)
		{
			ans++;
			k--;
		}
	}
	if(c > 1)cout << endl;
	printf("Case #%d: %d", c++, ans);
}
//system("pause");
	return 0;
}
