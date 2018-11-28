#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <list>

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <ctime>

using namespace std;

#define MAX 1001
#define INF 1000000
#define EPS 1e-7
#define PI acos(-1.0)
#define READ() freopen("input.txt", "r", stdin)
#define WRITE() freopen("output.txt", "w", stdout)
#define CLR(x) memset( x, 0, sizeof(x) )
#define SET(x) memset( x, -1, sizeof(x) )
#define CHKBIT(x, i) ( ( ( x & ( 1 << i ) ) == 0 ) ? 0 : 1 )
#define SETBIT(x, i) ( x | ( 1 << i ) )
#define CLRBIT(x, i) ( x & (!( 1 << i )) )

char str[10][10];
int  v[4][2] = { {0, 0}, {0, 1}, {0, 2}, {0, 3} };
int  h[4][2] = { {0, 0}, {1, 0}, {2, 0}, {3, 0} };
int dr[4][2] = { {0, 0}, {1, 1}, {2, 2}, {3, 3} };
int dl[4][2] = { {0, 0}, {1, -1}, {2, -2}, {3, -3} };

bool check(int x, int y){
	if( x <0 || x >= 4 || y < 0 || y >= 4 ) return false;
	return true;
}

bool check_4(char ch, int i, int j, int a[][2]){
	for(int k = 0; k<4; k++){
		int ti = i + a[k][0]; 
		int tj = j + a[k][1];
		if( check(ti, tj) == false ){
			return false;
		}
		if( str[ti][tj] != ch && str[ti][tj] != 'T' ){
			return false;
		}
	}
	return true;
}

bool check_win(char ch){
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if( check_4(ch, i, j, v) ) return true;
			if( check_4(ch, i, j, h) ) return true;
			if( check_4(ch, i, j, dr) ) return true;
			if( check_4(ch, i, j, dl) ) return true;
		}
	}
	return false;
}

int count_all(){
	int c = 0;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			if( str[i][j] == '.' ) c++;
		}
	}
	return 16 - c;
}

int main(){
	//ios_base::sync_with_stdio(false);
	READ();
	WRITE();
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++){
		for(int i=0; i<4; i++) scanf("%s", str[i]);
		bool xwin = check_win('X');
		bool owin = check_win('O');
		int c = count_all();
		printf("Case #%d: ", t);
		if( xwin == true ){
			puts("X won");
		}
		else if( owin == true ){
			puts("O won");
		}
		else if( c == 16 ){
			puts("Draw");
		}
		else{
			puts("Game has not completed");
		}
	}
	return 0;
}

