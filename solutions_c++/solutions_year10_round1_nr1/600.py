#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

char world[60][60];
char str[60], ck;
int rows,cols,k,v,z,cn;
bool red,blue,sea;

int range[8][2] = { {0,1}, {1,0}, {-1,0}, {0,-1}, {-1,-1}, {-1,1}, {1,1}, {1,-1} };

void rec(int r, int c, int dr, int dc, int n) {
	if (n==0) {
		ck=world[r][c];
		rec(r+dr,c+dc,dr,dc,1);
	} else {
		if (r >= 0 && r < rows && c >= 0 && c < cols) {
			if (world[r][c]==ck) {
				if (n+1==k) {
					if (ck=='B') blue=true;
					else red=true;
				}
				else {
					rec(r+dr,c+dc,dr,dc,n+1);
				}
			}
			
		}
		
	}
}

void dbg() {
	for (int i=0; i < rows; ++i) {
		for (int j=0; j < cols; ++j) {
			if (world[i][j])
				printf("%c",world[i][j]);
			else break;
		}
		printf("\n");
	}
}

void process() {
	scanf("%d %d",&rows,&k);
	cols=rows;
	memset(world,0,sizeof(world));
	for (int i=0; i < rows; ++i) {
		scanf("%s",str);
		z=0;
		for (int j=0; j < cols; ++j) {
			v=cols-1-j;
			if (str[v]!='.') {
				world[i][z++]=str[v];
			}
		}
	}
	
	//dbg();
	
	red=false;
	blue=false;
	sea=true;
	
	for (int i=0; i < rows && sea; ++i){
		for (int j=0; j < cols && sea; ++j) {
			if (red && blue) sea=false;
			if (world[i][j]) {
				for (int x=0; x < 8; ++x) {
					rec(i,j,range[x][0],range[x][1],0);
				}
			} else {
				break;
			}
		}
	}
	
	printf("Case #%d: ",++cn);
	if (red && blue) printf("Both");
	else if (red) printf("Red");
	else if (blue) printf("Blue");
	else printf("Neither");
	printf("\n");
	fflush(stdout);
}




int main() {
	int cases;
	scanf("%d",&cases);
	while (cases--) {
		process();
	}

	return 0;
}
