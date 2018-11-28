#include <iostream>
#include <list>
#include <set>
#include <string>
#include <assert.h>
#include <vector>

#define _CRT_SECURE_NO_WARNINGS

#define For(v, m, n) for(int v = m; v < n; ++v)
#define InOut(name) freopen("..\\" ##  #name ## ".in","r", stdin); \
	freopen("..\\" ##  # name  ## ".out", "w", stdout);
#define In(name) freopen("..\\" ##  #name ## ".in","r", stdin);
#define MAX(a, b) ((a)>(b))?(a):(b)
#define MIN(a, b) ((a)<(b))?(a):(b)
#define INF 100000

using namespace std;
char recur(char next_char, int x, int y, vector<vector<int>> map, char **cmap, int height, int width);
int main() {
	InOut(B-large);
	int n;
	cin>>n;
	For(i, 0, n) {
		int width, height;
		cin>>height>>width;
		vector<vector<int>> map;
		char **cmap = new char*[height];
		int max = 0;
		int tmp;
		set<int> altitudes;
		For(h, 0, height) {
			map.push_back(*(new vector<int>));
			cmap[h] = new char[width];
			For(w, 0, width) {
				cin>>tmp;
				map[h].push_back(tmp);
				cmap[h][w] = 0;
				if (tmp > max) 
					max = tmp;
			}
		}
		char next_char = 'a';
		for(int y = 0; y<height; ++y) {
			for(int x = 0; x<width; ++x) {
				if (next_char == recur(next_char,x, y, map, cmap, height, width)) 
					next_char++;
			}
		}
		cout<<"Case #"<<i+1<<":"<<endl;
		for(int y = 0; y<height; ++y) {
			for(int x = 0; x<width; ++x) {
				cout<<cmap[y][x]<<" ";
			}
			cout<<endl;
		}
	}
	return 0;
}

char recur(char next_char, int x, int y, vector<vector<int>> map, char **cmap, int height, int width) {
	if (cmap[y][x] != 0) {
		return cmap[y][x];
	} else {
		int north, west, east, south;
		if (!(y-1>-1) || !(x<width)) {
			north = INF;
		} else {
			north = map.at(y-1).at(x);
		}
		if (!(y<height) ||!(x-1 >-1)) {
			west = INF;
		} else {
			west = map.at(y).at(x-1);
		}
		if (!(y<height) || !(x+1 <width)) {
			east = INF;
		} else {
			east = map.at(y).at(x+1);
		}
		if (!(y+1<height) || !(x<width)) {
			south = INF;
		} else {
			south = map.at(y+1).at(x);
		}
		int min = MIN(MIN(north, east),MIN(south, west));
		if (min < map[y][x]) {
			if (min == north) {
				return (cmap[y][x] = recur(next_char, x, y-1, map, cmap, height, width));
			} else if (min == west) {
				return (cmap[y][x] = recur(next_char, x-1, y, map, cmap, height, width));
			} else if (min == east) {
				return (cmap[y][x] = recur(next_char, x+1, y, map, cmap, height, width));
			} else if (min == south) {
				return (cmap[y][x] = recur(next_char, x, y+1, map, cmap, height, width));
			}
		} else {
			return(cmap[y][x] = next_char);
		}
	}
}