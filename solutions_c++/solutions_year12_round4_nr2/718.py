/*************************************************************************
    > File Name: b.cpp
    > Created Time: 六  5/26 22:27:59 2012
 ************************************************************************/

#include<iostream>
using namespace std;

const int dead = -2147483600;
int r[1024], x[1024], y[1024];
int l[1024], W, L, N;

bool check(int i) {
	if(x[l[i]] < 0 || x[l[i]] > W) return false;
	if(y[l[i]] < 0 || y[l[i]] > L) return false;
	for(int u = 0; u < i; u ++) {
		double X, Y, R;
		X = x[l[u]] - x[l[i]];
		Y = y[l[u]] - y[l[i]];
		R = r[l[u]] + r[l[i]];
		if((X * X + Y * Y) < (R * R - 1e-8)) return false;
	}
	return true;
}

bool cmp(int x, int y) {
	return r[x] > r[y];
}

int main() {
	int Ncase;
	cin >> Ncase;
	for(int c = 1; c <= Ncase; c ++) {
		cin >> N >> L >> W;
		for(int i = 0; i < N; i ++) {
			cin >> r[i];
			l[i] = i;
		}
		sort(l, l + N, cmp);
		int x1, y1, x2, y2, x3, y3, x4, y4;
		x1 = y1 = x2 = y2 = x3 = y3 = x4 = y4 = dead;
		for(int u = 0; u < N; u ++) {
			int i = l[u];
			int R = r[i];
			if(x1 == dead && y1 == dead) {
				x[i] = 0;
				y[i] = 0;
				if(check(u)) {
					x1 = y1 = R;
					continue;
				}
			} else {
				x[i] = x1 + R;
				y[i] = 0;
				if(check(u)) {
					x1 = x1 + R * 2;
					continue;
				}
				x[i] = 0;
				y[i] = y1 + R;
				if(check(u)) {
					y1 = y1 + R * 2;
					continue;
				}
			}

			if(x2 == dead && y2 == dead) {
				x[i] = W;
				y[i] = 0;
				if(check(u)) {
					x2 = W - R; 
					y2 = R;
					continue;
				}
			} else {
				x[i] = x2 - R;
				y[i] = 0;
				if(check(u)) {
					x2 = x2 - R * 2;
					continue;
				}
				x[i] = W;
				y[i] = y2 + R;
				if(check(u)) {
					y2 = y2 + R * 2;
					continue;
				}
			}

			if(x3 == dead && y3 == dead) {
				x[i] = W;
				y[i] = L;
				if(check(u)) {
					x3 = W - R; 
					y3 = L - R;
					continue;
				}
			} else {
				x[i] = x3 - R;
				y[i] = L;
				if(check(u)) {
					x3 = x3 - R * 2;
					continue;
				}
				x[i] = W;
				y[i] = y3 - R;
				if(check(u)) {
					y3 = y3 - R * 2;
					continue;
				}
			}
			if(x4 == dead && y4 == dead) {
				x[i] = 0;
				y[i] = L;
				if(check(u)) {
					x4 = R; 
					y4 = L - R;
					continue;
				}
			} else {
				x[i] = x4 + R;
				y[i] = L;
				if(check(u)) {
					x4 = x4 + R * 2;
					continue;
				}
				x[i] = W;
				y[i] = y4 - R;
				if(check(u)) {
					y4 = y4 - R * 2;
					continue;
				}

			}
			if(x1 != dead && y1 != dead) {
				x[i] = x1 + R;
				y[i] = y1 + R;
				if(check(u)) {
					x1 = x1 + R * 2;
					y1 = y1 + R * 2;
					continue;
				}
			}
			if(x2 != dead && y2 != dead) {
				x[i] = x2 - R;
				y[i] = y2 + R;
				if(check(u)) {
					x2 = x2 - R * 2;
					y2 = y2 + R * 2;
					continue;
				}
			}
			if(x3 != dead && y3 != dead) {
				x[i] = x3 - R;
				y[i] = y3 - R;
				if(check(u)) {
					x3 = x3 - R * 2;
					y3 = y3 - R * 2;
					continue;
				}
			}
			if(x4 != dead && y4 != dead) {
				x[i] = x4 + R;
				y[i] = y4 - R;
				if(check(u)) {
					x4 = x4 + R * 2;
					y4 = y4 - R * 2;
					continue;
				}
			}
			cout << "Fuck!!!" << endl;
		}
		cout << "Case #" << c << ":";
		for(int i = 0; i < N; i ++) {
			cout << " " << y[i] << ".0 " << x[i] << ".0"; 
		}
		cout << endl;
	}
}
