//#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std ; 

#define vd vector<double>
#define vvd vector< vd >
#define vs vector<string>

void print_result( vvd & vals , int c );
double calc_win(string &s ) ; 
double calc_owp(int i , string & s ) ; 
void solve(vs & teams , int c );

ifstream cin("A.in");
ofstream cout("A.out");

int main() {

	int t ; 
	
	cin >> t ; 
	
	for ( int i = 0 ; i < t ; i ++ ) {
		int n ; 
		cin >> n ; 
		
		vector<string> teams ; 
		
		for ( int j = 0 ; j < n ; j ++ ) {
			string team = "" ; 
			
			cin >> team ; 
			teams.push_back( team ) ; 
		}
		
		solve(teams,i+1);
	}
	
	return 0 ; 
}

void solve(vs & teams , int c ) {
	
	vector<vector<double> > vals ( 3 , vector<double> ( teams.size() , 0.0 ) ) ; 

	for ( int i = 0 ; i < teams.size() ; i ++ ) {
		vals[ 0 ][ i ] = calc_win( teams[ i ] ) ; 
	}
	
	for ( int i = 0 ; i < teams.size() ; i ++ ) {
		
		double owp = 0.0 ; 
		
		int tot = 0 ; 
		for ( int j = 0 ; j < teams[i].size() ; j ++ ) {
			if ( teams[ j ][ i ] == '.' ) continue ; 
			
			tot ++ ; 
			owp += calc_owp( i, teams[ j ] ) ; 
		}
		
		double p = 1 / (double) tot ; 
		vals[ 1 ][ i ] = owp * p ; 
	}
	
	for ( int i = 0 ; i < teams.size() ; i ++ ) {
		double oowp = 0.0 ; 
		
		int tot = 0 ; 
		for ( int j = 0 ; j < teams[i].size() ; j ++ ) {
			if ( teams[ i ][ j ] == '.' ) continue ;
			tot ++ ;  
			oowp += vals[ 1 ][ j ]  ; 
		}
		
		double p = 1 / (double) tot ; 
		vals[ 2 ][ i ] = p * oowp ; 
	}		

	print_result(vals,c);
}

void print_result( vvd & vals , int c ) {
	cout<<"Case #"<<c<<":"<<endl;
	
	for ( int i = 0 ; i < vals[0].size() ; i ++ ) {
		double res = ( 0.25 * vals[0][i] ) + (0.50*vals[1][i] ) + (0.25 * vals[2][i] ) ; 
		cout<<res<<endl; 
	}
}

double calc_win(string &s ) {
	int win = 0 ; 
	int all = 0 ; 
	
	for ( int i = 0 ; i < s.size() ; i ++ ) {
		if ( s[i] == '1' ) { win ++ ; all ++ ; }
		else if ( s[i] == '0' ) all ++ ;  
	}
	
	if ( all == 0 ) return 0.0 ; 
	if ( win == 0 ) return 0.0 ; 
	
	return (double) win / ( double ) all ; 
}

double calc_owp(int i , string & s ) {
	if ( s[ i ] == '.' ) return 0.0 ; 
	
	string tmp = s ; 
	tmp[ i ] = '.' ; 
	
	return calc_win(tmp);
}
