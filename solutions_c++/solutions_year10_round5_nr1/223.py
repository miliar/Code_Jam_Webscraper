//DS includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>

//Other Includes
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define oo 					(int)13e7
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define ull 					unsigned long long
#define ll 						long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb( z ) 				push_back( z )
#define gcd					__gcd
using namespace std;

const int mxn = (int)1e6;
bool sv[mxn];
ll x[16];


ll karo( ll f, ll p )
{
	f%=p;
	if( f < 0 ) f+=p;
	return f;
}
ll expo(ll a, ll p, ll mod )
{
	ll r = 1;
	while( p > 0 )
	{
		if( p&1 )
		{
			r = (r*a)%mod;
		}
		a = (a*(ll)a)%mod;
		p >>= 1;
	}
	return r;
}
int main()
{
	
	
	//freopen("A-small-attempt0.in", "r", stdin ); freopen("A-small-attempt0.out", "w", stdout );
	//freopen("A-small-attempt1.in", "r", stdin ); freopen("A-small-attempt1.out", "w", stdout );
	//freopen("A-small-attempt2.in", "r", stdin ); freopen("A-small-attempt2.out", "w", stdout );
	//freopen("A-small-attempt3.in", "r", stdin ); freopen("A-small-attempt3.out", "w", stdout );
	freopen("A-small-attempt4.in", "r", stdin ); freopen("A-small-attempt4.out", "w", stdout );
	
	//freopen("A-large.in", "r", stdin ); freopen("A-large.out", "w", stdout );
	
	
	
	vector<int> primes;
	for(int i=2; i < mxn; i++)
	if( !sv[i] )
	{
		primes.pb( i );
		for(int j=i*2; j < mxn; j += i )
		sv[j] = 1;
	}
	
	int T;
	cin>>T;
	for(int t=1; t <= T; t++)
	{
		ll D, K;
		cin>>D>>K;
		int Lim = 1;
		for(int i=0;i<D;i++) Lim *= 10;
		ll mxk = 0;
		for(int i=0; i < K; i++)
		{
			cin>>x[i];
			mxk = max( mxk, x[i] );
		}
		
		
		
		set< ll > sols;
		
		if( K==2 )
		{
			if( x[0]==x[1] && x[1]==0 )
			{
				sols.insert( 0 );
			}
		}
		if( K > 1 )
		for(int i=0; i < primes.size() && primes[i] <= Lim; i++)
		if( primes[i] > mxk )
		{
			
			ll p = primes[i];
			ll Z = karo(x[1]-x[0], p);
			ll W = karo(x[2]-x[1],p);
			ll cA = ( W*(ll)expo( Z, p-2, p ) ) % p;
			ll cB = karo( x[1] - ( cA*(ll)x[0] )%p, p );
			ll S = x[0];
			
			bool works = 1;
			
			for(int j=0; j < K; j++)
			{
				if( S != x[j] ) { works = 0; break; }
				S = ( cA*S + cB ) % p;
			}
			//if( p > 1000 && p < 1050 )	cout<< S << " " << p << " " << cA << " " << cB << " " << p << endl;
			if( works )
			{
				sols.insert( ( x[K-1]*cA + cB ) % p );
			}
		}
		//cout<< sols.size() << endl;
		printf("Case #%d: ", t );
		if( sols.size() != 1 )
		{
			printf("I don't know.\n");
		}
		else
		{
			printf("%lld\n", *sols.begin() );
		}
		
	}
	
	
	return 0;
}
