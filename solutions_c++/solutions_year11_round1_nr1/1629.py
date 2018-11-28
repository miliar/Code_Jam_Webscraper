#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <iomanip>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())

typedef long long			ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>			vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>			vpii;

const int N = 25;

int gcd(int a, int b)
{
	if (a == 0)
		return b;
	return gcd(b%a, a);
}

int main(int argc, char *argv[])
{
#if 0
	freopen(argv[1],"r",stdin);
#endif
#if 1
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	int T,n,d,g;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> n >> d >> g;
		int x = gcd(d,100);
		int y = gcd(g,100);
		int n1 = d/x;
		int d1 = 100/x;
		int n2 = g/y;
		int d2 = 100/y;
		if (d1 > n) {
			cout << "Case #" << t << ": Broken" << endl;
			continue;
		}
		x = n2 - n1;
		y = d2 - d1;
		if (x < 0 || y < 0) {
			cout << "Case #" << t << ": Broken" << endl;
			continue;
		}
		if (x <= y)
			cout << "Case #" << t << ": Possible" << endl;
		else
			cout << "Case #" << t << ": Broken" << endl;
	}
	return 0;
}
