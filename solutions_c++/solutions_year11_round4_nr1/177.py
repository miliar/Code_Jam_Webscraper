#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define FOR(it,A) for( typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define impr(A) for( typeof A.begin() chen = A.begin(); chen !=A.end(); chen++ ) cout<<*chen<<" "; cout<<endl
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define poner push_back
#define eps (1e-9)
#define sqr(x) (x)*(x)
#define par pair<ll,ll>
using namespace std;

int T;
int caso = 1;
ll x,s,r,n; double t;
ll b[1001], e[1001], w[1001];

int main()
{
	cin >> T;
	while( T-- ){
		cin >> x >> s >> r >> t >> n;
		f(i,0,n) scanf( "%lld %lld %lld", b+i, e+i, w+i );
		vector< par > P;
		f(i,0,n) P.poner( par(w[i],e[i]-b[i]) );
		P.poner( par( 0,x-(accumulate(e,e+n,0) - accumulate(b,b+n,0)) ) ),
		n++;
		sort( all(P) );
		double res = 0;
		f(i,0,n){
			double tmp = (0.0+P[i].second)/(r+P[i].first);
			if( t > tmp-eps ) t-= tmp, res+= tmp;
			else{
				res += t+ ( 0.0+P[i].second-t*(r+P[i].first) )/(s+P[i].first);
				f(j,i+1,n) res += (0.0 + P[j].second )/(s+P[j].first);
				break;
			}
		}
		printf( "Case #%d: %.9f\n", caso++, res );
	}
}
