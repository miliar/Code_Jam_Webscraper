#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

#define fr(i,j,k) for(int (i) = (j) ; (i) < (k); ++(i))
#define cl(x) memset(x, 0, sizeof(x))
char in[5][5];

int main(){

	int t; int caso =1;
	scanf("%d\n", &t);
	while(t--){
		fr(i,0,4) cl(in[i]);
		fr(i,0,4) scanf("%s\n", in[i]);
		//fr(i,0,4) cout << in[i] << endl;
		bool xwon =false, ywon = false, empty = false;
		int hx, hy, vx, vy, d1x, d1y, d2x,d2y;
		d1y = d1x = d2y = d2x = 0;
		fr(i,0,4) {
			hx = hy = vx = vy = 0;
			fr(j,0,4) {
				if( in[i][j] == '.') empty = true;
				if( in[i][j] == 'X' || in[i][j] == 'T') hx++;
				if( in[i][j] == 'O' || in[i][j] == 'T') hy++;
				if( in[j][i] == 'X' || in[j][i] == 'T') vx++;
				if( in[j][i] == 'O' || in[j][i] == 'T') vy++;
			}

			if( hx == 4 || vx == 4 ) xwon = true;
			if( hy == 4 || vy == 4 ) ywon = true;
			if( in[i][i] == 'X' || in[i][i] == 'T') d1x++;
			if( in[i][3-i] == 'X' || in[i][3-i] == 'T') d2x++;
			if( in[i][i] == 'O' || in[i][i] == 'T') d1y++;
			if( in[i][3-i] == 'O' || in[i][3-i] == 'T') d2y++;

		}
		if( d1x == 4 || d2x == 4 ) xwon = true;
		if( d1y == 4 || d2y == 4 ) ywon = true;

		if( xwon ) printf("Case #%d: X won\n",caso++ );
		else if( ywon ) printf("Case #%d: O won\n",caso++ );
		else if( empty ) printf("Case #%d: Game has not completed\n", caso++ );
		else printf("Case #%d: Draw\n",caso++ );
	}


	return 0;
}