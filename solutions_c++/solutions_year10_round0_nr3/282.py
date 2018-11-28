#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;
#define forn(i,n) for(int i=0; i<int(n); i++)
#define forsn(i,s,n) for(int i=(s); i<int(n); i++)
#define dforn(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(__typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(), (c).end()
#define esta(v,c) ((c).find(v) != (c).end())
#define zMem(c) memset((c), 0, sizeof(c))
#define pb push_back
#define x first
#define y second
#define INF 1000000000
typedef long long tint;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef pair<int,int> pint;

const int N = 1024;
tint g[2*N]; int pos[2*N]; tint suma[2*N]; int pise[N];

int main()
{	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	int TT;
	cin >> TT;
	
	forn(tt,TT)
	{
		tint r; int n; tint k;
		cin >> r >> k >> n;
		
		forn(i,n) cin >> g[i];
		
		forn(i,N) pise[i] = -1;
		int p = 0;
		pos[0] = suma[0] = pise[0] = 0;
		
		int i = 1;
		for(; 1; i++)
		{
			tint s = 0; int p0 = p, prim = 1;
			for(; s + g[p] <= k and (prim or p != p0); ((++p)>=n) ? (p-=n) : p, prim = 0)
				s += g[p];
			pos[i] = p;
			suma[i] = suma[i-1] + s;
			if( pise[p] == -1 ) pise[p] = i;
			else break;
		}
		//cout << "pos "; forn(j,i+1) cout << pos[j] << " "; cout << endl;
		//cout << "sum "; forn(j,i+1) cout << suma[j] << " "; cout << endl;
		//cout << "pise[p] " << pise[p] << endl;
		
		tint res;
		if(r <= pise[p])
		{
			//cout << "caso 1 " << suma[r] << endl;
			res = suma[r];
		}
		else
		{
			//cout << "caso 2" << endl;
			res = suma[pise[p]];
			//cout << "head " << suma[pise[p]] << endl;
			r -= pise[p];
			tint m = i - pise[p];
			//cout << "tail " << suma[i] - suma[pise[p]] << endl;
			//cout << "ciclos " << r << " " << m << " " << r/m << endl;
			res += (suma[i] - suma[pise[p]]) * (r / m);
			r %= m;
			//cout << "resto " << r << endl;
			res += suma[r + pise[p]] - suma[pise[p]];
		}
		cout << "Case #" << (tt+1) << ": " << res << endl;		
	}
	
	return 0;
}
