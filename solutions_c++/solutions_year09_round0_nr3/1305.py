#include <string>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

string input;
string target = "welcome to code jam";

int N;

int dp[500][50];

int solve( int indexi , int indexj ){


	if( indexj == target.size() )
		return 1;

	if( indexi >= input.size() )
		return 0;

	if( dp[indexi][indexj] != -1 )
		return dp[indexi][indexj];

	int res = 0;

	for( int i = indexi ; i < input.size() ; i ++ )
		if( input[i] == target[indexj] ){
			res += solve( i+1 , indexj+1 );
			if( res >= 10000 )
				res -= 10000;
		}

	dp[indexi][indexj] = res;

	return res;
}

void readOthers( void ){

	char enter;
	while( true ){
		scanf("%c",&enter);

		if( enter == '\n' )
			break;
	}

	return;
}

int main(){

	//FILE *fin = freopen( "C-test.in" , "r" , stdin );
	//FILE *fout = freopen( "C-testout.out" , "w" , stdout );

	//FILE *fin = freopen( "C-small-attempt0.in" , "r" , stdin );
	//FILE *fout = freopen( "C-smallout.out" , "w" , stdout );

	FILE *fin = freopen( "C-large.in" , "r" , stdin );
	FILE *fout = freopen( "C-largeout.out" , "w" , stdout );

	
	scanf("%d",&N);

	readOthers();

	for( int cases = 1 ; cases <= N ; cases ++ ){

		getline( cin , input );

		memset( dp , -1 , sizeof( dp ) );

		cout<<"Case #"<<cases<<": ";
		printf("%04d\n",solve(0,0));

	}

	return 0;
}