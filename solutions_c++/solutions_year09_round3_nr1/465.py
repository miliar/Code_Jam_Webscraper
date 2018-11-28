
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
	FOR(l1,1,kases+1) {
		
		string a; 
		cin >> a;

		set<char> t;
		REP(i,a.size()) t.insert(a[i]);


		int base = max(2,(int )t.size());
		map < char , int > Value;
		
		Value[a[0]] = 1;int x= 0;
		FOR(i,1,a.size()) if(!Value.count(a[i])) {
			Value[a[i]] = x++;
			if(x == 1) ++x;
		}
		LL ans = 0;x = 0;
		for(int i = a.size() - 1 ; i >= 0 ; --i) {

			ans +=  Value[a[i]] * ((LL )pow((double )base,x*1.));
			++x;
		}
		cout << "Case #" << l1 << ": " << ans << endl;
	}	
	return 0;
}


