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

const int MAX = 110;
char mat[MAX][MAX];
int N;
long double wmp[MAX], rpi[MAX], wp[MAX];

/*
 *
 RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

OWP (Opponents' Winning Percentage) is the average WP of all your opponents, after first throwing out the games they played against you.
For example, if you throw out games played against team D, then team B has WP = 0 and team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5, team B has OWP = 0.5, and team C has OWP = 2/3.

OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. OWP is exactly the number computed in the previous step.
For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12. 

*/ 
void go(int a) {
	long double d = 0 ;
	int i,j,amt = 0;
	for (i= 0 ; i < N;  i++)
		if (i != a && mat[a][i] != '.') {
			// find wp
			int win =0 , adv = 0;
			for (j = 0 ; j < N ; j++) 
				if (j != a && mat[i][j] != '.') {
					adv++;
					if (mat[i][j] == '1')
						win++;	
				}
			amt++;
			long double temp = (long double) win / adv;
			d += temp;
		}
	wmp[a] = d / amt;
}
void solve() {
	int i , j;
	scanf("%d", &N);
	for (i = 0 ; i < N ; i++) {
		scanf("%s" , mat[i]);
		rpi[i] = 0;
		int amt = 0, win = 0;
		for (j = 0 ; j < N ; j++) {
			if (mat[i][j] != '.') {
				amt++;
				if (mat[i][j] == '1')
					win++;
			}
		}
		wp[i] = (long double)win / amt;
	}
	for (i= 0 ; i < N ; i++) {
		go(i);
		//	printf("%d: %.6Lf   %.6Lf  \n", i , wp[i], wmp[i] );
	}
	for (i = 0 ; i < N ; i++) {
		go(i);
		long double oowmp = 0.;
		int adv = 0;
	//	printf(" oowmp\n");
		for (j = 0 ; j < N ; j++) {
			if (mat[i][j] != '.') {
				oowmp += wmp[j];
	//			printf("sum %d : %.6Lf\n", j , wmp[j]);
				adv++;
			}
		}
		oowmp /= adv;
	
		rpi[i] = 0.25 * wp[i] + 0.5 * wmp[i] + 0.25 * oowmp;
	}
	
	for (i= 0 ; i < N ; i++)
		printf("%.9Lf\n", rpi[i]);
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
