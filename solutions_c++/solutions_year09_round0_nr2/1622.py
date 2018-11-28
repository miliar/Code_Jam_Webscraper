#include <iostream>
#include <queue>
#include <map>

using namespace std;
#define FIELD_MAX 110

int field[FIELD_MAX][FIELD_MAX];
int ofield[FIELD_MAX][FIELD_MAX];
int h, w;

typedef pair<int, int> Point;

struct Alpha {
	map<int, char> m;
	char index;
	Alpha(){
		index = 'a';
	}
	char request(int i){
		if(m.find(i) == m.end()){
			m[i] = index;
			index++;
		}
		return m[i];
	}
};

struct Marker {
	int score;
	Point p;
	bool operator > (const Marker &a) const {
		return score > a.score;
	}
};

int tbl[][2] = {
	{0, 1},
	{1, 0},
	{-1, 0},
	{0, -1},
};

pair<bool, Point> lowest(int x, int y) {
	int min = field[y][x];
	Point p;
	for(int i = 0; i < 4; i++){
		int tx = tbl[i][0] + x;
		int ty = tbl[i][1] + y;
		if(tx >= 0 && ty >= 0 && tx < w && ty < h){
			if(min >= field[ty][tx]){
				min = field[ty][tx];
				p = make_pair(tx, ty);
			}
		}
	}
	if(min == field[y][x]){
		return make_pair(false, p);
	} else {
		return make_pair(true, p);
	}
}

void mark(int x, int y, int val){
	ofield[y][x] = val;
	for(int i = 0; i < 4; i++){
		int tx = tbl[i][0] + x;
		int ty = tbl[i][1] + y;
		if(tx >= 0 && ty >= 0 && tx < w && ty < h){
			pair<bool, Point> ret = lowest(tx, ty);
			if(ret.first && ret.second == make_pair(x, y) && ofield[ty][tx] == -1){
				mark(tx, ty, val);
			}
		}
	}
	
}

void dumpOfield(){
	Alpha al;
	
	for(int i = 0; i < h; i++){
		for(int l = 0; l < w; l++){
			cout << al.request(ofield[i][l]);
			if(l < w - 1) cout << " ";
		}
		cout << endl;
	}
}

int main(){
	int t;
	cin >> t;
	for(int k = 0; k < t; k++){
		priority_queue<Marker, deque<Marker>, greater<Marker> > markers;
		fill_n(field[0], FIELD_MAX * FIELD_MAX, 0);
		fill_n(ofield[0], FIELD_MAX * FIELD_MAX, -1);

		cin >> h >> w;
		for(int i = 0; i < h; i++){
			for(int l = 0; l < w; l++){
				int s;
				cin >> s;
				field[i][l] = s;
				
				Marker m;
				m.score = s;
				m.p.first = l;
				m.p.second = i;
				markers.push(m);
			}
		}

		int i = 0;
		while(!markers.empty()){
			Marker m = markers.top();
			markers.pop();
			if(ofield[m.p.second][m.p.first] == -1){
				mark(m.p.first, m.p.second, i);
			}
			i++;
		}

		cout << "Case #" << (k + 1) << ":" << endl;
		dumpOfield();
	}
}
