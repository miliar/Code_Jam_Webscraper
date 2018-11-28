#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
using namespace std;
#define PB			push_back
#define ALL(v)			(v).begin() , (v).end()
#define SZ(v)			( (int) v.size() )
#define Set(v,x)		memset(  v , x , sizeof(v))
#define two(n)			( 1 << (n) )
#define contain(S,i)		( (S) & two(i) ) 
#define SQR(v)			( (v) * (v) )
#define ABS(x)			( ( (x) >= 0 ) ? (x) : -(x) )
#define foreach(v,it)		for( typeof((v).begin()) it = (v).begin() ; it != (v).end() ; it++ )
#define MAX 60
int L,C;
char mat[MAX][MAX];
bool ok(int i , int j) {
	return i < L && j < C && mat[i][j] == '#';
}
bool square(int i , int j ) {
	if (ok(i,j) && ok(i+1,j) && ok(i,j+1) && ok(i+1,j+1)) {
		mat[i][j] = '/';
		mat[i][j+1] = '\\';
		mat[i+1][j+1] = '/';
		mat[i+1][j] = '\\';
		return true;
	}
	else
		return false;
}
bool go() {
	int i , j ;
	for (i = 0 ; i < L ; i++) {
		for (j = 0 ; j < C ; j++) 
			if (mat[i][j] == '#') {
				if (!square(i,j))
					return false;
			}
	}
	return true;
}
void solve() {
	int i,j;
	scanf("%d %d", &L, &C);
	for (i = 0 ; i < L ; i++)
		scanf("%s", mat[i]);

	if (go()) {
		for (i = 0 ; i < L ; i++)
			puts(mat[i]);
	}
	else
		puts("Impossible");
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ":\n";
		solve();
	}	
	return 0;
}
