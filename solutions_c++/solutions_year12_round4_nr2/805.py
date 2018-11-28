#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct guy {
	float r;
	float x, y;
	int n;
	bool p;
};

bool operator<(const guy &a, const guy& b)  { return a.r > b.r || (a.r == b.r && a.n < b.n); }

bool filled(guy* g, int N) {
	for (int i=0; i<N; i++)
		if (g[i].p == false) return false;
	return true;
}

void put(guy* g, int N, float W, float L, int x0, int y0, bool c) {
	if (filled(g, N)) return;
	
	vector<guy> gg;
	for (int i=0; i<N; i++)
		if (g[i].p == false) 	gg.push_back(g[i]);
	sort(gg.begin(), gg.end());
	float K;

	if (c) {
		K = gg[0].r;
		g[gg[0].n].x = 0;
		g[gg[0].n].y = 0;
		g[gg[0].n].p = true;
		float x = K;
		float y = K;
		for (int i=1; i<gg.size(); i++) {
//			cout << i <<  endl;
			if (gg[i].r+x <= W && gg[i].r+y <= L) {
				if (i%2 == 1) {
						g[gg[i].n].x = gg[i].r+x+x0;
						g[gg[i].n].y = 0.0f+y0;
						g[gg[i].n].p = true;
						x += 2*gg[i].r;
				} else {
						g[gg[i].n].x = 0.0f+x0;
						g[gg[i].n].y = gg[i].r+y+y0;
						y += 2*gg[i].r;
						g[gg[i].n].p = true;
				}
			} else if (gg[i].r+x <= W) {
						g[gg[i].n].x = gg[i].r+x+x0;
						g[gg[i].n].y = 0.0f+y0;
						g[gg[i].n].p = true;
						x += 2*gg[i].r;
			} else if (gg[i].r+y <= L) {
						g[gg[i].n].x = 0.0f+x0;
						g[gg[i].n].y = gg[i].r+y+y0;
						y += 2*gg[i].r;
						g[gg[i].n].p = true;
			} else break;
		}
	} else {
		K = gg[0].r*2;
		g[gg[0].n].x = K/2+x0;
		g[gg[0].n].y = K/2+y0;
		g[gg[0].n].p = true;
		float x = K;
		float y = K;
		for (int i=1; i<gg.size(); i++) {
			if (gg[i].r+x <= W && gg[i].r+y <= L) {
				if (i%2 == 1) {
						g[gg[i].n].x = gg[i].r+x+x0;
						g[gg[i].n].y = 0.0f+y0;
						g[gg[i].n].p = true;
						x += 2*gg[i].r;
				} else {
						g[gg[i].n].x = 0.0f+x0;
						g[gg[i].n].y = gg[i].r+y+y0;
						y += 2*gg[i].r;
						g[gg[i].n].p = true;
				}
			} else if (gg[i].r+x <= W) {
						g[gg[i].n].x = gg[i].r+x+x0;
						g[gg[i].n].y = 0.0f+y0;
						g[gg[i].n].p = true;
						x += 2*gg[i].r;
			} else if (gg[i].r+y <= L) {
						g[gg[i].n].x = 0.0f+x0;
						g[gg[i].n].y = gg[i].r+y+y0;
						y += 2*gg[i].r;
						g[gg[i].n].p = true;
			} else break;
		}
	}
	put(g, N, W-K, L-K, x0+K, y0+K, false);
}

int main(int argc, char* argv[]) {
	ifstream fff;
	fff.open(argv[1]);
	int T;
	fff >> T;
	for (int ttt=0; ttt<T; ttt++) {
		cout << "Case #" << ttt+1 << ": ";
		int N;
		float W, L;
		fff >> N >> W >> L;
		guy* g = new guy[N];
		for (int i=0; i<N; i++) {
			float r;
			fff >> r;
			g[i].r = r;
			g[i].x = g[i].y = 0.0f;
			g[i].n = i;
			g[i].p = false;
		}
		put(g, N, W, L, 0, 0, true);
		for (int i=0; i<N; i++) printf("%.1f %.1f ", g[i].x, g[i].y);
		cout << endl;
		delete[] g;
	}	
	fff.close();
}
