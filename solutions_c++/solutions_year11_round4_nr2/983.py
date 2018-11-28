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

#define MAX 510
int L , C, D;
char m[MAX][MAX];

long long smass[MAX][MAX] , mass[MAX][MAX];

void solve() {
	int res = 0 , i , j , k;
	scanf("%d %d %d", &L , &C , &D);
	for (i = 1 ;  i<= L ; i++)
		scanf("%s", m[i]+1);

	for (i = 1 ; i <= L ; i++)
		for (j = 1 ; j <= C ; j++) {
			mass[i][j] = m[i][j]-'0'+D;
			smass[i][j] =  mass[i][j] + smass[i][j-1] + smass[i-1][j] - smass[i-1][j-1];
		}

	res = 2;

	for (i = 3 ; i <= L ; i++)
		for (j = 3 ; j <= C ; j++) 
			for (k = res+1 ; i-k+1 >= 1 && j-k+1 >= 1 ; k++) {
				// try squares res+1 * res+1
					
				
				// i-k, j-k
				double cy = i-k/2.0 , cx = j-k/2.0;
/*
				if (i == 6 && j == 6 ) {
					printf("center %.2f %.2f \n", cy,cx);
				}
				*/
				int a,  b,x,y ;
				double sx = 0 , sy = 0;
				for (a = 0 ; a < k ; a++)
					for (b = 0 ; b < k ; b++) {
						if ((a == 0 && b == 0) || (a == 0 && b == k-1) || (a == k-1 && b == 0) || (a == k-1 && b == k-1))
							continue;

						x = j-b , y = i-a;
						sx += (x-0.5-cx) * mass[y][x];
						sy += (y-0.5-cy) * mass[y][x];
/*
						if (i == 6 && j == 6 && k == 5 ) {
							printf("\t ponto %.2f %.2f %lld\n", y+0.5,cx+0.5 , mass[y][x]);
						}
						*/
					}
				/*
				if (i == 6 && j == 6 && k == 5 ) {
					printf("%.2f  %.2f\n", sy,sx);
				}
				*/
				if (fabs(sx) < 1e-6 && fabs(sy) < 1e-6)
					res = k;
			}
	if (res == 2)
		puts("IMPOSSIBLE");
	else
		cout << res << endl;
}

int main() {
	int C , nc;
	
	scanf("%d\n", &C);
	for ( nc = 1 ; nc <= C ; nc++) {
		cout << "Case #" << nc << ": ";
		solve();
	}	
	return 0;
}
