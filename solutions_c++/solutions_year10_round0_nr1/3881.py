#pragma warning(disable:4786)
#include<iostream>
#include<ctype.h>
#include<bitset>
#include<sstream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<utility>
#include<numeric>

using namespace std;

#define inf (1<<28)
#define eps (1e-8)
#define pi (acos(-1.0))

#define _max(a,b) ( (a)>(b)?(a):(b) )
#define _min(a,b) ( (a)<(b)?(a):(b) )
#define _clear(a) memset(a,0,sizeof(a))
#define _nclear(a,n) memset(a,0,(n*sizeof(a[0])))
#define _set(a) memset(a,-1,sizeof(a))
#define _sq(a) ((x)*(x))
#define contain(s,x) ((s&(1<<x))>0)

long countBit(long x)
{
	return (x)? 1 + countBit(x&(x-1)):0;
}

template<class T>
T gcd(T a,T b)
{
	if(a<0) return gcd(-a,b);
	else if(b<0) return gcd(a,-b);
	else return (b)?gcd(b,a%b):a;
}

template<class T>
T lcm(T a,T b)
{
	return a*(b/gcd(a,b));
}

#define _read(a) freopen(a,"r",stdin)
#define _write(a) freopen(a,"w",stdout)

//typedef __int64 long long;
//#define _fs "%I64d"
//#define _fs "%lld"

typedef vector < int > vi;
typedef pair < int, int > pii;
typedef pair < int, pii > piii;
typedef vector < pii > vpii;
typedef vector < vpii > vvpii;
typedef vector < string > vs;
typedef pair < int, string > pis;

#define X first
#define Y second

#define max 100


int main()
{

	long cs, n, k, tc;

//	_read("a2.txt");
//	_write("aout2.txt");

	cin >> tc;

	for( cs = 1 ; cs <= tc ; cs++ )
	{
		cin >> n >> k;
		
		if( k == 0 ) cout << "Case #" << cs << ": OFF" << endl;
		else if ( k % ( 1 << n ) == ( 1 << n ) - 1 ) cout << "Case #" << cs << ": ON" << endl;
		else cout << "Case #" << cs << ": OFF" << endl;
	}

	return 0;
}