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

#define rep(i, k, n) for(ll (i)=(k);(i)<(n);++(i))
#define all(x) x.begin(), x.end()
#define clr(a,v) memset((a),(v),sizeof(a))
#define sortt(a) sort((a).begin(), (a).end())
#define frr() freopen("test.in", "r", stdin)
#define fro() freopen("test.out", "w", stdout)
#define sqr(x) ((x) * (x))
#define abss(x) (int) abs ((double) x)
using namespace std;

typedef pair <int, int> pii;
typedef pair <short, short> pss;
typedef long long ll;
typedef unsigned long long ull;
typedef long double lcd;
typedef vector<int> vii;
typedef vector<string> vs;

int const inf = 0x7f7f7f7f;
ll const llinf = 0x7f7f7f7f7f7f7f7fll;
lcd const eps = 1e-9;

#include <iostream>
#include <algorithm>

vii operator+ (vii const &a, vii const &b){
	int as = a.size(), bs = b.size(), rs = max(as, bs);
	if(as > bs) return b+a;
	vii res(rs);
	int t = 0;
	for(int i = 0; i < as; i++){
		res[i] = a[i] + b[i] + t;
		t = 0;
		if(res[i] >= 10){
			res[i] -= 10;
			t++;
		}
	}
	for(int i = as; i < bs; i++){
		res[i] = b[i] + t;
		t = 0;
		if(res[i] >= 10){
			res[i] -= 10;
			t++;
		}
	}
	if(t) res.push_back(t);
	return res;
}

using namespace std;

vii check(vii a, vii b)
{
	vii res;
	set<int> res1;

	rep (i, 0, a.size())
		rep (j, 0, b.size())
		if (a[i] == b[j])
			res1.insert(a[i]);

	for (set<int>::iterator it = res1.begin(); it != res1.end(); ++it)
		res.push_back(*it);

	return res;

}
int main()
{
	frr();
	fro();

	int test;
	cin >> test;

	int n, minn, xor, sum, curr;

	rep (i, 1, test + 1)
	{
		sum = xor = 0;
		minn = inf;

		cin >> n;
		rep (j, 0, n)
		{
			cin >> curr;
			sum += curr;
			minn = min (minn, curr);
			xor ^= curr;
		}

		if (xor != 0)
		{
			cout << "Case #" << i << ": NO\n";
			continue;
		}

		cout << "Case #" << i << ": " << sum - minn << endl;
	}

	return 0;
}
