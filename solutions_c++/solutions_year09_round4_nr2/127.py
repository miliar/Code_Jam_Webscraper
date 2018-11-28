#include <iostream>
#include <string>
#include <queue>
#include <map>

using namespace std;

#define MAX 60

struct maze {
	string sq;
};

struct state {
	maze smz;
	int x, y;
	int digs;
};

bool operator< (const state & s1, const state & s2) {
	if (s1.digs < s2.digs) return false;
	if (s1.digs > s2.digs) return true;
	return true;
}

int r, c, f;

bool isempty(maze & m, int x, int y) {
	if (x < 0 || x >= c || y < 0 || y >= r) return false;
	return m.sq[(y * c + x)] == '.';
}

string print_maze(state & s) {
	string ss;
	for (int  i = 0; i < r; i++){
		for (int j = 0; j < c; j++) {
			if (s.x == j && s.y == i) ss += 'X';
			else ss += s.smz.sq[i * c + j];
		}
		ss += '\n';
	}
	return ss;
}

void dig(maze & m, int x, int y) {
	m.sq[(y * c + x)] = '.';
}

bool fall(state & s) {
	int fs = 0;
	while (isempty(s.smz, s.x, s.y + 1)) {
		s.y++;
		fs++;
	}
	if (fs > f) return false;
	return true;
}


void solve() {
	cin >> r >> c >> f;

	map<string, bool> visited;

	maze mz; 
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++) {
			char s; cin >> s;
			mz.sq += s;
		}

	priority_queue<state> pq;
	state is; is.x = 0; is.y = 0; is.digs = 0; is.smz = mz;
	if (fall(is)) pq.push(is);

	while (!pq.empty()) {
		state cs; cs = pq.top(); pq.pop();
	
		string sth = print_maze(cs);
		if (visited.find(sth) != visited.end()) continue;
		visited[sth] = true;
	
		if (cs.y == r - 1) {cout << "Yes " << cs.digs << endl; return;}

		// go right
		if (isempty(cs.smz, cs.x + 1, cs.y)) {
			state ns; ns = cs;
			ns.x++;
			if (fall(ns)) pq.push(ns);	
		}

		// go left
		if (isempty(cs.smz, cs.x - 1, cs.y)) {
			state ns; ns = cs;
			ns.x--;
			if (fall(ns)) pq.push(ns);	
		}

		// dig right
		if (isempty(cs.smz, cs.x + 1, cs.y) && !isempty(cs.smz, cs.x + 1, cs.y + 1)) {
			state ns; ns = cs;
			ns.digs++; dig(ns.smz, ns.x + 1, ns.y + 1);
			pq.push(ns);
		}

		// dig left
		if (isempty(cs.smz, cs.x - 1, cs.y) && !isempty(cs.smz, cs.x - 1, cs.y + 1)) {
			state ns; ns = cs;
			ns.digs++; dig(ns.smz, ns.x - 1, ns.y + 1);
			pq.push(ns);
		}

	}
	
	cout << "No" << endl;
}

int main() {
	int t; cin >> t;

	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": "; solve(); 
	}
	return 0;
}
