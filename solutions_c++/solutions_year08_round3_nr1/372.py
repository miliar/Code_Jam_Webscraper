#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <iostream>

using namespace std;

#define SZ(x) ((int)(x).size())
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define ZERO(a) memset(a, 0, sizeof(a))
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define FORE(i, a, b) for(int i = (a); i <= (b); ++i)
#define RFOR(i, b, a) for(int i = (b); i >= (a); --i)
#define FOREACH(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)

typedef long long LL;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<LL> vll;

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	int testCase;
	cin >> testCase;
	LL P, K, L, t;
	for (int cas = 1; cas <= testCase; cas++)
	{
		cin >> P >> K >> L;
		vll v;
		FOR(i, 0, L) cin >> t, v.PB(t);
		sort(ALL(v)); reverse(ALL(v));
		LL ans = 0, k = 0;
		for (int i = 1; i <= P; i++)
		{
			LL s = 0;
			for (int kl = 0; kl < K && k < L; kl++)
				s += v[k++];
			ans += i * s;
		}
		cout << "Case #" << cas << ": " << ans << endl;
	}
	return 0;
}