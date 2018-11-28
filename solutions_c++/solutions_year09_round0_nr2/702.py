#include <iostream>
#include <cstring>
#include <algorithm>
#include <string>
#include <iomanip>
#include <vector>
#include <fstream>
#include <map>
#include <cstdio>
#include <stack>
using namespace std;

int T, W, H;

ifstream in("in.txt");
ofstream out("out.txt");

struct Node {
	int h;
	vector<pair<int, int> > dir;
} mapp[101][101];

vector<pair<int, int> > sink;

#define MAX 100000

int off[4][2] = {-1,0, 0,-1, 0,1, 1,0};
int edge[101][101];

bool check(int w, int h) {
	if(w >= 0 && w < W && h >= 0 && h < H)
		return true;
	return false;
}

int main() {
	in >> T;
	int TT = 1;
	for(int v = 0; v < T; ++v) {
		in >> W >> H;
		for(int i = 0; i < W; ++i) {
			for(int j = 0; j < H; ++j) {
				in >> mapp[i][j].h;
				mapp[i][j].dir.clear();
			}
		}
		sink.clear();

		for(int i = 0; i < W; ++i) {
			for(int j = 0; j < H; ++j) {
				int H = MAX, x, y;
				for(int k = 0; k < 4; ++k) {
					int xx = i + off[k][0], yy = j + off[k][1];
					if(check(xx, yy) && mapp[xx][yy].h < H) {
						H = mapp[xx][yy].h;
						x = xx;
						y = yy;
					}
				}
				if(H < mapp[i][j].h) {
					mapp[x][y].dir.push_back(pair<int, int>(i,j));
				} else {
					sink.push_back(pair<int, int>(i,j));
				}
			}
		}

		memset(edge, 0, sizeof(edge));

		for(int i = 0; i < sink.size(); ++i) {
			int group = i + 1;
			stack<pair<int, int> > tp;
			tp.push(sink[i]);
			while(!tp.empty()) {
				pair<int, int> pr = tp.top();
				tp.pop();
				edge[pr.first][pr.second] = group;
				for(int j = 0; j < mapp[pr.first][pr.second].dir.size(); ++j) {
					tp.push(mapp[pr.first][pr.second].dir[j]);
				}
			}
		}
		map<int, char> maps;
		map<int, char>::iterator itr;
		char ch = 'a';
		for(int i = 0; i < W; ++i) {
			for(int j = 0; j < H; ++j) {
				itr = maps.find(edge[i][j]);
				if(itr == maps.end()) {
					maps[edge[i][j]] = ch;
					++ch;
				}
			}
		}

		out << "Case #" << TT << ":" << endl;
		for(int i = 0; i < W; ++i) {
			for(int j = 0; j < H; ++j) {
				out << maps[edge[i][j]];
				if(j < H - 1) {
					out << " ";
				} else {
					out << endl;
				}
			}
		}
		++TT;

	}
	return 0;
}