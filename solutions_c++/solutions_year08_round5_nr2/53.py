#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>
#define MAXN 20
#define EMPTY 1
#define WALL 0
#define BAWAH 0
#define KANAN 1
#define ATAS 2
#define KIRI 3
#define BIG 1929385123

using namespace std;

int a,b,c,d,e,f,g,h,i,j,k,l,m;
int n;
int jmlcase;
int panjang;
int tinggi;
int minmove[MAXN][MAXN][MAXN][MAXN][MAXN][MAXN];
int shoot[2][4][MAXN][MAXN];
int target[2];
int start[2];
char sex;
int state[MAXN][MAXN];
int movex[5] = {0,1,0,-1,0};
int movey[5] = {1,0,-1,0,0};
int original;
queue<int> q[8];

void taro(int abc,int def,int ghi,int jkl,int mno,int pqr) {
	q[0].push(abc);
	q[1].push(def);
	q[2].push(ghi);
	q[3].push(jkl);
	q[4].push(mno);
	q[5].push(pqr);
	}

void doit(void) {
	if (a == c && b == d) {
		if (minmove[e][f][c][d][e][f] > original + 1) {
			minmove[e][f][c][d][e][f] = original + 1;
			taro(e,f,c,d,e,f);
			}
		}
	if (a == e && b == f) {
		if (minmove[c][d][c][d][e][f] > original + 1) {
			minmove[c][d][c][d][e][f] = original + 1;
			taro(c,d,c,d,e,f);
			}
		}
	
	int aa;
	for (aa = 0;aa < 4;aa++) {
		int bb = a + movex[aa];
		int cc = b + movey[aa];
		if (state[bb][cc] == WALL) continue;
		if (minmove[bb][cc][c][d][e][f] > original + 1) {
			minmove[bb][cc][c][d][e][f] = original + 1;
			taro(bb,cc,c,d,e,f);
			}
		}
	}
			

int main() {
	
	scanf("%d",&jmlcase);
	for (m = 0;m < jmlcase;m++) {
		printf("Case #%d: ",m + 1);
		scanf("%d%d\n",&tinggi,&panjang);
		
		memset(state,0,sizeof(state));
		//printf("debug 1\n");
		for (a = 1;a <= tinggi;a++) {
			for (b = 1;b <= panjang;b++) {
				sex = getchar();
				if (sex == 'O') {
					sex = '.';
					start[0] = b;
					start[1] = a;
					}
				if (sex == 'X') {
					sex = '.';
					target[0] = b;
					target[1] = a;
					}
				
				if (sex == '.') {
					state[b][a] = EMPTY;
					}
				}
			sex = getchar();
			}
		//printf("debug 2\n");
		for (a = 1;a <= tinggi;a++) {
			for (b = 1;b <= panjang;b++) {
				if (state[b][a] == WALL) continue;
				for (c = 0;c < 4;c++) {
					d = b;
					e = a;
					while (state[d][e] == EMPTY) {
						d += movex[c];
						e += movey[c];
						}
					d -= movex[c];
					e -= movey[c];
					shoot[0][c][b][a] = d;
					shoot[1][c][b][a] = e;
					///if (b == 7 && a == 3) printf("%d %d %d : %d %d\n",c,b,a,d,e);
					}
				}
			}
		//printf("debug 3\n");
		
		memset(minmove,127,sizeof(minmove));
		
		for (e = 0;e < 4;e++) {
			for (f = 0;f < 4;f++) {
				if (e == f) continue;
				
		a = shoot[0][e][start[0]][start[1]];
		b = shoot[1][e][start[0]][start[1]];
		c = shoot[0][f][start[0]][start[1]];
		d = shoot[1][f][start[0]][start[1]];
		minmove[start[0]][start[1]][a][b][c][d] = 0;
		taro(start[0],start[1],a,b,c,d);

		/*q[6].push(e);
		q[7].push(f);*/
		}
		}
		
		//printf("%d %d\n",start[0],start[1]);
		while (!q[0].empty()) {
			a = q[0].front();
			q[0].pop();
			b = q[1].front();
			q[1].pop();
			c = q[2].front();
			q[2].pop();
			d = q[3].front();
			q[3].pop();
			e = q[4].front();
			q[4].pop();
			f = q[5].front();
			q[5].pop();
			
			original = minmove[a][b][c][d][e][f];
			//if (a == 7 && b == 3) printf("%d %d %d %d %d %d : %d\n",a,b,c,d,e,f,original);
			/*g = q[6].front();
			q[6].pop();
			h = q[7].front();
			q[7].pop();*/
			int oc = c;
			int od = d;
			int oe = e;
			int of = f;
			//try not to shoot
			doit();
			
			//shoot shoot shoot
			for (g = 0;g < 5;g++) {
				for (h = 0;h < 5;h++) {
					if (g == h) continue;
					
					c = shoot[0][g][a][b];
					d = shoot[1][g][a][b];
					if (g == 4) {
						c = oc;
						d = od;
						}
				
					e = shoot[0][h][a][b];
					f = shoot[1][h][a][b];
					if (h == 4) {
						e = oe;
						f = of;
						}
					
					//if (a == 7 && b == 3 && original == 1) printf("%d %d %d %d %d %d %d %d\n",a,b,c,d,e,f,g,h);
					
					doit();
					}
				}
			}
		
		int minanswer = BIG;
		//printf("%d %d\n",target[0],target[1]);
		for (a = 1;a <= panjang;a++) {
			for (b = 1;b <= tinggi;b++) {
				for (c = 1;c <= panjang;c++) {
					for (d = 1;d <= tinggi;d++) {
						minanswer = min(minanswer,minmove[target[0]][target[1]][a][b][c][d]);
						}
					}
				}
			}
		if (minanswer == BIG) printf("THE CAKE IS A LIE\n");
		else printf("%d\n",minanswer);
		}
			
					
			
		
		
	
	return 0;
	}
