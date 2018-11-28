#include <iostream>
#include <fstream>
#include <map>
#include <stack>
#include <memory.h>
#include <string>
using namespace std ;

bool vi[900] ;
bool jk[900] ;
int main () {
	//freopen("B-small-attempt0.in","r",stdin) ;
	freopen("B-large.in","r",stdin) ;
	freopen("op.out","w",stdout) ;
	
	
	// ------------  variables    ----------------
	int t,n ;
	int s,p ;
	int a[500] ;
	//--------------------------------------------
	
	scanf ( "%d" , &t ) ;
	for ( int k = 1 ; k <= t ; ++k ) {
		//-------------- do -------------------
		scanf ( "%d %d %d" , &n,&s,&p ) ;
		p *= 3 ;
		int ans = 0 ;
		for ( int i = 0 ; i < n ; ++i ) {
			scanf ( "%d" , &a[i] ) ;
			if ( p < 3 ) {
				++ans ;
			}
			else if ( p == 3 ) {
				if ( a[i] ) ++ans ;
			}
			else if ( a[i] >= p-2 ) ++ans ;
			else if ( a[i] >= p-4 && s ) {
				++ans ;
				--s ;
			}
		}
		//--------------------------------------
		//=============================================
		//-------------- output ----------------
		printf ( "Case #%d: " , k ) ;
		
		printf ( "%d\n" , ans ) ;
		//--------------------------------------
	}
	//system("pause") ;
	return 0 ;
}
