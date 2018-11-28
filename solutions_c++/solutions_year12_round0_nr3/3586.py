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

int solve (int a, int b, int c)
{
	int ndig = 0;
	for (int j = c; j > 0; j /= 10)
		ndig++;
	int tmp = c;
	set <int> numb;
	rep(i, 0, ndig)
	{
		tmp = tmp/10 + (int)pow(10.0, (double)(ndig-1))*(tmp%10);
		if (tmp <= b && tmp > c)
			numb.insert(tmp);
	}
	
	return numb.size();
}

int main() 
{
	frr();
	fro();

	int T;
	cin >> T;


	rep (i, 0, T)
	{
		int res = 0;
		int a, b;
		cin >> a >> b;

	    rep (i, a, b + 1)
			res += solve (a, b, i);

		cout << "Case #"<<i+1<<": "<<res<<endl;
	}

	return 0;
}