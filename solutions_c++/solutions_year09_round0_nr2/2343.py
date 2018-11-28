#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define UP 1
#define LEFT 2
#define RIGHT 3
#define DOWN 4

int field[101][101];
int grp[10001][10001];
char sol[101][101];
char chk[10001];
int xx, yy;

void goNext(int n, char ch)
{
	int i;

	chk[n]++;
	sol[n/yy][n%yy] = ch;

	for(i=0; i<xx*yy; i++) 
		if(chk[i]==0 && grp[i][n]) goNext(i, ch);

}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("cj02large.out", "w", stdout);

	int i, j, cas, now, minval, mindir;
	char reg;
	scanf("%d\n",&cas);

	for(now = 1; now <= cas; now++) {
		reg = 'a';
		scanf("%d %d\n",&xx,&yy);

		memset(grp, 0, sizeof(grp));
		memset(chk, 0, sizeof(chk));

		for(i=0; i<xx; i++) {
			for(j=0; j<yy; j++) {
				scanf("%d",&field[i][j]);
				sol[i][j] = 0;
			}
		}

		
		for(i=0; i<xx; i++) {
			for(j=0; j<yy; j++) {
				minval = 99999;
				mindir = 0;
				if(i > 0 && field[i-1][j] < field[i][j]) {
					if(field[i-1][j] < minval) {
						minval = field[i-1][j];
						mindir = UP;
					}	
				}
				if(j > 0 && field[i][j-1] < field[i][j]) {
					if(field[i][j-1] < minval) {
						minval = field[i][j-1];
						mindir = LEFT;
					}	
				}
				if(j+1 < yy && field[i][j+1] < field[i][j]) {
					if(field[i][j+1] < minval) {
						minval = field[i][j+1];
						mindir = RIGHT;
					}	
				}
				if(i+1 < xx && field[i+1][j] < field[i][j]) {
					if(field[i+1][j] < minval) {
						minval = field[i+1][j];
						mindir = DOWN;
					}	
				}
				if(mindir == UP) grp[(i-1)*yy+(j)][(i)*yy+(j)] = grp[(i)*yy+(j)][(i-1)*yy+(j)] = 1;
				if(mindir == LEFT) grp[(i)*yy+(j)][(i)*yy+(j-1)] = grp[(i)*yy+(j-1)][(i)*yy+(j)] = 1;
				if(mindir == RIGHT) grp[(i)*yy+(j)][(i)*yy+(j+1)] = grp[(i)*yy+(j+1)][(i)*yy+(j)] = 1;
				if(mindir == DOWN) grp[(i+1)*yy+(j)][(i)*yy+(j)] = grp[(i)*yy+(j)][(i+1)*yy+(j)] = 1;

			}
		}

		for(i=0; i<xx*yy; i++) {
			if(chk[i] == 0) {
				goNext(i, reg++);
			}
		}


		printf("Case #%d:\n",now);
		for(i=0; i<xx; i++) {
			for(j=0; j<yy; j++) {
				printf("%c",sol[i][j]);
				if(j+1 < yy) printf(" ");
			}
			printf("\n");
		}
	}


	return 0;
}