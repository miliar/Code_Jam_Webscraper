#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std ;
main()
{
	ios_base::sync_with_stdio(0) ;
	int tests ;
	string s   = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz" ;
	string s2  = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq" ;
	map<char, char> x ;
	for(int i = 0 ; i<s.size() ; i++) {
		x[ s[i] ] = s2[i] ;
	}
	cin >> tests ; cin.ignore() ;
	for(int test=1 ; test<=tests ; test++) {
		cout << "Case #" << test << ": " ;
		int N, S, p ;
		cin >> N >> S >> p ;
		int a=0, b=0 ;
		int x ;
		while(N--) {
			cin >> x ;
			if(x >= p+2*max(0,p-2)) {
				if(x>= p + 2*max(0,p-1)) a++ ;
				else b++ ;
			}
		}
		cout << a + min(S,b) << endl ;
	}
}
