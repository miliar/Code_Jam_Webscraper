#include <iostream>
#include <fstream>
using namespace std;

int map[101][101];
char lab[101][101];
int h,w;

void min(int i, int j, int &di, int &dj) {
	int alt=map[i][j]; di=dj=0;
	if (i>0 && map[i-1][j]<alt) { alt=map[i-1][j]; di=-1; dj=0; } // north
	if (j>0 && map[i][j-1]<alt) { alt=map[i][j-1]; di=0; dj=-1; } // west
	if (j<w-1 && map[i][j+1]<alt) { alt=map[i][j+1]; di=0; dj=+1; } // east
	if (i<h-1 && map[i+1][j]<alt) { alt=map[i+1][j]; di=+1; dj=0; } // south
}

struct to_do {int i,j;};
void fill(int i, int j, char l) {
	int di,dj;
	min(i,j,di,dj);
//	cerr<<i<<j<<" ";
	while (di||dj) {
		i+=di; j+=dj;
//		cerr<<i<<j<<" ";
		min(i,j,di,dj);
	}
//	cerr<<endl;
	
	static to_do list[100*100+1];
	int n=1;
	list[0].i=i; list[0].j=j;
	lab[i][j]=l;
	while (n) {
		n--;
		i=list[n].i; j=list[n].j;
//		cerr<<i<<" "<<j<<"  "<<map[i][j]<<"  "<<l<<endl;
		
		
#define _test(mi,mj) \
	if (lab[i+mi][j+mj]==0) { \
		min(i+mi,j+mj,di,dj); \
		if (di==-mi && dj==-mj) { \
			list[n].i=i+mi; list[n].j=j+mj; \
			lab[i+mi][j+mj]=l; n++; \
		} \
	}

			if (i>0) _test(-1,0);
			if (i+1<h) _test(1,0);
			if (j>0) _test(0,-1);
			if (j+1<w) _test(0,1);
			
	}
}

int main(int argc, char *argv[]) {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	
	int t;
	fin>>t;
	for (int i=0;i<t;i++) {
		
		fin>>h>>w;
		for (int j=0;j<h;j++) {
			for (int k=0;k<w;k++) {
				fin>>map[j][k];
			}
		}
		
		char cl='a';
		memset(lab,0,sizeof(lab));
		for (int j=0;j<h;j++) {
			for (int k=0;k<w;k++) {
				if (lab[j][k]==0) {
					fill(j,k,cl);
					cl++;
				}
			}
		}
		
		fout<<"Case #"<<i+1<<":"<<endl;
		for (int j=0;j<h;j++) {
			for (int k=0;k<w;k++) {
				fout<<lab[j][k]<<' ';
			}
			fout<<endl;
		}
	}
	
	fin.close();
	fout.close();
	return 0;
}

