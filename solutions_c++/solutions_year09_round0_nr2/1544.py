//use g++
#include <iostream>

using namespace std;

const int MAX = 20000;

struct cell {
	int alt;
	int num;
	bool sink;
};

bool is_sink(cell** map, int h, int w) {
	int a = map[h][w].alt;
	return map[h-1][w].alt >=a &&
		map[h+1][w].alt >=a &&
		map[h][w-1].alt >=a &&
		map[h][w+1].alt >=a;
}

inline int min(int a, int b) {
	return a<b ? a : b;
}

bool flows_from_to(cell** map, int from_h, int from_w, int to_h, int to_w) {
	int m = MAX;
	m = min(m, map[from_h-1][from_w].alt);
	m = min(m, map[from_h+1][from_w].alt);
	m = min(m, map[from_h][from_w-1].alt);
	m = min(m, map[from_h][from_w+1].alt);

	if (m >= map[from_h][from_w].alt) return false;

	if (map[from_h-1][from_w].alt == m) {
		if (to_h == from_h-1 && to_w == from_w)
			return true; else return false;
	}
	if (map[from_h][from_w-1].alt == m) {
		if (to_h == from_h && to_w == from_w-1)
			return true; else return false;
	}
	if (map[from_h][from_w+1].alt == m) {
		if (to_h == from_h && to_w == from_w+1)
			return true; else return false;
	}
	if (map[from_h+1][from_w].alt == m) {
		if (to_h == from_h+1 && to_w == from_w)
			return true; else return false;
	}
	cout << "no" << endl;
}

int H, W;

void flow_up(cell** map, int h, int w, int sink_id) {
	if (h<1 || h>H || w<1 || w>W)
		return;
	map[h][w].sink = true;
	map[h][w].num = sink_id;
	if (h-1 >= 1 && flows_from_to(map, h-1, w, h, w)) {
		flow_up(map, h-1, w, sink_id);
	}
	if (h+1 <= H && flows_from_to(map, h+1, w, h, w)) {
		flow_up(map, h+1, w, sink_id);
	}
	if (w-1 >= 1 && flows_from_to(map, h, w-1, h, w)) {
		flow_up(map, h, w-1, sink_id);
	}
	if (w+1 <= W && flows_from_to(map, h, w+1, h, w)) {
		flow_up(map, h, w+1, sink_id);
	}
}


int main() {

	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> H >> W;
		cell** map;
		map = new cell*[H+2];
		for (int j = 0; j < H+2; j++) {
			map[j] = new cell[W+2];
			map[j][0].alt = MAX;
			map[j][W+1].alt = MAX;
			for (int k = 1; k <= W; k++) {
				if (j==0 || j==H+1)
					map[j][k].alt = MAX;
				else
					cin >> map[j][k].alt;
			}
		}

		int sink_id = 0;
		for (int j = 0; j < H*W; j++) {
			if (is_sink(map, j/W+1, j%W+1)) {
				flow_up(map, j/W+1, j%W+1, sink_id);
				sink_id++;
			}
		}

		bool seen[26];
		for (int j=0; j<26; j++) seen[j]=false;
		int ch[26]; int cnt=0;
		cout << "Case #" << i << ":" << endl;
		for (int j = 1; j <= H; j++) {
			for (int k = 1; k<=W; k++) {
				if (!seen[map[j][k].num]) {
					seen[map[j][k].num]=true;
					ch[map[j][k].num] = cnt++;
				}
				cout << (char)(ch[map[j][k].num]+97) << " ";
			}
			cout << endl;
		}
		
	}


	return 0;

}
