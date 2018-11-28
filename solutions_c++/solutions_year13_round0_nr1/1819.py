
#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <iostream>
#include <assert.h>



#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define PI 3.14159265358979323
#define EPS 0.000000001
#define INF 1000000000

int T;


char f[10][10];

char lc;

char are_equal(char a, char b) {
	lc=0;
	if (a=='.'||b=='.') return 0;
	
	if (a=='T') {lc=b; return b; }
	if (b=='T') {lc=a; return a; }
	
	if (a==b) {lc=a; return a; }
	
	return 0;
}



int main() {
	cin>>T;
	int cs=1;
	char tc;
	
	while (T-->0) {
		bool full, xwins=false, owins=false;

		cin>>f[0];
		cin>>f[1];
		cin>>f[2];
		cin>>f[3];
		
		full=true;
		
		
		for (int i=0;i<4;i++) {
			for (int j=0;j<4;j++) {
				if (f[i][j]=='.') full=false;
			}
		}
		
		xwins=false;
		owins=false;
		
		
		for (int i=0;i<4;i++) {
			if (
				are_equal(f[i][0], f[i][1])&&
				are_equal(f[i][1], f[i][2])&&
				are_equal(f[i][2], f[i][3])&&
				are_equal(f[i][3], f[i][0])
				) {
				
				if (lc=='X') {
					xwins=true;
//					printf("xwins at i=%d\n", i);
				}
				else {
					owins=true;
//					printf("owins at i=%d\n", i);
				}
			}
			

			if (
				are_equal(f[0][i], f[1][i])&&
				are_equal(f[1][i], f[2][i])&&
				are_equal(f[2][i], f[3][i])&&
				are_equal(f[3][i], f[0][i])
				) {
				
				if (lc=='X') {
					xwins=true;
//					printf("xwins at v i=%d\n", i);
				} else {
					owins=true;
//					printf("owins at v i=%d\n", i);
				}
			}
	
		}
		
		if (
			are_equal(f[0][0], f[1][1])&&
			are_equal(f[1][1], f[2][2])&&
			are_equal(f[2][2], f[3][3])&&
			are_equal(f[0][0], f[3][3])
			) {
			
				if (lc=='X') {
					xwins=true;
//					printf("xwins at diag 1\n");
				} else {
					owins=true;
//					printf("owins at diag 1\n");
				}
		}
		
		if (
			are_equal(f[0][3], f[1][2])&&
			are_equal(f[1][2], f[2][1])&&
			are_equal(f[2][1], f[3][0])&&
			are_equal(f[0][3], f[3][0])
			) {
			
				if (lc=='X') {
					xwins=true;
//					printf("xwins at diag 2\n");
				} else {
					owins=true;
//					printf("owins at diag 2\n");
				}
		}
		
		
		printf("Case #%d: ", cs++);
		
		
		if (xwins) {
			printf("X won");
		} else if (owins) {
			printf("O won");
		} else if (full) {
			printf("Draw");
		} else
			printf("Game has not completed");
		
		
		printf("\n");
	}
	
    return 0;
    
}


