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

const int64 oo = (1ll << 5);
const int MAXN = (int)1e4 + 1;
const int mod = (int)1e9;
const double eps = 1e-9;
const double pi = acos(-1);

//int dp[MAXN];
//int val[MAXN];
vi pos;
vi val;
vi reach;
int dist;

bool calc()
{
	reach = vi(SZ(pos), -1);
	reach[0] = pos[0];
	REP(i, SZ(pos))
	{
		FOR(j, i + 1, SZ(pos) - 1)
		{
			if(pos[i] + reach[i] < pos[j])
				break;
			reach[j] = max(reach[j], min(pos[j] - pos[i], val[j]));
		}
	}
	REP(i, SZ(reach))
	{
		if(pos[i] + reach[i] >= dist)
			return true;
	}
	return false;
}


int main()
{
//	freopen ("in.txt", "rt", stdin);
//	freopen ("out.txt", "wt", stdout);
	int c = 0;int T; cin >> T;
while(T--)
{
	int n;
	cin >> n;
	pos = vi(n);
	val = vi(n);
	REP(i, n)
		cin >> pos[i] >> val[i];
	cin >> dist;
	c++;
	printf("Case #%d: %s\n", c, calc() ? "YES" : "NO");
}
//system("pause");
	return 0;
}
