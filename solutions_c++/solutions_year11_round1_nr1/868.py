#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstring>

#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <utility>
#include <queue>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

using namespace std;

int gcd(int a, int b){
	if (b==0) return a;
	else return gcd(b, (a%b));
}

int main(){
	ios_base::sync_with_stdio(false);
	
	int test, t=1, pd, pg;
	long long n;
	
	cin >> test;
	while (test--){
		cin >> n >> pd >> pg;
		int den = 100 / gcd(pd, 100);
		//cout << "DBG: den: " << den << " gcd: " << gcd(pd, 100) << endl;
		if ( (den > n)
			|| ( (pd != 100 ) && (pg == 100) )
			|| ( (pd != 0) && (pg == 0) ) ){
			cout << "Case #" << t++ << ": Broken\n";
		}
		else cout << "Case #" << t++ << ": Possible\n";
	}
	
	return 0;
}