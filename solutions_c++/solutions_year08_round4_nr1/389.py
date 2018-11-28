#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define iss istringstream
#define oss ostringstream
#define prv(vec) {for(int zz = 0; zz < vec.size(); ++zz) cout << vec[zz] << " "; cout << endl;}
#define sz(a) ((a).size())
#define len(a) ((a).length())
#define all(c) (c).begin(),(c).end() 
#define forn(i,a,n) for(int i = (int) a; i < (int)n; i++) 

vector <int> g,c,a;
int f[10001][2];
int n;

int calc ( int v, int zn)
{
	if ( f[v][zn] != -1 ) return f[v][zn];
	if ( v > (n-1)/2 )
	{
		if ( a[v] == zn ) f[v][zn] = 0; 
		else f[v][zn] = 100000;
	}
	else if ( c[v] == 0 )
	{
		if ( g[v] == 1 )
		{
			if ( zn == 1 ) f[v][zn] = calc(2*v,1) + calc(2*v+1,1);
			else f[v][zn] = min( calc(2*v,0), calc(2*v+1,0) );
		}
		else
		{
			if ( zn == 1 ) f[v][zn] = min( calc(2*v,1), calc(2*v+1,1) );
			else f[v][zn] = calc(2*v,0) + calc(2*v+1,0) ;
		}
	}
	else
	{
			int r1,r2;
			if ( zn == 1 ) r1 = calc(2*v,1) + calc(2*v+1,1);
			else r1 = min( calc(2*v,0), calc(2*v+1,0) );
			if ( zn == 1 ) r2 = min( calc(2*v,1), calc(2*v+1,1) );
			else r2 = calc(2*v,0) + calc(2*v+1,0);
			if ( g[v] == 1 ) r2++;
			else r1++;
			f[v][zn] = min(r1,r2);
	}
	return f[v][zn];
}

int main()
{
	freopen("a3.in","rt",stdin);
    freopen("a3.out","wt",stdout); 
	int T,v;
	cin >> T;
	forn(t,0,T)
	{
		cin >> n >> v;
		g.resize(n+1);
		c.resize(n+1);
		a.resize(n+1);
		forn(i,1,n+1) { f[i][0] = -1; f[i][1] = -1; }
		forn(i,1,(n+1)/2) cin >> g[i] >> c[i];
		forn(i,(n+1)/2,n+1) cin >> a[i];
		int res = calc(1,v);
		if ( res < 10000 ) cout << "Case #" << t+1 <<": " << res << endl;
		else cout << "Case #" << t+1 <<": " << "IMPOSSIBLE" << endl;
		//printf("Case #%d: %lld\n",t+1,ts);
	}
    return 0;
}