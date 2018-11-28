#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;

void printList(vector<int>& v) {
  for (size_t i = 0; i < v.size(); i++) {
	cout << v[i] << " ";
  }
  cout << endl;
}

void printArray(vector< vector<int> >& v) {
  for (size_t i = 0; i < v.size(); i++) {
	printList(v[i]);
  }
  cout << endl;
}

char blue = '#';
char white = '.';
char slash = '/';
char bsla = '\\';

inline bool check(size_t i, size_t j, size_t R, size_t C,
				  vector<string>& tiles) {
  return  i + 1 < R && j + 1 < C && 
	tiles[i][j] == blue && tiles[i][j+1] == blue &&
	tiles[i+1][j] == blue && tiles[i+1][j+1];
}

bool solve(vector<string>& tiles) {
  size_t R = tiles.size();
  size_t C = tiles[0].size();
  for (size_t i = 0; i < R; i++) {
	for (size_t j = 0; j < C; j++) {
	  if (tiles[i][j] != blue) continue;
	  if (!check(i, j, R, C, tiles)) return false;
	  tiles[i][j] = slash;
	  tiles[i][j+1] = bsla;
	  tiles[i+1][j] = bsla;
	  tiles[i+1][j+1] = slash;
	}
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
	int R, C;
	cin >> R >> C;
	vector<string> tiles;
	for (int j = 0; j < R; j++) {
	  string s;
	  cin >> s;
	  tiles.push_back(s);
	}
	bool ans = solve(tiles);
	cout << "Case #" << i + 1 << ":" << endl;
	if (ans) {
	  for (size_t i = 0; i < tiles.size(); i++) {
		cout << tiles[i] << endl;
	  }
	} else {
	  cout << "Impossible" << endl;
	}
  }
  return 0;
}
