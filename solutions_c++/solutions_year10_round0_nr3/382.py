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
const LL INF = 1000000000 ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
LL t[1100] ;
bool uzyte[1100] ;
main()
{
	ios_base::sync_with_stdio(0) ;
	LL C, i, j ;
	cin >> C ;
	for(LL cc=1 ; cc<=C ; cc++) {
		cout << "Case #" << cc << ": " ;
		LL R, k, N ;
		cin >> R >> k >> N ;
		memset(uzyte, 0, sizeof(uzyte)) ;
		REP	(i, N) cin >> t[i] ;
		vector<pair<LL, LL> > zysk ;
		i=0 ;
		while(zysk.size() < R) {
			//cout << "i = " << i << endl ;
			if(uzyte[i]) break ;
			LL razem = t[i] ;
			j = (i+1)%N ;
			while(j!=i && razem+t[j]<=k) {
				razem += t[j] ;
				j = (j+1)%N ;
			}
			zysk.PB(MP(razem,i)) ;
			uzyte[i] = true ;
			i = j ;
		}
		/*cout << "zysk :" ;
		FOREACH(q, zysk) cout << "(" << q->FI << " " << q->SE << ") "  ;
		cout << endl ;*/
		if(zysk.size() == R) {
			LL suma = 0 ;
			FOREACH(q, zysk) suma += q->FI ;
			cout << suma << endl ;
		}
		else {
			LL powtorzone = i ;
			LL rozbieg = 0 ;
			for(i=0 ; zysk[i].SE != powtorzone ; i++) rozbieg += zysk[i].FI ;
			//cout << "rozbieg = " << rozbieg << endl ;
			R -= i ;
			LL indeks = i ;
			//cout << "indesk = " << indeks << " R = " << R ;
			LL rozmiar = zysk.size()-indeks ;
			//cout << " rozmiar = " << rozmiar << endl ;
			LL reszta = 0 ;
			for(i=indeks ; i<zysk.size() ; i++) reszta += zysk[i].FI ;
			LL odp = rozbieg + (R/rozmiar)*reszta ;
			for(i=0 ; i< (R%rozmiar) ; i++) odp += zysk[indeks+i].FI ;
			cout << odp << endl ;
		}
	}
}

