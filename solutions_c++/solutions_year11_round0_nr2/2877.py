//#include <iostream>
#include <vector>
#include <algorithm>
//#include <set>
#include <map>
#include <string>
#include <fstream>
//#include <queue>
#include <stack>

using namespace std ; 

string solve(map<pair<char,char>,char> & combine , map<pair<char,char>,char> & oppose , string & input ) ;
void print( string  res , int cases ) ; 

ifstream cin("code.in") ;
ofstream cout("code.out") ;
 
int main() {
	
	int T ; 
	cin >> T ; 
	for ( int i = 0 ; i < T ; i ++ ) {
		int C , D ; 
		map<pair<char,char> , char > combine ; 
		map<pair<char,char> , char > oppose ; 
		
		cin >> C ; 
		
		string str = "" ; 
				
		for ( int j = 0 ; j < C ; j ++ ) {
			cin >> str ;
			pair<char,char> p ; 
			p.first = str[ 0 ] ; 
			p.second = str[ 1 ] ;  
			combine[ p ] = str[ 2 ] ;
			swap( p.first, p.second ) ; 
			combine[ p ] = str[ 2 ] ;			
		}
		
		cin >> D ; 

		for ( int j = 0 ; j < D ; j ++ ) {
			cin >> str ; 
			
			pair<char,char> p ; 
			p.first = str[ 0 ] ; 
			p.second = str[ 1 ] ; 
			
			oppose[ p ] = str[ 2 ] ; 
			
			swap(p.first,p.second) ; 
			
			oppose[ p ] = str[ 2 ] ; 
			
		}
		
		int N ; 
		
		cin >> N ; 
		
		cin >> str ; 
		
		print(solve(combine,oppose,str),i+1) ; 
//		cout<<"Case #"<<i+1<<": "<<solve(combine,oppose,str)<<endl;
		
	}

	return 0 ;

}

void print(string str , int cases ) {
	cout<<"Case #"<<cases<<": ";
	cout<<"[";
	
	for ( int i = 0 ; i < str.size() ; i ++ ) {
		if ( i == 0 ) cout<<str[ i ] ;
		else cout<<", "<<str[ i ] ;
	}
	cout<<"]" ;
	cout<<endl;
} 

string solve(map<pair<char,char>,char> & combine , map<pair<char,char>,char> & oppose , string & input ) {

	stack<char> a ; 
	stack<char> b ; 
	
	for ( int i = 0 ; i < input.size() ; i ++ ) {

		int cur_char = input[ i ] ; 
		
		a.push( cur_char ) ; 
		
		if ( a.size() == 1 ) continue ; 
		
		char f_char = a.top() ;
		a.pop() ;  
		char s_char = a.top() ; 
		a.pop() ; 
		
		pair<char,char> p ; 
		p.first = f_char ; 
		p.second = s_char ; 
		
		if ( combine.find( p ) != combine.end() ) {
			a.push( combine[ p ] ) ; 
			continue ; 
		}
		
		else {
			a.push( s_char ) ;
			b.push( f_char ) ;  
			bool empty = false ; 
			while ( !a.empty() ) {
			
				b.push( a.top() ) ; 
				char cur = a.top() ; 
				a.pop() ; 
				
				pair<char,char> tmp ; 
				tmp.first = cur_char ; 
				tmp.second = cur ; 
				
				if ( oppose.find(tmp) != oppose.end() ) {
					empty = true ; 
					/*while ( !a.empty() ) {
						a.pop() ; 
					}
					break ;*/ 
				} 
			}
			
			if ( empty == false ) {
				while ( !b.empty() ) {
					a.push( b.top() ) ; 
					b.pop() ; 
				
				}
			
				//a.push(f_char) ; 
			}
			
			else {
				while ( !a.empty() ) a.pop() ;
				while ( !b.empty() ) b.pop() ;  
			}
		} 				
	}
	
	string res = "" ; 
	
	while ( !a.empty( ) ) {
		res += a.top( ) ; 
		a.pop() ; 
	}
	
	reverse(res.begin(),res.end());
	
	return res ; 
} 
