#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

vint t[2];
vint q;
int res,n,k,l,m,w;
int p[2], c[2];
string s;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	rep(S,T)
	{
		res = 0;
		q.clear();
		t[0].clear();
		t[1].clear();
		p[0] = p[1] = 1;
		c[0] = c[1] = 0;

		cin >> n;
		rep(i,n)
		{
			cin >> s >> k;
			if (s == "O") l = 0;
			else l = 1;
			t[l].pb(k);
			q.pb(l);
		}
		rep(i,n)
		{
			l = q[i];
			m = 1-l;
			k = abs(t[l][c[l]] - p[l]) + 1;
			res += k;
			p[l] = t[l][c[l]];
			c[l]++;
			if (c[m] < int(t[m].size())) /* if have to move*/
			{
				w = min(abs(t[m][c[m]] - p[m]), k);
				if (t[m][c[m]] < p[m]) p[m] -= w;
				else p[m] += w;
			}
		}

		printf("Case #%d: %d\n",S+1,res);
	}

	return 0;
}

