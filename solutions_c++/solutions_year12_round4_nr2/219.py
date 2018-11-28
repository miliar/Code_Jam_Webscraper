#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <iostream>

using namespace std;


int T,N;
int r[1010];
int x[1010], y[1010];
int o[1010];
int W,L;
bool swapped = false;

int main(){
	cin >> T;
	for (int times = 0; times < T; ++times){
		swapped = false;
		cin >> N >> W >> L;
		/*
		if (W < L) {
			int tmp = W;
			W = L;
			L = tmp;
			swapped = true;
		}
		*/
		for (int i = 0; i < N; ++i){
			cin >> r[i];
			o[i] = i;
		}
		for (int i = 0; i < N-1; ++i){
			for (int j = N - 1; j > i; --j){
				if (r[o[j]] > r[o[j-1]]) {
					int tmp = o[j];
					o[j]=o[j-1];
					o[j-1]=tmp;
				}
			}
		}
		int dir = 1;
		for (int i = 0; i < N; ++i){
			if (i == 0) {
				x[i] = 0;
			} else {
				x[i] = x[i-1] + (r[i-1]+r[i])*dir;
				if (x[i] < 0 || x[i] > W) {
					dir *= -1;
					x[i] = (dir == 1) ? 0 : W;
				}
			}
			y[i] = 0;
			for (int j = 0; j < i; ++j) {
				if (abs(x[i]-x[j]) < r[i]+r[j]) {
					int ny = y[j] + r[i] + r[j];
					if (ny > y[i]) {
						y[i] = ny;
					}
				}
			}
		}
		cout << "Case #" << times+1 << ":";
		for (int i = 0; i< N; ++i){
			cout << " " << x[i] << " " << y[i];
		}
		cout << endl;
	}
	return 0;
}