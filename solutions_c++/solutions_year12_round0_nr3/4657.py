#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std ; 

int add( int low , int cur ) {
	ostringstream oss ;
	oss << cur ;
	
	string num = oss.str() ; 
	
	vector<int> nb ; 
	
	for ( int i = 1 ; i < num.size() ; i ++ ) {
		string e = num.substr( 0 , i ) ;
		string b = num.substr( i ) ;
		
		if ( b[ 0 ] == '0' ) continue ; 
		
		string ul = b + e ;
		
		istringstream iss( ul ) ; 
		
		int N ; 
		
		iss >> N ; 
		
		nb.push_back( N ) ;
	}
	
	int sum = 0 ; 
	
	for ( int i = 0 ; i < nb.size() ; i ++ ) {
		if ( nb[ i ] < cur && nb[ i ] >= low ) sum ++ ;
	}
	
	return sum ; 
}

int solve( int A , int B ) {
	
	int res = 0 ;
	
	for ( int i = A + 1 ; i <= B ; i ++ ) {
		int tmp = add( A , i ) ;
		
		res += tmp ; 
		
	//	cerr << i << " " << tmp << endl ;
	}
	
	return res ;
}

int main() {
	
	int T ; 
	
	cin >> T ; 
	
	int A , B ; 
	
	for ( int i = 0 ; i < T ; i ++ ) {
		cin >> A >> B ; 
		
		int res = solve( A , B ) ;
		
		cout << "Case #" << i + 1 << ": " << res << endl ;
	}
	
	return 0 ;
}
