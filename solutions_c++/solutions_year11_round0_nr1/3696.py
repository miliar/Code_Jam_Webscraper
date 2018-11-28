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
	int t , n , cnt = 1;
	scanf("%d",&t);
	while ( t-- ) {
		int n , button , posb = 1, poso = 1 , tot = 0 , last = 0 , t1  = 0 , t2 = 0;
		char ch;
		scanf("%d",&n);
		for( int i = 0 ; i < n ; i++ ) {
			cin >> ch >> button;
			
			if( ch == 'B' ) {
//				cout << t1 << endl;
				t1 = max( t1+abs( button - posb )+1 , t2 + 1 );
				posb = button;
			}
			if( ch == 'O' ) {
//				cout << t2 << endl;
                		 t2 = max( t2+abs( button - poso )+1 , t1 + 1 );	
				  poso = button;
                        }

		}
		tot = max( t1 , t2 );
		printf("Case #%d: %d\n",cnt++ , tot);
	}

	return 0;
}
