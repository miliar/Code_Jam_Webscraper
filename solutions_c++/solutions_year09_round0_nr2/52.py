#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int t,h,w;
int a[105][105];
int mark[105][105];
int m;
int mark2Ch[10005];
char ch;

int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

bool onBoard(int y, int x) {
	return (0<=y && y<h && 0<=x && x<w);
}

int main() {
    FILE *fin=fopen("B-large.in","r");
    FILE *fout=fopen("B-large.out","w");
	fscanf(fin,"%d",&t);
	for (int test=1;test<=t;test++) {
		printf("%d/%d\r",test,t);
		memset(mark,-1,sizeof(mark));
		ch='a'; m=0;
		fscanf(fin,"%d %d",&h,&w);
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				fscanf(fin,"%d",&a[i][j]);
			}
		}
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				if (mark[i][j]!=-1) continue;
				int y=i, x=j;
				int sink=0;
				while (mark[y][x]==-1) {
					mark[y][x]=m;
					int mina=-1, ny, nx;
					for (int d=0;d<4;d++) {
						int y2=y+dir[d][0], x2=x+dir[d][1];
						if (onBoard(y2,x2) && a[y2][x2]<a[y][x]) {
							if (mina==-1 || a[y2][x2]<mina) {
								mina=a[y2][x2]; ny=y2; nx=x2;
							}
						}
					}
					if (mina==-1) { sink=1; break; }
					else { y=ny; x=nx; }
				}
				if (sink) { mark2Ch[m]=ch; ch++; }
				else {
					mark2Ch[m]=mark2Ch[mark[y][x]];
				}
				m++;
			}
		}
		fprintf(fout,"Case #%d:\n",test);
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				if (j!=0) fprintf(fout," ");
				fprintf(fout,"%c",mark2Ch[mark[i][j]]);
			}
			fprintf(fout,"\n");
		}
	}
    return 0;
}
