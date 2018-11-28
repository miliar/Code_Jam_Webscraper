#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <climits>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef long long       Long;

#define toStr(a)      (((stringstream&)((stringstream()<<(a)))).str())
#define FOR(i,a,b)    for (int i = (a); i < (b); i++)
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it! = (c).end(); it++)
#define all(a)        ((a).begin(), (a).end())
#define pb(a)         push_back(a)
#define mp            make_pair
#define _x            first
#define _y            second

Long gcd(Long a, Long b)
{ return (b==0 ? a : gcd(b, a%b)); }

int main()
{
	freopen("data.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; cin >> T;
	
	for (int x=1; x<=T; x++)
	{
		cout << "Case #" << x << ": "; 

		Long n, a, b, c, d;
		cin >> n >> a >> c;

		b = d = 100;

		Long f = gcd(a, b);
		a /= f;
		b /= f;
		f = gcd(c, d);
		c /= f;
		d /= f;

		if (b > n) goto end;
		if (c==0 && a!=0) goto end;
		if (c==d && a!=b) goto end;

		cout << "Possible\n";
		continue;

end:
		cout << "Broken\n";
	}
}