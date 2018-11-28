#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RI( i, o ) for(typeof(o.begin()) i= (o).begin(); i!=(o).end(); ++i)
#define RP3( x, y, z ) RP( i, 0, x ) RP( j, 0, y ) RP( k, 0, z )
#define RP( i, s, e ) for(typeof(s) i=(s); i<(e); ++i)
#define R( i, x ) RP(i,0,(x).size())
#define pB push_back

int M;
vector<int> g;
vector<int> h;
vector<int> r;

int solve(int p)
{
	int ans;
	if(r[p]==0)
	{
		if(g[p]==1)
			ans= 0;
		else ans= 1<<20;
	}
	else{
	
	int p2=1, d;
	while(p2<p) p2*=2;
	p2/=2; d=(p-p2)*2;
	
	int a=solve(d+p2*2), b=solve(d+p2*2+1);
	
	if(g[p]==1)
	{
		if(h[p]==1)
			ans= min(min(a+b, min(a,b)+1),1<<20);
		else
		ans= min(a+b,1<<20);
	}
	else
	{
		ans= min(min(a,b),1<<20);
	}}
	//cout << r[p] << " " << p << " " << ans << endl;
	return ans;
}

int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		int v,m,e, c;
		cin >> m >> v;
		M=m;
		g=h=r=vi(1,1);
		
		RP(i,0,m)
		if(i<((m-1)/2))
		{
			cin >> e >> c;
			if(v==1)
				g.push_back(e);
			else
				g.push_back(1-e);
			h.push_back(c);
			r.push_back(1);
		}
		else
		{
			cin >> e;
			if(v==1)
				g.push_back(e);
			else
				g.push_back(1-e);
			h.push_back(0);
			r.push_back(0);
		}
		
		int S=solve(1);
		if(S<M)
			cout << "Case #" << cn << ": " << S << endl;
		else
			cout << "Case #" << cn << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
