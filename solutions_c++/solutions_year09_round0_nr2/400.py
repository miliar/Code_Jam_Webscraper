
#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
using namespace std;


int h,w;
char ch;
int a[100][100];
char b[100][100];

int dirs[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

void color(int i, int j) {
	if (b[i][j]!='.') return;

	int mi=-1,mj=-1;
	for (int d=0; d<4; d++) {
		int ii = i+dirs[d][0];
		int jj = j+dirs[d][1];
		if (ii>=0 && jj>=0 && ii<h && jj<w) {
			if (a[ii][jj]<a[i][j]) {
				if (mi==-1 || a[ii][jj]<a[mi][mj]) {
					mi = ii;
					mj=jj;
				}
			}
		}
	}
	if (mi==-1) {
		b[i][j]=ch;
		ch++;
	}
	else {
		color(mi,mj);
		b[i][j]=b[mi][mj];
	}
}

void solveCase() {
	scanf("%d %d",&h,&w);
	for (int i=0; i<h; i++) {
		for (int j=0; j<w; j++) {
			scanf("%d", &a[i][j]);
			b[i][j]='.';
		}
	}

	ch = 'a';

	for (int i=0; i<h; i++) {
		for (int j=0; j<w; j++) {
			color(i,j);
			if (j>0) cout<<" ";
			cout<<b[i][j];
		}
		cout<<"\n";
	}
}


int main() {
	int ncases;
	scanf("%d",&ncases);
	for (int i=0; i<ncases; i++) {
		cout<<"Case #"<<i+1<<":\n";
		solveCase();
	}
	return 0;
}

