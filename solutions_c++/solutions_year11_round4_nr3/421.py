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

const lint maxn = 1000000000000LL ;

const int maxp = 1000100 ;
bool ps[maxp] ;

void init(){
	memset(ps,true,sizeof ps);
	ps[0]=ps[1]=false;
	for(int i=2;i*i <= maxp; ++i)if(ps[i])
		for(int j=i*i;j < maxp ; j += i)
			ps[j] = false ;
	return ;
}

lint solve2(lint n){
	//min
	lint res = 0 , last = 0;
	for(int a = 2 ; (1LL<<a) <= n ; a++){
		int p = (int)pow(n,1.0/a);
		for(int x = last+1; x <= p ; x ++ ) if(ps[x] )
			last = x , res ++ ;
	}
	return res ;
}


lint solve1(lint n){
	lint res = 1, last = 0;
	for(int a = 2  ;(1LL<<a) <= n ; a++){
		int p = (int)pow(n,1.0/a);
		for(int x = last+1 ; x <= p ; x ++)if(ps[x])
			res += a , last = x;
	}
	return res ;
}

lint solve(lint n){
	if(n == 1)return 0 ;
	lint res = 0 ;
	for(int p=2;p <= n/p;p++)
		if(ps[p]){
			res -- ;
			for(lint t=1,a=0;t <= n/p;t *= p , a++, res++) ;
		}
	return ++res ;
}

int main(){
	init();
	int cas ;
	cin >> cas ;
	for(int cs = 1 ;cs <= cas ; cs ++ ){
		lint n ;
		cin >> n ;
		cout << "Case #" << cs << ": " << solve(n ) << endl ;
	}
	return 0 ;
}
