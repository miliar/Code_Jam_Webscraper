#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define O 3010

char a[2*O][2*O];
int m;
int dir, x, y, px, py;
char tmp[64];
int in1, in2, cnt;
int minX[2*O], maxX[2*O];
int minY[2*O], maxY[2*O];

void move() {
	if (dir==0)		y++;
	if (dir==1)		x++;
	if (dir==2)		y--;
	if (dir==3)		x--;
}

int main () {
	int i, j, l, pom;
	int t, c;
	char *p;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	for (scanf("%d", &t), c=1; c<=t; c++) {		
		fprintf(stderr,"%d\n",c);
		dir=0;
		x=y=O;
		memset(a,0,sizeof(a));
		for (i=0; i<2*O; i++) {
			minX[i]=minY[i]=(int)1e9;
			maxX[i]=maxY[i]=-1;
		}
		for (scanf("%d", &m); m>0; m--) {
			scanf("%s", tmp);
			for (scanf("%d", &l); l>0; l--)
				for (p=tmp; *p; p++) {
					px=x;
					py=y;
					if (*p=='F')		move();
					if (*p=='L')		dir=(dir-1+4)%4;
					if (*p=='R')		dir=(dir+1)%4;
					if (px!=x) {
						pom=min(px,x);
						a[pom][y]|=1;
						minY[pom]=min(minY[pom],y);
						maxY[pom]=max(maxY[pom],y);
					}
					if (py!=y)	{
						pom=min(py,y);
						a[x][pom]|=2;
						minX[pom]=min(minX[pom],x);
						maxX[pom]=max(maxX[pom],x);
					}
				}
			}
		cnt=0;
		for (i=0; i<2*O; i++) {
			in1=in2=0;
			for (j=0; j<2*O; j++) {
				if (a[i][j]&1) 
					in1^=1;									

				if (!in1 && minY[i]<=j && j<maxY[i]) 
					if (!(a[i][j]&4)) {
						a[i][j]^=4;
						cnt++;
					}

				if (a[j][i]&2) 
					in2^=1;
				
				if (!in2 && minX[i]<=j && j<maxX[i]) 
					if (!(a[j][i]&4)) {
						a[j][i]^=4;
						cnt++;
					}
			}			
		}		
		printf("Case #%d: %d\n",c,cnt);
	}
	return 0;
}