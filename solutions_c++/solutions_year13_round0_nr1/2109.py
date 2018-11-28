#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <stdio.h>
#include <cmath>
#include <math.h>
#include <queue>

using namespace std;

int whowin( string p[] ){
		map< char , int > res ;
		res.clear() ;
		for( int i=0 ; i<4 ; i++ )	res[p[i][i]]++ ;
		if( ( res['X']==3 && res['T']==1 ) || res['X']==4 )			return 1 ;
		else if( ( res['O']==3 && res['T']==1 ) || res['O']==4 )	return 2 ;
		//----------------------------------------------------------------------
		res.clear() ;
		res[p[0][3]]++ ;	res[p[1][2]]++ ;	res[p[2][1]]++ ;	res[p[3][0]]++ ;
		if( ( res['X']==3 && res['T']==1 ) || res['X']==4 )			return 1 ;
		else if( ( res['O']==3 && res['T']==1 ) || res['O']==4 )	return 2 ;
		//----------------------------------------------------------------------		
		for( int i=0 ; i<4 ; i++ ){
			res.clear() ;
			for( int j=0 ; j<4 ; j++ )	res[p[i][j]]++ ;
			if( ( res['X']==3 && res['T']==1 ) || res['X']==4 )			return 1 ;
			else if( ( res['O']==3 && res['T']==1 ) || res['O']==4 )	return 2 ;
		}
		//----------------------------------------------------------------------		
		for( int i=0 ; i<4 ; i++ ){
			res.clear() ;
			for( int j=0 ; j<4 ; j++ )	res[p[j][i]]++ ;
			if( ( res['X']==3 && res['T']==1 ) || res['X']==4 )			return 1 ;
			else if( ( res['O']==3 && res['T']==1 ) || res['O']==4 )	return 2 ;
		}
		//----------------------------------------------------------------------		
		for( int i=0 ; i<4 ; i++ ){
			for( int j=0 ; j<4 ; j++ ){		if( p[i][j]=='.' )	return 4 ;		}
		}
		//----------------------------------------------------------------------		
		return 3 ;
}

int main(){
	freopen("A-large-practice1.in.txt","rt",stdin) ;
	freopen("A-large-practice1.out.txt","wt",stdout) ;
	
	int t , l=1 , res ;
	string p[4] , x ;
	cin >> t ;
	while( t-- ){
		for( int i=0 ; i<4 ; i++ )	cin >> p[i] ;
		res=whowin( p ) ;
		if( res==1 )		x=": X won" ;
		else if( res==2 )	x=": O won" ;
		else if( res==3 )	x=": Draw" ;
		else				x=": Game has not completed" ;
		cout << "Case #" << l << x << endl ;
		l++ ;
	}
	//--------------------------------------------------------------------------
	//--------------------------------------------------------------------------
	//freopen("A-small-practice1.in.txt","rt",stdin) ;
	//freopen("A-small-practice1.out.txt","wt",stdout) ;
	//--------------------------------------------------------------------------
	return 0 ;
}
