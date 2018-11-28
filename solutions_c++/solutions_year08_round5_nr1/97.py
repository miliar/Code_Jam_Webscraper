#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<fstream>
#include<iostream>

#define MAXC 3005
#define INFTY 99999

#define NORTH 0
#define EAST 1
#define SOUTH 2
#define WEST 3

using namespace std;

int minx[2*MAXC], maxx[2*MAXC], uminx[2*MAXC], umaxx[2*MAXC], lminx[2*MAXC], lmaxx[2*MAXC], area, x, y, dir;

inline int right(int d) {
	return (d+1)%4;
}

inline int left(int d) {
	return (d+3)%4;
}

int miny(int x) {
	int lo = 0;
	int hi = 2*MAXC;
	while(lo < hi) {
		int g = (lo + hi)/2;
		if(x >= uminx[g] && x < umaxx[g]) {
			hi = g;
		} else {
			lo = g+1;
		}
	}
	return lo;
}

int maxy(int x) {
	int lo = 0;
	int hi = 2*MAXC;
	while(lo < hi) {
		int g = (lo + hi + 1)/2;
		if(x >= lminx[g] && x < lmaxx[g]) {
			lo = g;
		} else {
			hi = g-1;
		}
	}
	return lo;
}

int main() {
	ifstream fin("A.in");
	ofstream fout("A.out");
	int N, L;
	fin >> N;
	for(int k = 1; k<=N; k++) {
		area = 0;
		fin >> L;
		string path = "";
		string segment;
		int t;
		for(int i = 0; i<L; i++) {
			fin >> segment;
			fin >> t;
			for(int j = 0; j<t; j++) {
				path = path+segment;
			}
		}
		for(int i = 0; i<2*MAXC; i++) {
			uminx[i] = lminx[i] = minx[i] = INFTY;
			umaxx[i] = lmaxx[i] = maxx[i] = -INFTY;
		}
		x = 0; y = 0; dir = NORTH;
		for(int i = 0; i<path.length(); i++) {
			char c = path[i];
//			if(c == 'R' || c == 'L') {	
//				cout << "(" << x << ", " << y << ")" << endl;
//			}
			if(c == 'R') {
				dir = right(dir);
			} else if(c == 'L') {
				dir = left(dir);
			} else if(c == 'F') {
				if(dir == NORTH) {
					if(x < minx[y+MAXC]) {
						minx[y+MAXC] = x;
					}
					if(x > maxx[y+MAXC]) {
						maxx[y+MAXC] = x;
					}
					area = area + x;
					y = y + 1;
				} else if(dir == SOUTH) {
					if(x < minx[y+MAXC-1]) {
						minx[y+MAXC-1] = x;
					}
					if(x > maxx[y+MAXC-1]) {
						maxx[y+MAXC-1] = x;
					}
					area = area - x;
					y = y - 1;
				} else if(dir == EAST) {
					x = x + 1;
				} else {
					x = x - 1;
				}
			}
		}
		if(area < 0) area = -area;
		int bigarea = 0;
		uminx[0]=minx[0];
		umaxx[0]=maxx[0];
		for(int i = 1; i<2*MAXC; i++) {
			if(uminx[i-1] < minx[i]) {
				uminx[i] = uminx[i-1];
			} else {
				uminx[i] = minx[i];
			}
//			cout << i << " " << uminx[i] << endl;
			if(umaxx[i-1] > maxx[i]) {
				umaxx[i] = umaxx[i-1];
			} else {
				umaxx[i] = maxx[i];
			}
		}
		lminx[2*MAXC-1] = minx[2*MAXC-1];
		lmaxx[2*MAXC-1] = maxx[2*MAXC-1];
		for(int i = 2*MAXC-2; i>=0; i--) {
			if(lminx[i+1] < minx[i]) {
				lminx[i] = lminx[i+1];
			} else {
				lminx[i] = minx[i];
			}
			if(lmaxx[i+1] > maxx[i]) {
				lmaxx[i] = lmaxx[i+1];
			} else {
				lmaxx[i] = maxx[i];
			}
		}
		for(int i = 0; i<2*MAXC; i++) {
			int xy = maxy(i-MAXC), ny = miny(i-MAXC);
			if(xy >= ny) {
//				cout << i << ", " << xy << ", " << ny << endl;
				bigarea += xy - ny + 1;
			}
		}
//		cout << "Case #" << k << ": " << bigarea << "," << area << endl;
		fout << "Case #" << k << ": " << bigarea - area << endl;
	}
	return 0;
}
