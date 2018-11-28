#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;

const char *wynik[4]={"Draw", "X won", "O won", "Game has not completed"};

char tab[5][10];


int licz() {
    bool X=false;
    bool O=false;
    bool K=false;
    for (int i=0; i<4; i++) for (int j=0; j<4; j++)
	K=K||(tab[i][j]=='.');
    for (int i=0; i<4; i++) {
	int tXA=0;
	int tOA=0;
	int tXB=0;
	int tOB=0;
	for (int j=0; j<4; j++) {
	    if (tab[i][j]=='X' || tab[i][j]=='T') tXA++;
	    if (tab[j][i]=='X' || tab[j][i]=='T') tXB++;
	    if (tab[i][j]=='O' || tab[i][j]=='T') tOA++;
	    if (tab[j][i]=='O' || tab[j][i]=='T') tOB++;
	}
	X=X|| tXA==4 || tXB==4;
	O=O|| tOA==4 || tOB==4;
    }
	int tXA=0;
	int tOA=0;
	int tXB=0;
	int tOB=0;
	for (int i=0; i<4; i++) {
	    if (tab[i][i]=='X' || tab[i][i]=='T') tXA++;
	    if (tab[i][3-i]=='X' || tab[i][3-i]=='T') tXB++;
	    if (tab[i][i]=='O' || tab[i][i]=='T') tOA++;
	    if (tab[i][3-i]=='O' || tab[i][3-i]=='T') tOB++;
	}
	X=X|| tXA==4 || tXB==4;
	O=O|| tOA==4 || tOB==4;
    if (X) return 1;
    if (O) return 2;
    if (K) return 3;
    return 0;
}


int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf ("%s %s %s %s", tab[0], tab[1], tab[2], tab[3]);
        printf("Case #%d: %s\n", t, wynik[licz()]);
    }
    return 0;
}

