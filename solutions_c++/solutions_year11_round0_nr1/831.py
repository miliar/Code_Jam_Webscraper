#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <cstring>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;
typedef long long LL ;
const int INF = 1000*1000*1000 ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
int przesun(int a, int b) {
	if(a == b) return a ;
	else if(a<b) return a+1 ;
	else return a-1 ;
} 
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		int n, i, j, x ;
		char co ;
		cin >> n ;
		queue<int> a, b ;
		vector< pair<char, int> > t ;
		REP(i,n) {
			cin >> co >> x ;
			t.PB(MP(co,x)) ;
			if(co=='O') a.push(x) ;
			else b.push(x) ;
		}
		a.push(INF) ;
		b.push(INF) ;
		int gdzie1 = 1, gdzie2 = 1 ;
		int s=0 ;
		for(i=0 ; i<t.size() ; ) {
			s++ ;
		//	cout << t[i].FI << " " << t[i].SE << endl ;
			if(t[i].FI == 'O') {
				if(gdzie1 == t[i].SE) {
					i++ ;
					a.pop() ;
				}
				else gdzie1 = przesun(gdzie1, a.front()) ;
				gdzie2 = przesun(gdzie2, b.front()) ;
			}
			else {
				if(gdzie2 == t[i].SE) {
					i++ ;
					b.pop() ;
				}
				else gdzie2 = przesun(gdzie2, b.front()) ;
				gdzie1 = przesun(gdzie1, a.front()) ;
			}
		}
		cout << s << endl ;
	}
}

