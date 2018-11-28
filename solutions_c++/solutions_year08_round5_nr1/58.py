#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <stack>

#define ATAS 0
#define KANAN 1
#define BAWAH 2
#define KIRI 3
#define MAXN 275

using namespace std;

int a,b,c,d,e,f;
int jmlcase;
int hub[MAXN][MAXN][4];
int movex[4] = {0,1,0,-1};
int movey[4] = {1,0,-1,0};
int outside[MAXN][MAXN];
int posx;
int posy;
int face;
int n;
char move[MAXN];


int main() {
	
	scanf("%d",&jmlcase);
	for (f = 0;f < jmlcase;f++) {
		printf("Case #%d: ",f + 1);
		memset(hub,1,sizeof(hub));
		posx = 102;
		posy = 102;
		face = ATAS;
		
		scanf("%d",&n);
		//printf("%d\n",n);
		for (a = 0;a < n;a++) {
			scanf("%s",move);
			scanf("%d",&b);
			//printf("%d %s\n",b,move);
			for (c = 0;c < b;c++) {
				for (d = 0;d < strlen(move);d++) {
					//printf("%d %d %d\n",posx,posy,face);
					if (move[d] == 'F') {
					
						if (face == ATAS) {
							
							hub[posx - 1][posy][KANAN] = hub[posx][posy][KIRI] = 0;
							}
						if (face == BAWAH) {
							hub[posx - 1][posy - 1][KANAN] = hub[posx][posy - 1][KIRI] = 0;
							}
						if (face == KANAN) {
							hub[posx][posy - 1][ATAS] = hub[posx][posy][BAWAH] = 0;
							}
						if (face == KIRI) {
							hub[posx - 1][posy - 1][ATAS] = hub[posx - 1][posy][BAWAH] = 0;
							}
						
						posx += movex[face];
						posy += movey[face];
						continue;
						}
					if (move[d] == 'R') {
						face++;
						face %= 4;
						continue;
						}
					face--;
					if (face < 0) face += 4;
					}
				}
			}
		
		memset(outside,0,sizeof(outside));
		
		outside[1][1] = 1;
		stack<int> sx;
		stack<int> sy;
		sx.push(1);
		sy.push(1);
		
		while (!sx.empty()) {
			int tx = sx.top();
			int ty = sy.top();
			sx.pop();
			sy.pop();
			if (tx <= 0 || ty <= 0 || tx >= 254 || ty >= 254) continue;
			for (a = 0;a < 4;a++) {
				if (!hub[tx][ty][a]) continue;
				b = tx + movex[a];
				c = ty + movey[a];
				if (outside[b][c]) continue;
				outside[b][c] = 1;
				sx.push(b);
				sy.push(c);
				}
			}
		int answer = 0;
		for (a = 1;a <= 254;a++) {
			for (b = 1;b <= 254;b++) {
				if (!outside[a][b]) continue;
				//checkleft;
				c = a;
				d = b;
				while (c >= 0 && hub[c][d][KIRI]) c--;
				if (c >= 0) {
					c = a;
					d = b;
					while (c <= 254 && hub[c][d][KANAN]) c++;
					if (c <= 254) {
						answer++;
						continue;
						}
					}
				//check updown
				c = a;
				d = b;
				while (d >= 0 && hub[c][d][BAWAH]) d--;
				if (d >= 0) {
					c = a;
					d = b;
					while (d <= 254 && hub[c][d][ATAS]) d++;
					if (d <= 254) {
						answer++;
						continue;
						}
					}
				}
			}
		
		printf("%d\n",answer);
		}
				
		
	
	return 0;
	}
