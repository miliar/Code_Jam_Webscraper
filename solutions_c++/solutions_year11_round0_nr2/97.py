#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <stack>
#include <deque>
using namespace std ;

int main()
{
	freopen("C:/Projects/Google Code Jam/Qualification/b/B-large.in","r",stdin);
	freopen("C:/Projects/Google Code Jam/Qualification/b/B-large.out","w",stdout);
	int t ; 
	cin >> t ;
	for ( int tests = 1 ; tests <= t ; ++tests )
	{
		map<pair<char,char>, bool> haspair, opposed ;
		map<pair<char,char>, char> pairname ;
		int c, d, n ;
		string a ;
		cin >> c ;
		for ( int i=0 ; i<c ; ++i )
		{
			cin >> a ;
			haspair[make_pair(a[0],a[1])] = haspair[make_pair(a[1],a[0])] = true ;
			pairname[make_pair(a[0],a[1])] = pairname[make_pair(a[1],a[0])] = a[2] ;
		}
		cin >> d ;
		for ( int i=0 ; i<d ; ++i ) 
		{
			cin >> a ;
			opposed[make_pair(a[0],a[1])] = opposed[make_pair(a[1],a[0])] = true ;
		}
		deque<char> l ;
		cin >> n >> a ;
		for ( int i=0 ; i<n ; ++i )
		{
			l.push_back(a[i]);
			while (l.size()>=2 && haspair[make_pair(l.back(), *(l.end()-2))] )
			{
				char tmp = pairname[make_pair(l.back(), *(l.end()-2))] ;
				l.pop_back(); l.pop_back(); l.push_back(tmp);
			}
			for ( int j=0 ; j<l.size()-1 ; ++j ) 
				if ( opposed[make_pair(l.back(),l[j])] ) 
				{
					l.clear() ;
					break ;
				}
		}
		printf("Case #%d: [",tests);
		for ( int i=0 ; i<int(l.size())-1 ; ++i )  
			cout << l[i] << ", " ;
		if (!l.empty() ) cout << l.back() ;
		cout << "]\n" ;
	}
}