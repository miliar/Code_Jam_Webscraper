#define DEBUG 1

using namespace std;

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define EPS 1e-11
#define inf ( 1LL << 31 ) - 1
#define LL long long

#define _rep(i, a, b, x) for(int i(a), _b(b); i <= _b; i += x )
#define rep(i, n) _rep( i, 0, n - 1, 1 )
#define rrep(i, a, b) for(int i(a),_b(b); i >= (_b); --i)
#define xrep( i, a, b ) _rep(i, a, b, 1)
#define foreach(type, v, it) for(type::iterator it = v.begin(); it!=v.end(); ++it)

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))
#define mp make_pair
#define pb push_back
#define sz(k) (int)(k).size()

#define dbg(x) if(DEBUG) cerr << __LINE__ << ": " << #x << " -> " << (x) << "\t";
#define dbge(x) if(DEBUG) cerr << __LINE__ << ": "<<#x << " -> " << (x) << endl;




// She
// May be the reason I survive
// The why and wherefore I'm alive
// The one I'll care for through the rough in ready years

//...

const int NMAX = 50;

LL x[NMAX+5], v[NMAX+5], pos[NMAX+5];

int main()
{
	int t, n, k, baje;
	LL B, T, swaps, ans;
	freopen("f:/data/B-large.in-1.txt","r",stdin);
	freopen("f:/data/bl.txt","w",stdout);



	scanf("%d", &t);
	
	xrep(tc,1,t)
	{
		scanf("%d %d %I64d %I64d", &n, &k, &B, &T);
		baje = 0, swaps = 0;
		rep(i,n) scanf("%I64d", &x[i]);
		rep(i,n) scanf("%I64d", &v[i]);
		
		rep(i,n) 
		{
			pos[i] = x[i] + T * v[i];
			//cout<<pos[i]<<endl;
		}
		
		rrep(i,n-1,0)
		{
			if (pos[i] < B) baje++;
			else 
			{
				swaps += baje; 
				k--;
			}
			if (k == 0) break;
		}
		
		if (k == 0) ans = swaps;
		else ans = -1;
		
		
		
				
		printf("Case #%d: ", tc);
		if (ans == -1) printf("IMPOSSIBLE\n");
		else printf("%I64d\n", ans);
	}
	
	
	
	
	return 0;
}
