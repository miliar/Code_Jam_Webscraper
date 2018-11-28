#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <deque>
#include <cmath>
#include <queue>
#include <sstream>

using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define FOREACH(it,v) for(typeof(v.begin()) it=v.begin();it != v.end();it++)
#define FORN(i,x,y) for(int i=(x);i<(y);++i)
#define FOR(i,x) FORN(i,0,x)
#define ALL(a) (a).begin(),(a).end()
#define SET(x,a) memset(x,a,sizeof x)
#define VEC vector
#define PB push_back
#define MP make_pair

template<class T,class U> inline void checkmin(T& x,U y){x=min(x,(T)y);};
template<class T,class U> inline void checkmax(T& x,U y){x=max(x,(T)y);};

const int maxn = 105 ;
int L , H , F[maxn] , n ;

string solve(){
	for(;L <= H ; L++){
		int yes = true ;
		for(int i=0;i<n;++i) yes &= F[i]%L==0 | L%F[i]==0;
		if(yes){
			ostringstream os;
			os << L ;
			return os.str();
		}
	}
	return "NO" ;
}

int main(){
	int T ;
	cin >> T ;
	for(int t=1;t <= T ; t++){
		cin >> n >> L >> H ;
		for(int i=0;i<n;i++)cin >> F[i];
		cout << "Case #" << t << ": " << solve() << endl ;
	}
	return 0 ;
}
