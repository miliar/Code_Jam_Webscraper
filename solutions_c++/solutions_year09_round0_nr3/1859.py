#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <string>


//#define DEBUG
#define LEN_MSG 18+1
#define LEN_LINE  500+1

using namespace std;


unsigned long long solve( string line, string msg )
{
	//long long n[LEN_MSG][LEN_LINE];
	unsigned long long** n = new unsigned long long*[ msg.size() ];
	for( int i = 0; i < msg.size(); i++){
		n[i] = new unsigned long long[line.size()];
	}

	// Init
	n[0][0] = ( line.at(0) == msg.at(0) ? 1 : 0 );
	for( int i = 1; i < msg.size(); i++){
		//n[i][0] = ( line.at(0) == msg.at(i) ? 1 : 0 );
		n[i][0] = 0;
	}
	for( int j = 1; j < (int)line.size(); j++){
		n[0][j] = n[0][j-1] + ( line.at(j) == msg.at(0) ? 1 : 0 );
	}
	

	for( int i = 1; i < msg.size(); i++){
		for( int j = 1; j < (int)line.size(); j++){
			if( line.at(j) == msg.at(i) ){
				n[i][j] = ( n[i-1][j-1] + n[i][j-1] ) % 10000;
			}else{
				n[i][j] = n[i][j-1];
			}
		}
	}

#ifdef DEBUG
	printf("   ");
	for( int j = 0; j < (int)line.size(); j++){
		printf( "%c ", line.at(j) );
	}
	printf("\n");
	for( int i = 0; i < msg.size(); i++){

		printf( "%c: ", msg.at(i) );
		for( int j = 0; j < (int)line.size(); j++){
			printf("%d ", n[i][j] );
		}
		printf("\n");
	}
#endif //DEBUG

	unsigned long long num = n[msg.size()-1][line.size()-1];

	for( int i = 0; i < msg.size(); i++){
		delete n[i];
	}
	delete n;



	return num;
}


int main(int argc, char** argv)
{
	//freopen("test.in", "r", stdin );
	//freopen("test.out", "w", stdout );
	//freopen("C-small-attempt3.in", "r", stdin );
	//freopen("C-small-attempt3.out", "w", stdout );
	//freopen("C-large.in", "r", stdin );
	//freopen("C-large.out", "w", stdout );


	int N;
	string line;
	string msg = "welcome to code jam";
	//string msg = "welcome to";
	set<char> msgChs( msg.begin(), msg.end() );

	cin >> N;
	getline(cin, line, '\n');
	for( int iN = 0; iN < N; iN++ ){
		getline(cin, line, '\n');
		

		string newline;
		for( string::iterator iter = line.begin(); iter != line.end(); ++iter ){
			if( msgChs.find( *iter ) != msgChs.end() ){
				newline.push_back( tolower( *iter ) );
			}
		}

#ifdef DEBUG
		printf("line: %s\n", line.c_str() );
		printf("new line: %s\n", newline.c_str() );
		printf("msg     : %s\n", msg.c_str() );
#endif //DEBUG
		
		unsigned long long n = 0;
		//if( newline.size() > 0 ){
		////	n = solve( newline, msg );
		//}else{
		//	n= 0;
		//}
		//n = n % 10000;
		n = solve( line, msg );
		//printf( "Case #%d: %04lld\n", iN + 1, n );
		//n = n % 10000;
		printf( "Case #%d: %04lld\n", iN + 1, n );
	}

	return 0;
}