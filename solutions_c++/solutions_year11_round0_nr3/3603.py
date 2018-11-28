#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

#define REP(i,a,b) for(i=(a);i<(b);i++)
#define ll long long int
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()


int main()
{
	int test , n , k , cs = 1;
	cin >> test;
	int a[ 1005 ];
	while( test-- ) {
		long long int ans = 0;
		cin >> n;
		REP( k , 0 , n ) scanf("%d",&a[k] );
		sort( a , a+n );
		int tmp1 = a[ 0 ];
		int tmp2  = 0 ;
		REP( k , 1 , n ) {
			tmp2 ^= a[ k ];
			ans += a[ k ];
		}
		if( tmp1 == tmp2 ) printf("Case #%d: %lld\n", cs++ , ans);
		else printf("Case #%d: NO\n" , cs++);
	}
	return 0;
}
