#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <sstream>
#include <limits.h>
#include <cassert>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cstring>

using namespace std;

#define FOR(i,n) for(int i = 0 ; i < n ; i++)
#define FOZ(i,v) FOR(i,int(v.size()))
#define rep(i,x,y) for(int i=(x);   \
	( i )<=( (y)); i ++)

#define FOT(i,v) for(typeof(v.begin()) i = v.begin(); i != v.end() ; i++)
#define FOTT(i,j,v) for(typeof(v.begin()) i = j; i != v.end() ; i++)
typedef vector<vector< int> > vvi;
typedef vector<int> vi;
typedef long long ll ; 
typedef pair<ll,ll> pii;
#define vv(T) vector< vector < T > >
#define Sort(v) sort(v.begin(),v.end());

pii add(pii a, pii b) { 
	return pii((a.first + b.first)%3, (a.second+b.second)%3) ;
}

pii genr(pii a, pii b) { 
	return pii(4*a.first - b.first, 4*a.second - b.second) ;
}

ll test() { 
	ll n, a, b, c, d, x, y, M ; 
	cin >> n>>a>>b>>c>>d>>x>>y>>M ; 
	vector<pii> p; 
	FOR(i,n) { 
		p.push_back(pii(x%3,y%3)) ;
		x = (a*x +b ) % M ; 
		y = (c*y +d) % M ;
	}

	vector<ll> co(100,0);
	/* do a count */
	FOR(i,n) co[p[i].first*3+p[i].second] ++ ;

	ll ans = 0 ; 
	FOR(i,9) rep(j,i+1,8) rep(k,j+1,8) {
		int first = i/3+j/3+k/3;
		first %= 3;
		int second = i%3 + j %3 + k %3 ; 
		second %= 3; 
		if ( first == 0 and second == 0 ) { 
			ans += co[i]*co[j]*co[k];
		}
	}

	/* case 2: two things are same */ 
	FOR(i,9) FOR(k,9) { 
		if ( i == k) continue ;
		int  j = i ;
		int first = i/3+j/3+k/3;
		first %= 3;
		int second = i%3 + j %3 + k %3 ; 
		second %= 3; 
		if ( first == 0 and second == 0 ) { 
			ans += co[i]*(co[j]-1)*co[k]/2;
		}

	}

	/* all three same */
	FOR(i,9) { 
		int  j = i, k = i ;
		int first = i/3+j/3+k/3;
		first %= 3;
		int second = i%3 + j %3 + k %3 ; 
		second %= 3; 
		if ( first == 0 and second == 0 ) { 
			ans += co[i]*(co[j]-1)*(co[k]-2)/6;
		}

	}

	return ans ;
	
}
int main() {

	int t;
	cin>>t ; 
	FOR(i,t) printf("Case #%d: %lld\n", i+1, test());
	return 0;
}
