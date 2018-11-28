#include <iostream>
using namespace std;

#define LARGE

#ifndef LARGE

const int GRID_SIZE = 100;

#else

const int GRID_SIZE = 10000;

#endif

int altitudes[GRID_SIZE];
char basin[GRID_SIZE];
int H, W;
char label;

void init () {
	label = 'a';
	for (int i = 0; i < W*H; i++) {
		basin[i] = '\0';
	}
}

int min_neigh(int i) {
	int j = i, min = altitudes[i];
	if (i >= W && altitudes[i-W] < min) {
		j = i - W;
		min = altitudes[j];
	}
	if (i % W > 0 && altitudes[i-1] < min) {
		j = i - 1;
		min = altitudes[j];
	}
	if (i % W < W - 1 && altitudes[i+1] < min) {
		j = i + 1;
		min = altitudes[j];
	}
	if (i < W*(H-1) && altitudes[i+W] < min) {
		j = i + W;
	}
	return j;
}

char flow(int i) {
	if (basin[i] == '\0') {
		int j = min_neigh(i);
		if (i == j) {
			basin[i] = label;
			label++;
		} else {
			basin[i] = flow(j);
		}
	}
	return basin[i];
}

void compute() {
	for (int i = 0; i < W*H; i++) {
		flow(i);
	}
}

int main() {
	cin.tie(NULL);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> H >> W;
		for (int j = 0; j < H*W; j++) {
			cin >> altitudes[j];
		}
		init();
		compute();
		cout << "Case #" << i + 1 << ":\n";
		for (int j = 0; j < H*W; j++) {
			cout << basin[j];
			if (j % W == W - 1) {
				cout << "\n";
			} else {
				cout << " ";
			}
		}
	}
	cout.flush();
	return 0;
}
