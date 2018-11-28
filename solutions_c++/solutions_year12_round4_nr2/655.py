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

typedef long long int64;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<string> vs;

const int64 oo = (1ll << 30);
const int MAXN = (int)1e5 + 1;
const int mod = (int)1e9;
const double eps = 1e-9;
const double pi = acos(-1);

int w, l, n;
vii r;
bool sw;
vector<complex<double> > ans;

bool test(complex<double> p)
{
	if(p.real() > w + 0.0)return false;
	if(p.imag() > l + 0.0)return false;
	REP(i, SZ(ans))
		if(norm(ans[i] - p) < (r[i].first + r[SZ(ans)].first + 0.0)*(r[i].first + r[SZ(ans)].first + 0.0))
			return false;
	return true;
}

void set_next()
{
//	cout << "TEMP " << SZ(ans) <<endl;
	complex<double> p;
	REP(i, SZ(ans))
	{
		p = ans[i];
		p.imag() += r[i].first + r[SZ(ans)].first + 0.0;
		if(test(p))
		{
//			cout << "1 " << p << endl;
			ans.PB(p);
			return;
		}
		p = ans[i];
		p.real() += r[i].first + r[SZ(ans)].first + 0.0;
		if(test(p))
		{
//			cout << "2 " << p << endl;
			ans.PB(p);
			return;
		}
	}
	assert(0);
	return;
}

int main()
{
//	freopen ("in.txt", "rt", stdin);
//	freopen ("out.txt", "wt", stdout);

	int c = 0, T;cin >> T;
while(T--)
{
	cin >> n >> w >> l;
	sw = l > w;
	ans.clear();
	if(sw)
		swap(l, w);
	r = vii(n);

	REP(i, n)
	{
		cin >> r[i].first;
		r[i].second = i;
	}

	sort(ALL(r));
	reverse(ALL(r));
	ans.PB(complex<double>(0, 0));
	REP(i, n - 1)
		set_next();
	
	vector<pair<double, double> > print(n);
	
	REP(i, n)
		print[r[i].second] = MP(ans[i].real(), ans[i].imag());
	
	c++;
	printf("Case #%d: ", c);

	REP(i, n)
	{
		if(!sw)
			cout << print[i].first << " " << print[i].second << " ";
		else
			cout << print[i].second << " " << print[i].first << " ";
	}
	cout << endl;
}
//system("pause");
	return 0;
}
