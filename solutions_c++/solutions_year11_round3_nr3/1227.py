//#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std ; 

ifstream cin("a.in");
ofstream cout("a.out");

int GCD(int a, int b); 
void solve( vector<int> & others , int L , int H , int c) ; 

#define vs vector<string>
#define vb vector<bool>
#define vvb vector< vb >

int main() {

	int T ; 

	cin >> T ; 

	for ( int i = 0 ; i < T ; i ++ ) {
		int N , L , H ;

		cin >> N >>L >> H ; 
		 
		vector<int> others ; 

		
		for ( int j = 0 ; j < N ; j ++ ) {
			int other ; 
			cin >> other ;
			others.push_back( other ) ; 
		}

		solve(others , L , H , i + 1) ;
	}
}

void solve( vector<int> & others , int L , int H , int c) {

	int G = 0 ; 
	
/*	if ( others.size() == 1 ) G = others[0] ; 

	G = GCD ( others[0],others[1] ) ; 
	G = ( others[0] * others[1] ) / G ; 

	int GG = 0 ; 
	for ( int i = 2 ; i < others.size() ; i ++ ) {
		GG = GCD ( G , others[i] ) ;
		G = ( G * others[i] ) / GG ;  		
	}
*/
	int v = -1 ; 

	for ( int i = L ; i <= H ; i ++ ) {
		bool found = true ; 

		for ( int j = 0; j < others.size() ; j ++ ) {
			if ( others[j] % i != 0 && i % others[j] != 0 ) {
				found = false ; 
				break ; 
			}
		}

		if ( found == true ) {
			v = i ; 
			break ;
		}
	}
//	cout<<G<<endl;	
/*	for ( int i = L ; i <= H ; i ++ ) {
		//int g = GCD ( G , i ) ; 

		if ( i % G == 0 || G % i == 0 ) { v = i ; break ; }
		//if ( g == G || g == i ) { v = i ; break ; } 
	}
*/
	if ( v == -1 ) {
//		Case #1: NO
		cout<<"Case #"<<c<<": NO"<<endl;
	}

	else {
		cout<<"Case #"<<c<<": "<<v<<endl;
	}
//	}
}

int GCD(int a, int b)
{
   if (b==0) return a;
   return GCD(b,a%b);
}

