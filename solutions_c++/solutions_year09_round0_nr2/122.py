#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

int t;
int h;
int w;

int grid[100][100];
char marked[100][100];

int queue[10000][2];
int top;
int bottom;

fstream in, out;

bool isbasin(int aa, int bb) {
	if (aa > 0 && grid[aa-1][bb] < grid[aa][bb]) {
		return false;
	}

	if (aa < h - 1 && grid[aa+1][bb] < grid[aa][bb]) {
		return false;
	}

	if (bb > 0 && grid[aa][bb-1] < grid[aa][bb]) {
		return false;
	}

	if (bb < w - 1 && grid[aa][bb+1] < grid[aa][bb]) {
		return false;
	}

	return true;
}

int flow(int aa, int bb) {
	int vals[4];
	vals[0] = 100010;
	vals[1] = 100010;
	vals[2] = 100010;
	vals[3] = 100010;

	if (aa > 0) {
		vals[0] = grid[aa-1][bb];
	}

	if (aa < h - 1) {
		vals[3] = grid[aa+1][bb] ;
	}

	if (bb > 0) {
		vals[1] =  grid[aa][bb-1];
	}

	if (bb < w - 1) {
		vals[2] = grid[aa][bb+1];
	}

	int ret = 0;
	for (int i = 1; i < 4; i++) {
		if (vals[i] < vals[ret]) {
			ret = i;
		}
	}
	if (vals[ret] < grid[aa][bb]) {
		return ret;
	} else {
		return -1;
	}
}

void flood(int a, int b, char marker) {
	top = 0;
	bottom = 1;
	queue[0][0] = a;
	queue[0][1] = b;

	while (top != bottom) {
		int aa = queue[top][0];
		int bb = queue[top][1];
		top++;

		if (marked[aa][bb] == '1') {
			marked[aa][bb] = marker;
			if (aa > 0 && flow(aa-1, bb) == 3 && marked[aa-1][bb] == '1') {
				queue[bottom][0] = aa - 1;
				queue[bottom][1] = bb;
				bottom++;
			}

			if (aa < h - 1 && flow(aa+1, bb) == 0  && marked[aa+1][bb] == '1') {
				queue[bottom][0] = aa + 1;
				queue[bottom][1] = bb;
				bottom++;
			}

			if (bb > 0 && flow(aa, bb-1) == 2  && marked[aa][bb-1] == '1') {
				queue[bottom][0] = aa;
				queue[bottom][1] = bb - 1;
				bottom++;
			}

			if (bb < w - 1 && flow(aa, bb+1)== 1  && marked[aa][bb+1] == '1') {
				queue[bottom][0] = aa;
				queue[bottom][1] = bb + 1;
				bottom++;
			}
		}
	}
}

void swap(char upper, char lower) {
	for (int x = 0; x < h; x++) {
		for (int y = 0; y < w; y++) {
			if (marked[x][y] == upper) {
				marked[x][y] = lower;
			}
		}
	}
}

int main() {
	in.open("prob2.in", fstream::in);
	out.open("prob2.out", fstream::out);

	in >> t;

	for (int i = 0; i < t; i++) {
		in >> h >> w;
		for (int a = 0; a < h; a++) {
			for (int b = 0; b < w; b++) {
				in >> grid[a][b];
				marked[a][b] = '1';
			}
		}

		char marker = 'A';

		for (int aa = 0; aa < h; aa++) {
			for (int bb = 0; bb < w; bb++) {
				if (isbasin(aa, bb)) {
					flood(aa, bb, marker);
					marker++;
				}
			}
		}

		char lower = 'a';
		for (int x = 0; x < h; x++) {
			for (int y = 0; y < w; y++) {
				if (marked[x][y] >= 'A' && marked[x][y] <= 'Z') {
					swap(marked[x][y], lower);
					lower++;
				}
			}
		}

		out << "Case #" << i + 1 << ":" << endl;
		for (int aaa = 0; aaa < h; aaa++) {
			for (int bbb = 0; bbb < w; bbb++) {
				out << marked[aaa][bbb];
				if (bbb < w - 1) {
					out << " ";
				}
			}
			out << endl;
		} 
		
	}

	in.close();
	out.close();

	return 0;
}
