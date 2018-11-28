
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;

int tst;
char buf[8][8];
bool xw, ow, gs;

void chk(int r, int c, int dr, int dc) {
	int nx=0, no=0;
	for (int i=0; i<4; i++) {
		switch (buf[r][c]) {
		case 'X': nx++; break;
		case 'O': no++; break;
		case 'T': nx++; no++; break;
		case '.': gs=true;
		}
		r+=dr;
		c+=dc;
	}
	if (nx>3) xw=true;
	if (no>3) ow=true;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		for (int i=0; i<4; i++)
			scanf("%s", buf[i]);
			
		xw=false; ow=false; gs=false;
		
		for (int r=0; r<4; r++)
			chk(r,0,0,1);
			
		for (int c=0; c<4; c++)
			chk(0,c,1,0);
			
		chk(0,0,1,1);
		chk(0,3,1,-1);
		
		printf("Case #%d: ", cas);
		if (xw) printf("X won\n");
		else if (ow) printf("O won\n");
		else if (gs) printf("Game has not completed\n");
		else printf("Draw\n");
	}
}
