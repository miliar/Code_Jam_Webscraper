#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
#include <list>
#include <ctime>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;
#define dbgv(x) { cerr << #x << ": {"; for(int i = 0; i < x.size(); ++i) { if(i) cerr << ", "; cerr << x[i]; } cerr << "}" << endl; }

const int maxn = 2001;

LD sum[maxn];
LD fact[maxn];

int main()
{
	sum[0] = 1.0;
	LD cur = 1.0;
	fact[0] = 1.0;
	for(int i = 1; i < maxn; ++i)
	{
		cur /= i;
		cur = - cur;
		sum[i] = sum[i - 1] + cur;
		fact[i] = fact[i - 1] * i;
	}

	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n; cin >> n;
		vector<LD> f(n + 1, 0);
		vector<int> a(n);
		int cnt = 0;
		for(int i = 0; i < n; ++i)
		{
			cin >> a[i];
			if(a[i] == i + 1)
				cnt++;
		}

		f[0] = 0.0;
		for(int i = 1; i <= n; ++i)
		{
			f[i] = 0.0;
			for(int j = 1; j <= i; ++j)
			{
				f[i] += sum[i - j] / fact[j] * (1.0 + f[i - j]);
			}
			LD p = sum[i] / fact[0];
			f[i] = (p + f[i]) / (1.0 - p);
		}

		cout.precision(6);
		cout.setf(ios::fixed);
		cout << "Case #" << z + 1 << ": " << f[n - cnt] << endl;
	}
	return 0;
}
#endif

