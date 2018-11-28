//#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <fstream>
#include <numeric>

using namespace std ;

int get_num( vector<int> & a ) ; 
int solve(vector<int> &numbers ) ; 
int calculate( vector<int> & a , vector<int> & b ) ; 

ifstream cin("code.in");
ofstream cout("code.out");

int main() {

	int T ; 
	
	cin >> T ; 
	
	for ( int i = 0 ; i < T ; i ++ ) {

		int N ; 
		
		cin >> N ; 
		
		vector<int> numbers ; 
		
		for ( int j = 0 ; j < N ; j ++ ) {
			int num ; 
			cin >> num ; 
			numbers.push_back( num ) ; 
		}
		
		int num = solve(numbers) ;
		
		if ( num == -1 ) 
			cout<<"Case #"<<i+1<<": NO"<<endl; 
		else 
			cout<<"Case #"<<i+1<<": "<<num<<endl;	
	}
	
	return 0 ; 
}

int solve(vector<int> &numbers ) {

	int sz = numbers.size() ; 
	int mx = -1 ; 
	
	for ( int i = 1 ; i < ( 1 << sz ) - 1 ; i ++ ) {
		vector<int> zeros ; 
		vector<int> ones ; 
		
		for ( int j = 0 ; j < sz ; j ++ ) {
			if ( i & ( 1 << j ) ) {
				ones.push_back( numbers[j] ) ;
			}
			
			else zeros.push_back( numbers[j] ) ; 
			
			
		}
		
		mx = max( calculate(ones,zeros) , mx ) ; 
		
	}
	
	return mx ; 	
	
}

int calculate( vector<int> & a , vector<int> & b ) {
	int tot_a = get_num(a); 
	int tot_b = get_num(b) ; 
	
	if ( tot_a == tot_b ) {
//		cerr<<tot_a<<endl;
		int sum_a = accumulate(a.begin(),a.end(),0) ; 
		int sum_b = accumulate(b.begin(),b.end(),0) ; 
		
		return max(sum_a,sum_b) ; 
	}
	
	return -1 ; 
		
}

int get_num( vector<int> & a ) {

	int ret = 0 ; 
	
	for ( int i = 0 ; i < a.size() ; i ++ ) {
//		int tmp = 0 ; 
		for ( int j = 0 ; j < 20 ; j ++ ) {
			if ( ( a[ i ] & ( 1 << j ) ) && ( ret & ( 1 << j ) ) ) {
				ret = ret ^ ( 1 << j ) ;  
			
			}
			
			else if ( a[ i ] & ( 1 << j ) ) {
				ret = ret | ( 1 << j ) ; 
				//cerr<<" "<<ret<<endl;
			}
		}
	}
	
	/*
	cerr<<" hey look :P"<<endl;	
	for ( int i = 0 ; i < a.size() ; i ++ ) {
		cerr<<a[i]<<" ";
	}
	cout<<endl;
	cout<<" res is "<<ret<<endl;
	*/
	return ret ; 
}
