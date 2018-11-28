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
#include <string.h>

using namespace std;

#define REP(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define ll long long int
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()

int main()
{
	int t , cs = 1 , n;
	cin >> t;ll a[101] , l , h ;
	while( t-- ) {
		cout<<"Case #"<<cs<<": ";cs++;
		cin>>n>>l>>h;REP( i , 0 , n ) scanf("%lld",&a[i]);
		ll gd = a[0] , lc = a[0] , ans;
		REP( i , 1 , n ) { gd=__gcd(gd,a[i]);lc*=a[i];}
		lc = lc / gd;lc = max(lc , l);gd  = min(h , gd); 
		bool fin = 0;
		for( ll i = l; i <= h ;i++ ) {
			bool f = 1;
			REP( j , 0 , n ) {
				if((a[j]%i !=0)&&(i%a[j]!=0)) f = 0;
			}
			if(f) {
				ans = i;fin = 1;break;
			}
		}
		if(fin) printf("%lld\n",ans);
		else printf("NO\n");
	}
	return 0;
}
