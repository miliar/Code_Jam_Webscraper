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

const int maxs = 55 ;

string g[maxs] ;
int R , C ;

int solve(){
	for(int r=0;r<R;++r)
		for(int c=0;c<C;c++)
			if(g[r][c] == '#'){
				if(c+1 >= C or r+1 >= R or g[r][c+1] != g[r][c] or g[r+1][c] != g[r][c] or 
					g[r+1][c+1] != g[r][c])return false ;
				g[r][c] = '/' ; g[r][c+1] = '\\' ;
				g[r+1][c] = '\\' ; g[r+1][c+1] = '/' ;
			}
	return true ;
}

int main(){
	int T ; 
	cin >> T ;
	for(int t=1;t <= T ; t++){
		cin >> R >> C ;
		for(int r=0;r<R ; r++)
			cin >> g[r] ;
		cout << "Case #" << t << ":" << endl;
		if(!solve()){
			cout << "Impossible" << endl ;
		}
		else{
			//cout << endl ;
			for(int r=0;r<R;r++)
				cout << g[r] << endl;
		}
	}
	return 0 ;
}
