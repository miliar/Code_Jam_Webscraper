/*
 * Tongues.cpp
 *
 *  Created on: Apr 15, 2012
 *      Author: swem
 */

#include<iostream>
#include<string>
#include<map>
using namespace std;

int main()
{
	map<char,char> m ;
	string str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv" ;
	string str2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up" ;
	string buffer ;
	for( int i = 0 ; i < 26 ; i++ ) {
		m[ 'a'+i ] = 'a'+i ;
	}
	for( int i = 0 ; i < str1.length() ; i++ ) {
		m[ str1[ i ] ] = str2[ i ];
	}
	m[ 'z' ] = 'q' ;
	m[ 'q' ] = 'z' ;
	m[ ' ' ] = ' ' ;

	int t ;
	cin >> t ;
	getline( cin, buffer ) ;
	for( int caseidx = 1 ; caseidx <= t ; caseidx++ ) {
		string answer ;
		getline( cin, buffer ) ;
		for( int i = 0 ; i < buffer.length() ; i++ ) {
			answer += m[ buffer[ i ] ];
		}

		cout << "Case #" << caseidx << ": " << answer << endl ;
	}
	return 0 ;
}
