#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

struct node {
	struct node* sink; int alt; char label;
	node() : sink(0), alt(10000), label(0) {};
};

node* readMap(int h, int w) {
	string line;
	node* map = new node[(h + 2) * (w + 2)];
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) 
			cin >> map[i * (w + 2) + j].alt;
		getline(cin, line);
	}
	return map;
}

void solveMap(node *map, int h, int w) {
	vector<int> stack = vector<int>();
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			int ptr = i * (w + 2) + j;
			while (!map[ptr].sink) {
				int min_alt = min(min(map[ptr - 1].alt, map[ptr + 1].alt), min(map[ptr - w - 2].alt, map[ptr + w + 2].alt));
				if (min_alt >= map[ptr].alt) {
					map[ptr].sink = map + ptr;
				} else {
					stack.push_back(ptr);
					if (min_alt == map[ptr - w - 2].alt) {
						ptr = ptr - w - 2;
					} else if (min_alt == map[ptr - 1].alt) {
						ptr = ptr - 1;
					} else if (min_alt == map[ptr + 1].alt) {
						ptr = ptr + 1;
					} else if (min_alt == map[ptr + w + 2].alt) {
						ptr = ptr + w + 2;
					}
				}
			}
			node *sink_node = map[ptr].sink;
			while (!stack.empty()) {
				map[stack.back()].sink = sink_node;
				stack.pop_back();
			}
		}
	}
}

void printMap(node *map, int h, int w) {
	char next_label = 'a';
	for (int i = 1; i <= h; i++) {
		for (int j = 1; j <= w; j++) {
			int ptr = i * (w + 2) + j;
			if (!map[ptr].sink->label) {
				map[ptr].sink->label = next_label++;
			}
			cout << map[ptr].sink->label;
			if (j != w) cout << " ";
		}
		::cout << endl;
	}
}

int main (int argc, char * const argv[]) {
	string line;
	int T;

	::cin >> T;
	getline(::cin, line);

	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ":" << endl;
		int H, W;
		cin >> H >> W;
		getline(cin, line);
		node* map = readMap(H, W);
		solveMap(map, H, W);
		printMap(map, H, W);
		delete [] map;
	}
    return 0;
}
