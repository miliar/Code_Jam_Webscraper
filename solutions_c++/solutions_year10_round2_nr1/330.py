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
#include <sstream>
#include <ext/numeric>
using namespace std ;
using namespace __gnu_cxx ;

typedef long long LL ;
const int INF = 1000000000 ;

#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

struct tree {
	map<string, tree> napis ;
} ;

char folder[10000000] ;

main()
{
	ios_base::sync_with_stdio(0) ;
	int C ;
	cin >> C ;
	for(LL cc=1 ; cc<=C ; cc++) {
		cout << "Case #" << cc << ": " ;
		int N, M ;
		string sss ;
		char slesz ;
		cin >> N >> M ;
		tree root ;
		while(N--) {
			cin >> sss ;
			istringstream aaa(sss) ;
			tree* wsk = &root ;
			aaa >> slesz ;
			while(true) {
				if(aaa.eof()) break ;
				aaa.getline(folder, 1000000000, '/') ;
				wsk = &wsk->napis[folder] ;
			}
		}
		long long odp = 0 ;
		while(M--) {
			cin >> sss ;
			istringstream aaa(sss) ;
			tree* wsk = &root ;
			aaa >> slesz ;
			while(true) {
				if(aaa.eof()) break ;
				aaa.getline(folder, 1000000000, '/') ;
				if(wsk->napis.find(folder) == wsk->napis.end()) odp ++ ;
				wsk = &wsk->napis[folder] ;
			}
		}
		cout << odp << endl ;
	}
}

