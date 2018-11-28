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
	freopen("A-small-attempt2.in","r",stdin) ;
	//freopen("A-large-practice.in","r",stdin) ;
	//freopen("B-small-practice.in","r",stdin) ;
	//freopen("B-large-practice.in","r",stdin) ;
	//freopen("C-small-practice.in","r",stdin) ;
	//freopen("C-large-practice.in","r",stdin) ;
	//freopen("D-small-practice.in","r",stdin) ;
	//freopen("D-large-practice.in","r",stdin) ;
	
	freopen("op.out","w",stdout) ;
	
	string s[3],w[3] ;
	char google[900] ;
	s[0] = "our language is impossible to understand" ;
	s[1] = "there are twenty six factorial possibilities" ;
	s[2] = "so it is okay if you want to just give up" ;
	w[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi" ;
	w[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" ;
	w[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv" ;
	for ( int j = 0 ; j < 3 ; ++j ) {
		for ( int i = 0 ; i < s[j].size() ; ++i ) {
			google[w[j][i]] = s[j][i] ;
			vi[s[j][i]] = 1 ;
			jk[w[j][i]] = 1 ;
		}
	}
	google[int('q')] = 'z' ;
	google[(int)('z')] = 'q' ;
	// ------------  variables    ----------------
	int t,n ;
	string str ;
	
	//--------------------------------------------
	
	scanf ( "%d" , &t ) ;
	scanf ( "\n" ) ;
	for ( int k = 1 ; k <= t ; ++k ) {
		//-------------- do -------------------
		getline(cin,str) ;
		
		
		//--------------------------------------
		//=============================================
		//-------------- output ----------------
		printf ( "Case #%d: " , k ) ;
		for ( int i = 0 ; i < str.size() ; ++i ) 
			printf ( "%c" , google[str[i]] ) ;
		printf ( "\n" ) ;
		//--------------------------------------
	}
	//system("pause") ;
	return 0 ;
}
