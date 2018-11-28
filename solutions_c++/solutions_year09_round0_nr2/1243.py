#include<iostream>
#include<string>
#include<cstring>
using namespace std;

// north west east south
const int dh[] = {-1, 0, 0, 1};
const int dw[] = { 0,-1, 1, 0};

int H, W, T;

int height[128][128];
int parent[128 * 128];
char colour[128 * 128];

int ds_get(int idx) {
    if(parent[idx] == idx) return idx;
    return parent[idx] = ds_get(parent[idx]);
}

void ds_join(int a, int b) {
    parent[ds_get(a)] = ds_get(b);
}

int main() {
    cin >> T;
    for(int tt = 1; tt <= T; ++tt) {
	cin >> H >> W;
	for(int h = 0; h < H; ++h) {
	    for(int w = 0; w < W; ++w) {
		cin >> height[h][w];
		parent[h * 128 + w] = h * 128 + w;
		colour[h * 128 + w] = -1;
	    }
	}
	for(int h = 0; h < H; ++h) {
	    for(int w = 0; w < W; ++w) {
		int choice = -1;
		int lowest = height[h][w];
		for(int d = 0; d < 4; ++d) {
		    int nh = h + dh[d];
		    int nw = w + dw[d];
		    if(nh < 0 || nw < 0 || nh >= H || nw >= W) continue;
		    if(height[nh][nw] < lowest) {
			choice = d;
			lowest = height[nh][nw];
		    }
		}
		if(choice == -1) continue;
		int nh = h + dh[choice];
		int nw = w + dw[choice];
		ds_join(h * 128 + w, nh * 128 + nw);
	    }
	}
	cout << "Case #" << tt << ":" << endl;
	char C = 'a';
	for(int h = 0; h < H; ++h) {
	    for(int w = 0; w < W; ++w) {
		int c = ds_get(h * 128 + w);
		if(colour[c] == -1) {
		    colour[c] = C;
		    ++C;
		}
		if(w > 0) cout << ' ';
		cout << colour[c];
	    }
	    cout << endl;
	}
    }
    return 0;
}

