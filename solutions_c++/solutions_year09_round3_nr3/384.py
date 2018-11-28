
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


int main() {
	

	int kases; S(kases);
	REP(kk,kases) {

		int P,Q;
		cin >> P >> Q;

		VI t(Q);
		REP(i,Q) cin >> t[i];

		bool Prison[P];
		int ans = INF;
		do {
			memset(Prison,-1,sizeof Prison);
			int tem = 0,j,k = 0;	

			REP(i,Q) {
			
				int t1 = t[i] - 1;
				Prison[t1] = 0;
				j = t1 - 1;k = 0;
				while(j >= 0 && Prison[j]) --j,++k;j = t1 + 1;
				while(j < P && Prison[j]) ++j,++k;

				tem += k;
			}	
			ans = min (ans , tem);
		}while(next_permutation(ALL(t)));

		cout << "Case #" << kk+1 << ": "	 << ans << endl;
	}	
	return 0;
}


