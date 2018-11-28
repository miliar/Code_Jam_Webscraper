#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int T,H,W,V[105][105];
char map[105][105];

void ff(int x, int y, char cur);

int main() {
	ifstream fin("cjb.in");
	ofstream fout("cjb.out");

	fin>>T;

	for (int i = 0; i < T; i++) {
		fin>>H>>W;
		for (int y=0;y<H;y++) {
			for (int x=0;x<W;x++)
				fin>>V[y][x];
		}

		char cur='a';
		memset(map,0,sizeof(map));
		fout<<"Case #"<<i+1<<":"<<"\n";
		for (int y=0;y<H; y++) {
			for (int x=0;x<W;x++) {
				if (map[y][x]==0) ff(x,y,cur++);
				//cout<<"("<<x<<","<<y<<"):"<<map[y][x]<<"\n";
				fout<<map[y][x];
				if (x!=W-1) fout<<" ";			
			}
			fout<<"\n";
		}
	}
}

bool valid(int x, int y) {
	return x>=0&&y>=0&&x<W&&y<H;
}

static int dx[]={0,-1,1,0};
static int dy[]={-1,0,0,1};
#define NX(i) dx[i]+x
#define NY(i) dy[i]+y

void floodsto(int x, int y, int &nx, int &ny) {
	nx=-1;
	for (int i = 0; i < 4; i++) {
		if (!valid(NX(i),NY(i))) continue;
		if ((nx==-1&&V[NY(i)][NX(i)]<V[y][x])||
			(nx!=-1&&V[ny][nx]>V[NY(i)][NX(i)])) {
			nx=NX(i);ny=NY(i);
		}
	}
}

void ff(int x, int y, char cur) {
	if (map[y][x]!=0)return;

	int nx=-1,ny;
	map[y][x]=cur;
	floodsto(x,y,nx,ny);
	if (nx!=-1)
		ff(nx,ny,cur);

	for (int i = 0; i < 4; i++) {
		floodsto(NX(i),NY(i),nx,ny);

		if (nx==-1) continue;
		if (nx==x&&ny==y) {
			ff(NX(i),NY(i),cur);
		}
	}
}
