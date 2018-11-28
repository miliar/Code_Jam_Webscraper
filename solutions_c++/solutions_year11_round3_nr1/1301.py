//#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std ; 

ifstream cin("a.in");
ofstream cout("a.out");

#define vs vector<string>
#define vb vector<bool>
#define vvb vector< vb >

void solve( vs & tiles , int C  ) ;
bool within_limit( int i , int j , int A , int B )  ;

int main() {

	int t ; 

	cin >> t ; 

	for ( int i = 0 ; i < t ; i ++ ) {
		int R , C ; 

		cin >> R >> C ; 

		vector<string> tiles ; 
		
		for ( int j = 0 ; j < R ; j ++ ) {
			string tile ; 
			cin >> tile ; 
			tiles.push_back( tile ) ; 
		//	solve(tiles,i+1);
		} 
		solve(tiles,i+1);
	}
	return 0 ; 
}

void solve( vs & tiles , int CCC  ) {

	vvb used ( tiles.size() , vb ( tiles[0].size() , false ) ) ;  

	int RR = tiles.size() ; 
	int CC = tiles[0].size() ; 
	
	int R [] = { 0 , 0 , 1 , 1 } ; 
	int C [] = { 0 , 1 , 0 , 1 } ; 
	//string s = "/\\/" ; 
	
	for ( int i = 0 ; i < tiles.size() ; i ++ ) {
		for ( int j = 0 ; j < tiles[0].size() ; j ++ ) {
			int tot = 0 ; 
			if ( tiles[i][j] == '#' && used[i][j] == false ) {
				for ( int k = 0 ; k < 4 ; k ++ ) {
					int n_r = i + R[ k ] ; 
					int n_c = j + C[ k ] ;

					if ( within_limit(n_r,n_c , RR , CC) ) {
						if ( tiles[n_r][n_c] == '#' ) tot ++ ;
					}
				}

				if ( tot == 4 ) {
					for ( int k = 0 ; k < 4 ; k ++ ) {
						int n_r = i + R[ k ] ; 
						int n_c = j + C[ k ] ; 

						used[n_r][n_c] = true ; 
						if ( k == 0 ) tiles[n_r][n_c] = '/' ;
						if ( k == 1 ) tiles[n_r][n_c] = '\\' ;
						if ( k == 2 ) tiles[n_r][n_c] = '\\';
						if ( k == 3 ) tiles[n_r][n_c] = '/' ; 
					}
				}			
			}
		}
	}

	bool possible = true ; 

	for ( int i = 0 ; i < RR ; i ++ ) {
		for ( int j = 0 ; j < CC ; j ++ ) {
			if ( tiles[i][j] == '#' ) { possible = false ; break ; }
		}
	}

	if ( possible == false ) {
		cout<<"Case #"<<CCC<<":"<<endl<<"Impossible"<<endl;
	}

	else {
		cout<<"Case #"<<CCC<<":"<<endl;

		for ( int i = 0 ; i< RR ; i ++ ) {
			for (int j = 0 ; j < CC ; j ++ ) {
				cout<<tiles[i][j];
			}
			cout<<endl;
		}
	}	

}

bool within_limit( int i , int j , int A , int B ) {
	if ( i < A && j < B ) return true ; 
	return false ; 
}
