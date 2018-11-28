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
using namespace std;

int T,caso = 1;
int suma,cant;
void solve(ll n){
	suma = 1; cant = 0;
	for(ll p = 2; p*p<=n; p++ )if( n%p==0 ){
		while( n%p==0 ) n/=p, suma++;
		cant++;
	}
	if( n>1 ) suma++, cant++;
}
int a[1000005];
int p[100000]; int sz = 0;

int main()
{
	for( ll i =2; i<1000005; i++)if( !a[i] ){
		for( ll j = i*i; j<1000005; j+=i ) a[j] = 1;
		p[sz++] = i;
	}

	cin >> T;
	while(T--){
		ll n; cin >> n;
		cant = 0; suma = 1;
		f(i,0,sz)if( p[i]<=n ){
			cant++;
			ll pot = p[i];
			while( pot<=n ) pot*=p[i], suma++;
			
		}

		printf( "Case #%d: %d\n", caso++, n==1? 0:suma-cant );
	}
}
