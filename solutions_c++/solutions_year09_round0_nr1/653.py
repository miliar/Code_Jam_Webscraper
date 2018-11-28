
/* Author :: Yash */
#include <vector>
#include <list>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <deque>
#include <fstream>
#include <stack>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define PP pop()
#define EM empty()
#define INF 1000000000
#define PF push_front
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define V(x) vector< x >
#define Debug false
#define PRINT(x)        cout << #x << " " << x << endl
#define LET(x,a) 	    __typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define SZ(x) 		x.size();
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define D(N) 		int N
#define S(N)		scanf("%d",&N)

typedef pair<int,int>  PI;
typedef pair<int,PI>   TRI;
typedef V( int )       VI;
typedef V( PI  )       VII;
typedef V( string )    VS;
typedef long long      LL;

int L , D ,N;

// L == 15.
// D == 5000.
// N == 500.

VS Inp(5100);
bool Pattern[15][30];

void GetInp(int l) {

	char c;
	scanf(" %c",&c);
	if ( c != '(' ) Pattern[l][c - 'a'] = 1;
	else {
		while ( (c = getchar()) != ')' ) Pattern[l][c - 'a'] = 1;
	}
}

bool Find(int j) { 


	assert ( Inp[j].size() == L );
	if ( Inp[j].size() != L ) return false;
	REP(i,L) {
		if ( !Pattern[i][Inp[j][i] - 'a'] ) return false;	
	}
	return true;
}
int main() {
	
	scanf("%d%d%d",&L,&D,&N);
	REP(i,D) cin >> Inp[i];
	
	int ans = 0;
	REP(i,N) {
		memset(Pattern,0,sizeof Pattern);
		// Take The Pattern.
		REP(j,L) GetInp(j);
		ans = 0;
		REP(j,D) {
			// Check If Found().
			ans += Find(j); 
		}
		printf("Case #%d: %d\n",i+1,ans);
	}

	return 0;
}


