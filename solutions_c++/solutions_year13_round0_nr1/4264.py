// Author: Nishant R. Krishan
#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <deque>
#include <bitset>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>

using namespace std;

#define VI vector < int >
#define VVI(A,N,M) vector< VI > A( N, VI (M) )
#define LL long long
#define LLU unsigned long long
#define SI ({int x;scanf("%d",&x);x;})
#define SC ({char x;scanf("%c",&x);x;})
#define SLL ({LL x;scanf("%lld",&x);x;})
#define SLLU ({LLU x;scanf("%llu",&x);x;})
#define PI acos(-1)
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size()) 
#define SORT(c) sort(all(c)) 
#define FIT(it,v) for (typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define FITD(it,v) for (typeof(v.rbegin()) it = v.rbegin(); it != v.rend(); it++)
#define IATOV(a) ({vector<int> v(a,a+sizeof(a)/sizeof(int));v;})
#define CATOV(a) ({vector<char> v(a,a+sizeof(a)/sizeof(char));v;})
#define sieve(a) ({int b=ceil(sqrt(a));VI d(a,0);VI e;int f=2;e.pb(2);e.pb(3);for(int x=1;x<b+1;x++){for(int y=1;y<b+1;y++){int n=(4*x*x)+(y*y);if(n<=a&&(n%12==1||n%12==5)){d[n]^=1;}n=(3*x*x)+(y*y);if(n<=a&&n%12==7){d[n]^=1;}n=(3*x*x)-(y*y);if(x>y&&n<=a&&n%12==11){d[n]^=1;}}}for(int r=5;r<b+1;r++){if(d[r]){for(int i=r*r;i<a;i+=(r*r)){d[i]=0;}}}for(int c=5;c<a;c++){if(d[c]){e.pb(c);}}e;})
#define INF 1000000007
#define EPS 1e-9

/********************************************************************************************************************************/

int main(int argc, char** argv) {
	vector<string> Game(4);
	int i,j;
	int T=SI,t;
	bool completed, xwon, owon;
	for( t=1;t<=T;++t ){
		printf("Case #%d: ", t);

		completed = true;
		xwon = false;
		owon = false;

		for(i=0;i<4;++i)
			cin>>Game[i];

		for( i=0;i<4;++i ){
			for( j=0;j<4;++j ){
				if( Game[i][j]=='.' )
					break;
			}
			if(j<4)
				break;
		}
		if( i<4 )
			completed = false;

		for( i=0;i<4;++i ){
			for( j=0;j<4;++j ){
				if( Game[i][j]!='X' && Game[i][j]!='T' )
					break;
			}
			if( j==4 )
				xwon = true;
			for( j=0;j<4;++j ){
				if( Game[j][i]!='X' && Game[j][i]!='T' )
					break;
			}
			if( j==4 )
				xwon = true;
			for( j=0;j<4;++j ){
				if( Game[i][j]!='O' && Game[i][j]!='T' )
					break;
			}
			if( j==4 )
				owon = true;
			for( j=0;j<4;++j ){
				if( Game[j][i]!='O' && Game[j][i]!='T' )
					break;
			}
			if( j==4 )
				owon = true;
		}
		for( i=0;i<4;++i ){
			if( Game[i][i]!='X' && Game[i][i]!='T' )
				break;
		}
		if( i==4 )
			xwon = true;
		for( i=0;i<4;++i ){
			if( Game[i][i]!='O' && Game[i][i]!='T' )
				break;
		}
		if( i==4 )
			owon = true;
		for( i=0;i<4;++i ){
			if( Game[i][3-i]!='X' && Game[i][3-i]!='T' )
				break;
		}
		if( i==4 )
			xwon = true;
		for( i=0;i<4;++i ){
			if( Game[i][3-i]!='O' && Game[i][3-i]!='T' )
				break;
		}
		if( i==4 )
			owon = true;
		
		if( xwon ){
			printf("X won\n");
		}
		else if( owon ){
			printf("O won\n");
		}
		else if(completed){
			printf("Draw\n");
		}
		else{
			printf("Game has not completed\n");
		}
	}
	return 0;
}

