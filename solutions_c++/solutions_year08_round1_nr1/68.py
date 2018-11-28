#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#define INF 0x3f3f3f3f

using namespace std;

vector <int> tA, tB;
vector <int> A[2], B[2];
long long sol;

void load(){
	int n;
	scanf( "%d", &n );
	A[0].clear(); A[1].clear();
	B[0].clear(); B[1].clear();

	for( int i = 0; i < n; ++i ){
		int t; scanf( "%d", &t );
		if( t < 0 ) A[0].push_back(t);
		else A[1].push_back(t);
	}
	for( int i = 0; i < n; ++i ){
		int t; scanf( "%d", &t );
		if( t < 0 ) B[0].push_back(t);
		else B[1].push_back(t);
	}
}

void solve(){
	sort( A[0].begin(), A[0].end(), greater<int>() );
	sort( A[1].begin(), A[1].end() );
	sort( B[0].begin(), B[0].end(), greater<int>() );
	sort( B[1].begin(), B[1].end() );
	sol = 0;

	while( A[0].size() && B[1].size() ){
		sol += (long long)A[0].back()*B[1].back();
		A[0].pop_back();
		B[1].pop_back();
	}
	while( B[0].size() && A[1].size() ){
		sol += (long long)B[0].back()*A[1].back();
		B[0].pop_back();
		A[1].pop_back();
	}

	tA.clear(); tB.clear();

	for( int i = 0; i < A[0].size(); ++i ) tA.push_back( A[0][i] );
	for( int i = 0; i < A[1].size(); ++i ) tA.push_back( A[1][i] );
	for( int i = 0; i < B[0].size(); ++i ) tB.push_back( B[0][i] );
	for( int i = 0; i < B[1].size(); ++i ) tB.push_back( B[1][i] );

	sort( tA.begin(), tA.end() );
	sort( tB.begin(), tB.end(), greater<int>() );

	for( int i = 0; i < tA.size(); ++i ) {
		sol += (long long)tA[i]*tB[i];
	}

}

int main(){
	int tp;
	scanf( "%d", &tp );

	for( int tt = 1; tt <= tp; ++tt ){
		load();
		solve();
		printf( "Case #%d: %lld\n", tt, sol );
	}

	return 0;
}
