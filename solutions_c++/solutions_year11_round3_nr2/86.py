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

const int maxn = 1000100 ;
const double eps = 1e-9 ;

int n , a[maxn] , C , L;
double leg[maxn] ;
lint t ; 

lint solve(){
	lint all = 0 ;
	for(int i=0;i<n;++i)all += a[i] ;
	if(all <= t/2)return all*2 ;
	//all > t/2 , find which at which leg the builds complete.
	all = 0 ;int x = -1 ;lint rem = -1 ;
	lint ans = 0 ;
	for(int i=0;i<n;i++){
		all += a[i] ;
		if(all > t/2) {
			x = i ;
			rem = all - t/2 ;
			ans += (a[i] - rem)*2 ;
			break ;
		}
		else{
			ans += a[i] + a[i] ;
		}
	}
	vector<lint> vt ;
	vt.PB(rem);
	for(int i=x+1;i<n;++i)
		vt.PB(a[i]);
	sort(ALL(vt));reverse(ALL(vt));
	for(int i=0;i<SZ(vt);++i){
		if(L>0){
			ans += vt[i] ;
			L -- ;
		}
		else ans += vt[i] * 2 ;
	}
	return ans ;
}

int main(){
	int cas ;
	cin >> cas ;
	for(int cs=1; cs <= cas ; cs++){
		cin >> L >> t >> n >> C ;
		for(int c=0;c<C;c++)cin >> a[c] ;
		for(int c=C;c<n;c++)a[c] = a[c%C] ;
		cout << "Case #" << cs << ": " << solve() << endl ;	
	}
	return 0 ;
}
