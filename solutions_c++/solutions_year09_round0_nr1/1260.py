#include <cstdio>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int L,D,N;
vector<string> dict;
vector< vector<char> > pattern;

bool search( const string &str){

	for( int i = 0 ; i < str.size() ; i++ )
		if( !binary_search( pattern[i].begin() , pattern[i].end() , str[i] ) )
			return false;

	return true;
}

int solve( void ){

	int res = 0;
	for( int i = 0 ; i < dict.size() ; i ++ )
		if( search( dict[i] ) )
			res ++;

	return res;
}

void initPattern( const string &input ){

	int start = 0;
	
	while( start < input.size() ){

		vector<char> aPattern;
		if( input[start] != '(' ){
			aPattern.push_back( input[start] );
			start ++ ;
		}
		else{
			
			int i;
			for( i = start+1 ; ; i++ )
				if( input[i] != ')' )
					aPattern.push_back( input[i] );
				else
					break;

			start = i+1;
		}

		sort( aPattern.begin() , aPattern.end() );
		pattern.push_back( aPattern );
	}

	return;
}

int main( void ){

	//FILE *fin = freopen("A-test.in" , "r" , stdin );
	//FILE *fout = freopen("A-test.out" , "w" , stdout );

	//FILE *fin = freopen("A-small-attempt1.in" , "r" , stdin );
	//FILE *fout = freopen("A-small.out" , "w" , stdout );

	FILE *fin = freopen("A-large.in" , "r" , stdin );
	FILE *fout = freopen("A-large.out" , "w" , stdout );
	
	char enter;

	cin>>L>>D>>N;
	
	string dictItem;
	for( int i = 0 ; i < D ; i ++ ){
		cin>>dictItem;
		dict.push_back( dictItem );
	}

	string input;
	for( int i = 1 ; i<= N ; i ++ ){

		cin>>input;
		pattern.clear();

		initPattern( input ); 

		cout<<"Case #"<<i<<": ";

		//test
		//cout<<endl;
		//for( int i=0;i<pattern.size();i++){
		//
		//	for( int j=0;j<pattern[i].size();j++)
		//		cout<<pattern[i][j];
		//	
		//	cout<<endl;
		//}

		cout<<solve()<<endl;
	}

	//fclose( fin );
	//fclose( fout );

	return 0;
}
