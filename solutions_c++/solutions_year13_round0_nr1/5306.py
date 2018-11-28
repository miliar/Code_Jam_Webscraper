#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define INF 2000000000
#define INFLL (1LL<<62)
#define SS ({int x;scanf("%d", &x);x;})
#define SSL ({lint x;scanf("%lld", &x);x;})
#define rep(i,n) for(int i=0;i<(n);i++)
#define rept(i,m,n) for(int i=(m);i<(n);i++)
#define ull unsigned long long
#define lint long long
#define MX 10000001

char board[5][5];

char check(char a, char b, char c, char d) {
	if(a=='T' && b==c && c==d) {
		return b;
	}
	if( (b=='T' && a==c && c==d) || (c=='T' && a==b && b==d) || (d=='T' && a==b && b==c) || (a==b && b==c && c==d) ) {
		return a;
	}
	return '.';
}

char checkRow(int row) {
	char a,b,c,d;
	a = board[row][0];
	b = board[row][1];
	c = board[row][2];
	d = board[row][3];
	return check(a,b,c,d);
}

char checkColumn(int col) {
	char a,b,c,d;
	a = board[0][col];
	b = board[1][col];
	c = board[2][col];
	d = board[3][col];
	return check(a,b,c,d);			
}

char checkDiagonal1() {
	char a,b,c,d;
	a = board[0][0];
	b = board[1][1];
	c = board[2][2];
	d = board[3][3];			
	return check(a,b,c,d);			
}

char checkDiagonal2() {
	char a,b,c,d;
	a = board[0][3];
	b = board[1][2];
	c = board[2][1];
	d = board[3][0];			
	return check(a,b,c,d);			
}

int main()
{
	int i,j,k,l,n,m,t,testnum;
	t=SS;
	for(testnum=1; testnum<=t; testnum++) {

		for(i=0; i<4; ++i)
			scanf("%s",board[i]);

		bool done = false;
		//Check for rows
		for(i=0; i<4; ++i) {
			char c = checkRow(i);
			if(c!='.'){
				printf("Case #%d: %c won\n",testnum,c);
				done=true;
				break;
			}
		}
		if(done)
			continue;
			
		// Check for columns
		for(j=0; j<4; ++j) {
			char c = checkColumn(j);
			if(c!='.'){
				printf("Case #%d: %c won\n",testnum,c);
				done=true;
				break;
			}
		}
		if(done)
			continue;
			
		// Check for diagonals
		char c = checkDiagonal1();
		if(c!='.') {
				printf("Case #%d: %c won\n",testnum,c);
				continue;
		}
		c = checkDiagonal2();
		if(c!='.') {
				printf("Case #%d: %c won\n",testnum,c);
				continue;
		}
		
		//Check whether game is draw or yet not over	
		bool draw = true;
		for(i=0; i<4; ++i) {
			for(j=0; j<4; ++j) {
				if(board[i][j]=='.') {
					draw = false;
					break;
				}
			}
			if(!draw)
				break;
		}
		printf("Case #%d: %s\n",testnum,draw?"Draw":"Game has not completed");		
	}	
	return 0;
}



