#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
using namespace std;
int gettime( const string &s )
{
	int h, m;
	sscanf( s.c_str(), "%d:%d", &h, &m );
	return h * 60 + m;
}
int main( void )
{
	int N;
	cin >> N;
	for( int C = 0; C < N; C ++ ){
		int T;
		cin >> T;
		vector< pair<int,int> > A, B;
		int NA, NB;
		cin >> NA >> NB;
		for( int i = 0; i < NA; i ++ ){
			string s, t;
			cin >> s >> t;
			A.push_back( pair<int,int>(gettime(s), +1) );
			B.push_back( pair<int,int>(gettime(t) + T, -1) );
		}
		for( int i = 0; i < NB; i ++ ){
			string s, t;
			cin >> s >> t;
			B.push_back( pair<int,int>(gettime(s), +1) );
			A.push_back( pair<int,int>(gettime(t) + T, -1) );
		}
		sort( A.begin(), A.end() );
		sort( B.begin(), B.end() );
		int rA = 0, rB = 0;
		for( int i = 0, t = 0; i < A.size(); i ++ ){
			t -= A[i].second;
			rA = min( rA, t );
		}
		for( int i = 0, t = 0; i < B.size(); i ++ ){
			t -= B[i].second;
			rB = min( rB, t );
		}
		printf( "Case #%d: %d %d\n", C + 1, -rA, -rB );
	}
}
