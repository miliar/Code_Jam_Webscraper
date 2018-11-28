#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <ctype.h>
#include <stack>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
using namespace std;
#define PB		push_back
#define ALL(v)		(v).begin() , (v).end()
#define SZ(v)		( (int) v.size() )
#define Set(v,x)	memset(  v , x , sizeof(v))
#define two(n)		( 1 << (n) )
#define contain(Set,i)  ( (Set) & two(i) )
#define MAX 110
int H , W;
char mat[MAX][MAX], curLetter;
int val[MAX][MAX];
int dx[] = {0,-1,1,0} , dy[] = {-1,0,0,1};

int go(int i , int j ) {
	//printf("%d,%d = %d\n", i,j,mat[i][j]);
	if (mat[i][j] != 0 )
		return mat[i][j];


	int min = val[i][j], b = -1;
	for (int k = 0 ; k < 4 ; k++)
		if (val[ i+dy[k] ][ j+dx[k] ] < min ) {
			min = val[ i+dy[k] ][ j+dx[k] ];
			b = k;
		}
	//printf("%d,%d , b: %d\n", i,j,b);
	if (b == -1) {
		if ( mat[i][j] == 0)
			return mat[i][j] = curLetter++;
		return mat[i][j];
	}
	return mat[i][j] = go( i+dy[b] , j+dx[b]);
}
void solve() {
	int i , j;
	curLetter = 'a';
	for (i = 1; i <= H; i++)
		for (j = 1 ; j <= W ; j++)
			if (mat[i][j] == 0)
				go(i,j);

	for (i = 1; i <= H; i++) {
		cout << mat[i][1];
		for (j = 2 ; j <= W ; j++)
			cout << " " << mat[i][j];
		cout << endl;
	}
}
int main() {
	int t , nt, i , j;
	cin >> nt;
	for (t = 1 ; t <= nt ; t++) {
		Set(mat, 0);
		Set(val,0x3f);
		cin >> H >> W;
		for (i = 1 ; i <= H ; i++)
			for (j=1; j <= W ; j++)
				cin >> val[i][j];

		cout << "Case #" << t << ":\n";
		solve();
	}
	return 0;
}

