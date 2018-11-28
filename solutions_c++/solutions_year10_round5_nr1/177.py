#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
int res;
ll primos[100000], cant;
#define MM 1000000
int D, K;


ll modu(ll M, ll P)
{
	ll r = M % P;
	if( r < 0 ) r += P;
	return r;
}

ll pw(ll a, ll e, ll P)
{
	if( e == 0 ) return 1;
	if( e == 1 ) return a;
	ll x = pw(a, e/2, P);
	x = (x*x) % P;
	if( e& 1 )
		x = ( x * a ) % P;
	return x;
}


ll inverso(ll v, ll P)
{
	return pw(v, P-2, P);
}

int main()
{
	int i,j ,k;
	bool p[MM+1];
	REP(i, MM+1 ) p[i] = true;
	p[0] = p[1] = false;
	REP(i, MM+1)
	{
		if( !p[i] ) continue;
		int j = i + i;
		while( j <= MM ) p[j] = false, j += i;
		primos[cant++] = i;
	}
	
	int casos; cin >> casos;
	
	for( int h = 0 ; h < casos; h ++ )
	{
		cin >> D >> K;
		vector<long long> vec;
		long long aux;
		REP(i, K){ cin >> aux; vec.PB(aux);}
		
		if( K == 1 )
		{
			cout << "Case #" << (h+1) << ": " << "I don't know." << endl;
		}else if( K == 2 )
		{
			if( vec[0] == vec[1] ) 
				cout << "Case #" << (h+1) << ": " << vec[0] << endl;
			else cout << "Case #" << (h+1) << ": " << "I don't know." << endl;
		}else
		{
			// controlamos repeticiones..
			bool repeat = false;
			bool wrong = false;
			for(int i = 1; i < vec.size() ; i ++ )
			{
				
				if( vec[i] == vec[i-1] )
				{
					repeat = true;
				}else
				{
					if( repeat ) wrong = true;
				}
				 
			}
			if( wrong )
			{
				cout << "Case #" << (h+1) << ": " << "I don't know." << endl;
				continue;
			}else if( repeat )
			{
				cout << "Case #" << (h+1) << ": " << vec[(int)vec.size()-1] << endl;	
				continue;
			}
			
			int possible = 0;
			int rr = -1;
			ll great = 0;
			for( j = 0; j < vec.size(); j ++ ) great =  max( great, vec[j]);
			for( j = 0 ; j < cant && primos[j] <= pw(10, D, 100000000); j ++ )
			{
				if( primos[j] <= great ) continue;
				//printf("%lld %lld\n", primos[j], great);
				ll P = primos[j];
				
				ll v = modu(vec[2]-vec[1], P);
				ll resta = modu(vec[1] - vec[0], P);
				ll A = modu(v * inverso(resta, P), P);
				ll B = modu( vec[1] - modu(A * vec[0], P), P);
				if ( P == 7 ){
// 					printf("HOLA}\n");
// 					cout << v << " " << resta << "  " << A << " " << B << endl;
				}
				bool ok = true;
				for( k = 1 ; k < vec.size() ; k ++ )
				{
					ll R = modu((A * vec[k-1]) + B, P);
					if( R != vec[k] ) ok = false;
				}
				if( ok ) 
				{
// 					printf("   %lld\n", P);
					ll next = modu( A * vec[(int)vec.size()-1] + B, P);
					if( rr == -1 ) rr = next;
					else if( rr != next ) rr = -2;
				}
			}
// 			printf("%i \n", rr);
			if( rr >= 0 )
				cout << "Case #" << (h+1) << ": " << rr << endl;	
			else
				cout << "Case #" << (h+1) << ": " << "I don't know." << endl;
		
			}
	       
	}return 0;
}
