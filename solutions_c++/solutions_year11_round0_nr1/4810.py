#include <algorithm>
#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;
typedef unsigned int uint;

int advance(int pos, int goal, int dist) {
	if (goal > pos) {
		if (pos + dist >= goal) return goal;
		else return pos+dist;
	} else if (goal < pos) {
		if (pos - dist <= goal) return goal;
		else return pos-dist;
	}
	else return pos;
}
int dist(int pos, int goal) {
	return abs(goal-pos);
}

int simulate(vector<int> &o, vector<int> &b, vector<pair<int, char> > &m) {
	int time=0;
	int bpos=1,opos=1;
	int bgoal=0,ogoal=0;
	for (uint i = 0; i < m.size(); i++) {
		pair<int, char> next = m[i];
		int distance=0;
		if (m[i].second == 'O' && ogoal < o.size())  
			 distance = dist(opos,o[ogoal]);
		else if (bgoal < b.size())
			 distance = dist(bpos,b[bgoal]);
		if (ogoal < o.size())
			opos = advance(opos,o[ogoal],distance);
		time += distance;
		time ++; // button press
		if (bgoal < b.size()) 
			bpos = advance(bpos,b[bgoal],distance);
		if (next.second == 'O') {
			if (bgoal < b.size()) 
				bpos = advance(bpos,b[bgoal],1);
			ogoal++;
		} else {
			if (ogoal < o.size())
				opos = advance(opos,o[ogoal],1);
			bgoal++;
		}

	}
	return time;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int m = 0; m < tc; m++) {
		int buttons;
		scanf("%d", &buttons);
		vector<int> o;
		vector<int> b;
		vector<pair<int, char> > master;
		for (int i = 0; i < buttons; i++) {
			char ch[1];
			int val;
			scanf("%s", ch);
			scanf("%d ", &val);
			if (ch[0] == 'O') o.push_back(val);
			else b.push_back(val);
			master.push_back(make_pair(val, ch[0]));
		}
		int res = simulate(o,b,master);
		printf("Case #%d: %d\n", m+1, res);
	}
	return 0;
}
