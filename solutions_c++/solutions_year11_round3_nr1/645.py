#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>

#define pb push_back

using namespace std;

int T, R, C;

char A[60][60];

void print() {
  int i,j;
  for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			printf("%c",A[i][j]);
		}
		printf("\n");
	}
}

void solve(int test) {
	printf("Case #%d:\n", test);
	int i, j, ok = 1;
	
	
	for (i = 0; i < R; i++) {
		for (j = 0; j < C; j++) {
			if (A[i][j] == '#') 
			{
				if (A[i][j+1] != '#' || A[i+1][j+1] != '#' || A[i+1][j] != '#') {
					ok = 0;
					printf("Impossible\n", i, j);
					return;
				}
				
				A[i][j] = '/';
				A[i+1][j] = '\\';
				A[i][j+1] = '\\';
				A[i+1][j+1] = '/';
			}
		}
	}

	print();
	
}

int main () {
	
	int i,j,val;
	char c;
	
	scanf ("%d",&T);
	
	for (i =0; i < T; i++) {
		
		memset (A, 0, 60*60);

		scanf("%d %d\n", &R, &C);
		
		for (j=0; j<R; j++) {
			scanf("%s", A[j]);
		}
		solve(i+1);
		
	}
	
}
