#include <iostream>
#include <cstdio>
using namespace std;

#define FOR(i, M) for( int i = 0; i < (M); ++i )
#define FOR_(i, m, c, M) for( int i = (m); i c (M); ++i )

int main(){
	int T, N;
	int a[1001], b[1001];
	
	cin >> T;
	FOR_(Ti, 1, <=, T){
		cin >> N;
		FOR(i, N) cin >> a[i] >> b[i];
		
		int cross = 0;
		FOR(i, N) FOR(j, N){
			if (i == j) continue;
			if ((a[j] > a[i] && b[j] < b[i]) || (a[j] < a[i] && b[j] > b[i])) ++cross;
		}
		
		printf("Case #%d: %d\n", Ti, cross/2);
	}
}
