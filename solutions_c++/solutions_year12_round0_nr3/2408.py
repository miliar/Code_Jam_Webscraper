#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std ;
int dl(int x) {
	if(x==0) return 0 ;
	else return 1+dl(x/10) ;
}
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	cin >> tests ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		int A, B ;
		cin >> A >> B ;
		int odp = 0 ;
		int l = dl(A) ;
		int dzies = 1 ;
		while(dl(dzies*10) <= l) dzies *= 10 ;
		for(int x=A ; x<=B ; x++) {
			set<int> zbior ;
			int k = 10 ;
			int p = dzies ;
			for(int i=1 ; i<l ; i++) {
				int y = (x/k) + (x%k)*p ;
				if(y >= A && y <= B && x<y) zbior.insert(y) ;
				k *= 10 ;
				p /=10 ;
			}
			odp += zbior.size() ;
		}
		cout << odp << endl ;
	}
}
