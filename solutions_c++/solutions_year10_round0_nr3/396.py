#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <cstring>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1000000000
#define L(s) (long long)((s).end()-(s).begin())
#define FOR(i,a,b) for (long long _n(b), i(a); i <= _n; i++)
#define FORD(i,a,b) for(long long i=(a),_b=(b);i>=_b;i--)
#define rep(i,n) FOR(i,1,(n))
#define rept(i,n) FOR(i,0,(n)-1)
#define C(a) memset((a),0,sizeof(a))
#define lllong long long long
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))
#define VI vector<long long>
#define ppb pop_back
#define mp make_pair
#define pii pair<long long,long long>
#define pdd pair<double,double>
#define x first
#define y second
#define sqr(a) (a)*(a)
#define D(a,b) sqrt(((a).x-(b).x)*((a).x-(b).x)+((a).y-(b).y)*((a).y-(b).y))
#define pi 3.1415926535897932384626433832795028841971
#define tt (ll+rr)/2
#define rnd() ((rand() << 16) ^ rand())

int main()
{
	freopen("input.in","rt",stdin); freopen("output.txt","wt",stdout);
	
	long long tc, TC;
	cin >> TC;
	rep(tc, TC)
	{
		printf("Case #%d: ",tc);
		long long r, k, n;
		cin >> r >> k >> n;

		vector<long long> v(n), nxt(n), w(n);
		rept(i, n)	cin >> v[i];
		
		
		if (tc == 31)
			tc = tc;

		rept(i, n)
		{
			long long c = 0, j;
			for (j = i; j != i + n; j++) {
				c += v[j % n];
				if (c > k) break;
			}
			nxt[i] = j % n;
			w[i] = c;
			if (j != i + n)  w[i] -= v[j % n];
		}

		long long sum = 0, cycw = 0, cyclen = 0;

		long long used[1005];

		memset(used,0, sizeof(used));

		//precounting

		for (long long i = 0; ++used[i] != 2; i = nxt[i])
		{
 			cycw += w[i];
			cyclen++;
		}

		for (long long i = 0; used[i] != 2; i = nxt[i])
		{
			cyclen--;
			cycw -= w[i];
		}

		//counting
	
		for (long long i = 0; used[i] != 2 && r > 0; i = nxt[i])
		{
			r--;
			sum += w[i];
		}

		sum += cycw * (r / cyclen);
		r %= cyclen;


		long long st;
		for (long long i = 0; i < n; i++) if (used[i] == 2) st = i;


		for (long long i = st; r > 0; i = nxt[i])
		{
			r--;
			sum += w[i];
		}

		cout << sum << endl;
	}
	
	return 0;
}






