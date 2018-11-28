#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>
#include <map>
using namespace std;

const int N = 101;
int field[N][N];
int ans[N][N];
int w, h;

bool isSafe(int x, int y)
{
	return (0<=x && x<w && 0<=y && y<h);
}

const int dx[4] = { 0, -1, 1, 0 };
const int dy[4] = { -1, 0, 0, 1 };

int sinkNo(const int x, const int y)
{
	if (ans[y][x]!=0) return ans[y][x];

	const int val = field[y][x];

	int minI = -1;
	int minVal = INT_MAX;
	for (int i=0; i < 4; ++i) {
		if (isSafe(x+dx[i], y+dy[i])==false) continue;
		int v = field[y+dy[i]][x+dx[i]];
		if (field[y][x] <= v) continue;
		if (v < minVal) {
			minI = i;
			minVal = v;
		}
	}
	return ans[y][x] = sinkNo(x+dx[minI], y+dy[minI]);
}

bool isSink(int x, int y)
{
	for (int i=0; i < 4; ++i) {
		if (isSafe(x+dx[i], y+dy[i])==false) continue;
		if (field[y][x] > field[y+dy[i]][x+dx[i]]) return false;
	}
	return true;
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;
	for (int q=0; q < T; ++q) {
		in >> h >> w;
		for (int i=0; i < h; ++i) {
			for (int j=0; j < w; ++j) {
				in >> field[i][j];
			}
		}


		fill(&ans[0][0], &ans[N-1][N], 0);

		int sn = 0;
		for (int i=0; i < h; ++i) {
			for (int j=0; j < w; ++j) {
				if (isSink(j, i)) {
					ans[i][j] = ++sn;
				}
			}
		}

		for (int i=0; i < h; ++i) {
			for (int j=0; j < w; ++j) {
				if (ans[i][j]!=0) continue;
				ans[i][j] = sinkNo(j, i);
			}
		}

		map<int, char> conv;
		int t = 0;
		for (int i=0; i < h; ++i) {
			for (int j=0; j < w; ++j) {
				if (conv.find(ans[i][j])==conv.end()) {
					conv[ans[i][j]] = 'a'+t++;
				}
			}
		}

		out << "Case #" << q+1 << ":" << endl;
		for (int i=0; i < h; ++i) {
			for (int j=0; j < w; ++j) {
				if (j) out << " ";
				out << conv[ans[i][j]];
			}
			out << endl;
		}
	}

	in.close();
	out.close();

	return 0;
}
