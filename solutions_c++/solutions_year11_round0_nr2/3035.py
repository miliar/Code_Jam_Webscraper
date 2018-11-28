#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <map>
using namespace std ;

int main () {
	int t,n,m,k ;
	int i,j ;
	char x,y,z ;
	long long p ;
	char a[800];
	
	freopen ( "B-small-attempt0.in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;
	
	map<char,char> mp ;
	map<char,char> op ;
	map<string,char> fp ;
	cin>>t ;
	for ( k = 1 ; k <= t ; ++k ) {
		cin>>n;
		for ( i = 0 ; i < n ; ++i ) {
			cin>>x>>y>>z ;
			mp[x] = y ;
			mp[y] = x ;
			string s="" , ss="" ;
			s[0] = x ;
			s[1] = y ;
			ss[0] = y ;
			ss[1] = x ;
			
			fp[s] = fp[ss] = z ;
		}
		cin>>m;
		for ( i = 0 ; i < m ; ++i ) {
			cin>>x>>y ;
			op[x] = y ;
			op[y] = x ;
		}
		cin>>n;
		cin>>x ;
		a[0] = x ;
		for ( i = 1 ; i < n ; ++i ) {//  --i && --n 
			cin>>x ;
			a[i] = x ;
			if ( mp[x] == a[i-1] || mp[a[i-1]] == x ) {
				string s="" ;
				s[0] = x ;
				s[1] = y ;
				a[i-1] = fp[s] ;
				--i ;
				--n ;
			}
			else {
				for ( j = 0 ; j < i ; ++j ) {
					if ( op[x] == a[j] || op[a[j]] == x ) {
						n -= (i+1) ;
						if ( n <= 0 ) goto Mark ;
						i = 0 ;
						cin>>a[0] ;
						break ;
					}
				}
			}
		}
	//	cout<<a[0]<<' '<<op['Q']<<' '<<op['F']<<endl;
Mark:	cout<<"Case #"<<k<<": "<<"[";
		if ( n ) cout<<a[0];
		for ( i = 1 ; i < n ; ++i ) cout<<", "<<a[i];
		cout<<"]"<<endl;
		mp.clear() ;
		op.clear() ;
	}
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
