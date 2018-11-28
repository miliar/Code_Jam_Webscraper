#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <sstream>
#include <limits.h>
#include <cassert>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cstring>

using namespace std;

#define FOR(i,n) for(int i = 0 ; i < n ; i++)
#define FOZ(i,v) FOR(i,int(v.size()))
#define rep(i,x,y) for(int i=(x);   \
	( i )<=( (y)); i ++)
typedef vector<vector< int> > vvi;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define vv(T) vector< vector < T > >
#define Sort(v) sort(v.begin(),v.end());

struct node { 
	int g; 
	int c; 
	int val ;
};

bool isgate(int a, int m ) { 
	return a <= (m-1)/2 ; 
}

void test(int __case) { 
	int m, v; 
	cin >> m >> v; 
	vector<node> ar;
	node buh; 
	ar.push_back(buh);

	FOR(i, ((m-1)/2)) { 
		node t ; 
		cin >> t.g >> t.c; 
		ar.push_back(t) ;
	}

	FOR(i, ((m+1)/2)) { 
		node t; 
		cin >> t.val ; 
		t.g = -1;
		ar.push_back(t) ;
	}
	
	int best[2*m+1][2] ;
	FOR(i,2*m+1) FOR(j,2) { 
		best[i][j] = 20000;
	}
	for(int i = m ; i > 0 ; i-- ) { 
		if ( !isgate(i, m) ) {
			best[i][ar[i].val] = 0 ; 
			best[i][!ar[i].val] = 20000;
			continue;
		}

		int costforand = (ar[i].g != 1 ); 
		int costforor = (ar[i].g != 0 );
		if ( ar[i].c == 0 ) { 
//			printf(">> %d\n", i);
			/* not changeable, let's just fix the values */
			if ( ar[i].g == 0 ) 
				costforand = 20000; 
			else if ( ar[i].g == 1 ) 
				costforor = 20000 ; 
			else assert(false);
		}
		/* gate being AND, and to get 0 */
		best[i][0] = INT_MAX ;
		best[i][0] = min(best[i][0], best[2*i][1]+ best[2*i+1][0]+costforand);
		best[i][0] = min(best[i][0], best[2*i][0]+ best[2*i+1][1]+costforand);
		best[i][0] = min(best[i][0], best[2*i][0]+ best[2*i+1][0]+costforand);


		/* being OR, and to get 0 */
		best[i][0] = min(best[i][0], best[2*i][0]+best[2*i+1][0] + costforor);

		/* to get a 1 */
		best[i][1] = INT_MAX ;
		best[i][1] = min(best[i][1], best[2*i][1]+ best[2*i+1][1]+costforand);


		/* get a 1 with an OR */
		best[i][1] = min(best[i][1], best[2*i][1]+ best[2*i+1][0]+costforor);
		best[i][1] = min(best[i][1], best[2*i][0]+ best[2*i+1][1]+costforor);
		best[i][1] = min(best[i][1], best[2*i][1]+ best[2*i+1][1]+costforor);
		

		if ( best[i][0] > 20000 ) best[i][0] = 20000 ; 
		if ( best[i][1] > 20000 ) best[i][1] = 20000 ;
	}

	printf("Case #%d: ", __case);
	if ( best[1][v] >= 20000 ) printf("IMPOSSIBLE\n") ;
	else printf("%d\n", best[1][v]) ;
}
int main() {

	int t; 
	scanf("%d", &t);
	FOR(i,t) test(i+1) ;
	return 0;
}
