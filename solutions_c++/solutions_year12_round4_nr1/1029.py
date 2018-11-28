#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <numeric>
#include <fstream>
using namespace std ;

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

int h0[4] = {0, -1, +0, +1};
int h1[4] = {-1, +0, +1, +0};

int N, M ;

int inside( int x, int y)
{
	return x > 0 && x <= N && y > 0 && y <= M ;
}

int D[20007], L[20007] ;
long long Left[20007] ;

main()
{
	int test ;
	cin >> test ;
	FOR(Case,1,test)
	{
		int n ;
		cin >> n ;
		FOR(i, 1, n) cin >> D[i] >> L[i] ;
		cin >> D[n+1] ;
		L[n+1] = 0 ;
		
		FOR(i,1,n+1) Left[i] = -1 ;
		
		Left[1] = D[1] * (long long)D[1];
		FOR(i, 1, n+1)
		{
			if ( Left[i] < 0 )
				continue;
			
			long long kc2 = Left[i] ;
			FOR(j, i+1, n+1)
			{
				long long gh = D[j] - D[i] ;
				long long gh2 = gh * gh ;
				if ( kc2 < gh2 ) 
					continue;
				long long leng = min( gh2, (long long)L[j] * L[j] ) ; 
				if ( Left[j] < leng ) Left[j] = leng ;
			}
		}
		
		cout << "Case #" << Case << ": ";
 		if ( Left[n+1] == -1 ) 
			cout << "NO" << endl ;
		else
			cout << "YES" << endl ;
	}
}