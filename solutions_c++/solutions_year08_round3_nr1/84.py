#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctype.h>
#include <bitset>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef istringstream iss;
typedef ostringstream oss;

#define d2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a))) 
#define cl(a, val) memset(a, val, sizeof(a))
#define deb(x) cout<<#x<<" = "<<(x)<<endl
#define FG(a, b) for((a) = (b); (a) >= 0; (a)--)
#define FD(a, b) for((a) = 0; (a) < (b); (a)++)
#define all(a) (a).begin(),(a).end() 
#define sz(a) int((a).size())
#define PB push_back
#define INF 0x3fffffff
#define Y second
#define X first

char in[] = "A-large.in";//"A-small-attempt0.in";
char out[] = "A-large.out";

int n, m;
bool sf(int a, int b){ return  a > b; }

int main()
{
	freopen(in, "rt", stdin);
	freopen(out, "wt", stdout);

	int i, j, m;
	int T, t;
	scanf("%d", &T);

	for(t = 1; t <= T; t++)
	{
		int p, k, l;
		ll res(0);
		scanf("%d%d%d", &p, &k, &l);
		vi lk(l, 0);
		FD(i, l) scanf("%d", &lk[i]);

		if( p*k < l )
		{
			printf("Case #%d: Impossible\n", t);
			continue;
		}
		sort(all(lk), sf);

		for(i = 0; i < sz(lk); i++)
		{
			m = i / k + 1;
			res += lk[i] * m;
		}
		printf("Case #%d: %lld\n", t, res);
	}
	return 0;
}