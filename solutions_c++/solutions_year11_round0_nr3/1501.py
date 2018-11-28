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

bool op[26][26];
char comb[26][26];

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
	int T,n;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> n;
		int least = 100000000;
		int s = 0;
		int a[n];
		FOR(i,0,n) {
			cin >> a[i];
			s += a[i];
			least = min(least,a[i]);
		}
		bool ok = true;
		FOR(i,0,32) {
			int cnt = 0;
			FOR(j,0,n) {
				if (a[j] & (1 << i))
					++cnt;
			}
			if (cnt&1) {
				ok = false;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (ok)
			cout << s-least << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
