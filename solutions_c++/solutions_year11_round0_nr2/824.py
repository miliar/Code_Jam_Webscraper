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

char t[200][200] ;
bool zle[200][200] ;

main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		memset(t,0,sizeof(t)) ;
		memset(zle,0,sizeof(zle)) ;
		int C,D,N ;
		char a, b, c ;
		cin >> C ;
		while(C--) {
			cin >> a >> b >> c ;
			t[a][b] = c ;
			t[b][a] = c ;
		}
		cin >> D ;
		while(D--) {
			cin >> a >> b ;
			zle[a][b] = zle[b][a] = true ;
		}
		vector<int> napis ;
		char x ;
		cin >> N ;
		while(N--) {
			cin >> x ;
			if(napis.empty()) napis.PB(x) ;
			else {
				if(t[x][napis.back()]) napis[napis.size()-1] = t[x][napis.back()] ;
				else {
					FOREACH(q, napis) {
						if(zle[*q][x]) {
							napis.clear() ;
							break ;
						}
					}
					if(!napis.empty()) napis.PB(x) ;
				}
			}
		}
		cout << "[" ;
		for(int i=0 ; i<napis.size() ; i++) {
			cout << (char) napis[i] ;
			if(i != napis.size()-1) cout << ", " ;
		}
		cout << "]" << endl ;
	}
}

