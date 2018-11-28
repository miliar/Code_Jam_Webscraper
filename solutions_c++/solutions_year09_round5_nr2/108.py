#include <sstream> 
#include <iostream>
#include <string.h>
#include <algorithm>
#include <stdlib.h> 
#include <stdio.h> 
#include <numeric>
#include <math.h>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

const int mod = 10009;

vector < string > s;
int k;
int n;
int a[128][32];
int ans[16];
int b[32];

void read() {
	string t , h;
	int i , j;
	
	s.clear();
	memset ( a , 0 , sizeof a );
	
	cin >> t;
	for (i = 0; i < (int)t.size(); i++)
		if ( t[i] == '+' ) 
			t[i] = ' ';
	istringstream in ( t );
	
		
	while ( in >> h ) {
		s.push_back ( h );
	}
	
	cin >> k >> n;
	for (i = 1; i <= n; i++) {
		cin >> t;
		
		for (j = 0; j < (int)t.size(); j++)
			a[i][ t[j] - 'a' ] ++;
	}
}

int calc() {
	int ans = 0;
	int cur;
	int i , j;
	
	for (i = 0; i < (int)s.size(); i++) {
		cur = 1;
		for (j = 0; j < (int)s[i].size(); j++) {
			cur = (cur * b[ s[i][j] - 'a' ]) % mod;
		}
		ans = (ans + cur) % mod;
	}
	
//	printf ( "%d\n\n" , ans );
	
	return ans;
}

void rec ( int x , int y ) {
	if ( x == n + 1 || y == k ) {
	//	printf ( "%d\n" , y );
		ans[y] = (ans[y] + calc()) % mod;
		return ;
	}
	int i;
	
	rec ( x + 1 , y );
	
	for (i = 0; i < 26; i++) b[i] += a[x][i];
	rec ( 1 , y + 1 );
	for (i = 0; i < 26; i++) b[i] -= a[x][i];
	
}

void solve() {
	int i;
	memset ( ans , 0 , sizeof ans );
	rec ( 1 , 0 );
	
	for (i = 1; i <= k; i++)
		printf ( " %d" , ans[i] );
	printf ( "\n" );
}

int main() {
	int cases , i;
	
	cin >> cases;
	for (i = 1; i <= cases; i++) {
		printf ( "Case #%d:" , i );
		
		read();
		solve();
		
		fflush ( stdout );
	}
	
	return 0;
}

