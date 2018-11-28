#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <algorithm>
#define infinity 2139062143
#define swap(x, y) (x) ^= (y) ^= (x) ^= (y)
#define foreach( i, n ) 	for(int (i) = 0; (i) < (n); ++(i))
#define min( x, y )  ( ((x) < (y)) ? (x) : (y) )
#define max( x, y )  ( ((x) > (y)) ? (x) : (y) )
#define abs( x ) (((x) < 0)? (-x) : (x) )
#define full 100
using namespace std;

int main () {
	int n;
	char lala[10][10];
	int x[10][10], o[10][10];
	scanf("%d", &n);
	foreach (g, n) {
		foreach (k, 4)
			scanf("%s", lala[k]);
		memset(x, 0, sizeof(x));
		memset(o, 0, sizeof(o));
		bool tensobra=false, xvenc=false, ovenc=false;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (lala[i][j] == '.')
					tensobra = true;
			}
		}
		for (int i = 0; i < 4; i++) 
			if (lala[0][i] == 'X' || lala[0][i] == 'T')
				x[0][i] = 1;
		for (int i = 1; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (lala[i][j] == 'X' || lala[i][j] == 'T')
					x[i][j] = x[i-1][j] + 1;
				if (x[i][j] == 4)
					xvenc = true;
			}
		}
		//para o X2
		for (int i = 0; i < 4; i++) 
			if (lala[i][0] == 'X' || lala[i][0] == 'T')
				x[i][0] = 1;
		for (int i = 0; i < 4; i++) {
			for (int j = 1; j < 4; j++) {
				if (lala[i][j] == 'X' || lala[i][j] == 'T')
					x[i][j] = x[i][j-1] + 1;
				if (x[i][j] == 4)
					xvenc = true;
			}
		}
		int k, q;
		for (k = 0; k < 4; k++) 
			if (lala[k][k] != 'X' && lala[k][k] != 'T')
				break;
		if (k == 4)
			xvenc = true;
		for (k = 0, q = 3; k < 4; k++, q--) 
			if (lala[k][q] != 'X' && lala[k][q] != 'T')
				break;
		if (k == 4)
			xvenc = true;
			
		// para o O
		for (int i = 0; i < 4; i++) 
			if (lala[0][i] == 'O' || lala[0][i] == 'T')
				o[0][i] = 1;
		for (int i = 1; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (lala[i][j] == 'O' || lala[i][j] == 'T')
					o[i][j] = o[i-1][j] + 1;
				if (o[i][j] == 4)
					ovenc = true;
			}
		}
		//para o O2
		for (int i = 0; i < 4; i++) 
			if (lala[i][0] == 'O' || lala[i][0] == 'T')
				o[i][0] = 1;
		for (int i = 0; i < 4; i++) {
			for (int j = 1; j < 4; j++) {
				if (lala[i][j] == 'O' || lala[i][j] == 'T')
					o[i][j] = o[i][j-1] + 1;
				if (o[i][j] == 4)
					ovenc = true;
			}
		}
		for (k = 0; k < 4; k++) 
			if (lala[k][k] != 'O' && lala[k][k] != 'T')
				break;
		if (k == 4)
			ovenc = true;
		for (k = 0, q = 3; k < 4; k++, q--) 
			if (lala[k][q] != 'O' && lala[k][q] != 'T')
				break;
		if (k == 4)
			ovenc = true;
			
		if (xvenc)
			printf("Case #%d: X won\n", g+1);
		else if (ovenc)
			printf("Case #%d: O won\n", g+1);
		else if (tensobra)
			printf("Case #%d: Game has not completed\n",g+1);
		else
			printf("Case #%d: Draw\n", g+1);
	}
	return 0;
}


