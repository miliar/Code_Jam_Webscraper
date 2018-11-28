#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream in;

int t [110];

int dp [110][110];


int n,s,p;
int res1( int i ){
	int c = t[i];
	if( c/3 >= p ) return 1;
	int res = 0;

	int a = (c-p)/2;
	int b = c - a - p;

	if( abs(a-p)<=1 && abs(b-p)<=1 )
		return 1;
	return 0;
}

int res2( int i ){
	int c = t[i];
	if( c<p ) return 0;
	if( c/3 >= p ) return 1;

	int res = 0;
	int a = (c-p)/2;
	int b = c - a - p;

	if( abs(a-p)<=2 && abs(b-p)<=2 )
		return 1;
	return 0;
}

int solve(){
	in>>n>>s>>p;
	for( int i = 0; i < n; i++ )
		in>>t[i];

	for( int i = 0; i < 110; i++ )
		for( int j = 0; j < 110; j++ )
			dp[i][j] = 0;

	for( int i = 1; i <= n; i++ ){
		for( int j = 0; j <= s; j++ ){
			dp[i][j] = dp[i-1][j] + res1(i-1);
			if( j )
				dp[i][j] = max( dp[i][j], dp[i-1][j-1] + res2(i-1) );
		}
	}
	return dp[n][s];
}

int main(){
	int T;
	in = ifstream("in.txt");
	ofstream out ("out.txt");

	in>>T;
	for( int i = 1; i <= T; i++ ){
		if( i!=1 ) out<<endl;
		out<<"Case #"<<i<<": "<<solve();
	}
}