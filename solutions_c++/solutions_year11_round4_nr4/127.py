#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

#define PLANETS 36

int p, w;
vector<int> pov[PLANETS];

struct stanje {
	int p, z, pos;
	bool zaseda[PLANETS];
	
	stanje() {
		pos = 0;
		p = 0;
		z = 0;
		memset(zaseda, 0, sizeof zaseda);
	}
	
	stanje(stanje &s, int next) {
		p = s.p + 1;
		pos = next;
		memcpy(zaseda, s.zaseda, PLANETS * sizeof(bool));
		z = s.z;
		
		for (int i = 0; i < pov[pos].size(); i++)
			if (!zaseda[pov[pos][i]]) {
				zaseda[pov[pos][i]] = true;
				z++;
				//cout << "a" << endl;
			}
	}
	
	bool operator<(const stanje r) const {
		if (p > r.p) return true;
		if (p < r.p) return false;
		return z > r.z;
	}
};

bool visited[PLANETS];

void task() {
	for (int i = 0; i < PLANETS; i++)
		pov[i].clear();

	//read
	scanf("%d%d", &p, &w);
	for (int i = 0; i < w; i++) {
		int a, b;
		scanf("%d,%d", &a, &b);
		if (b != 0 && a != 1) pov[a].push_back(b);
		swap(a, b);
		if (b != 0 && a != 1) pov[a].push_back(b);
	}
	
	memset(visited, 0, sizeof visited);
		
	//solve
	
	priority_queue<stanje> vrsta;
	
	stanje empty = stanje();
	vrsta.push(stanje(empty, 0));
	
	int best_p = -1, best_z = -1;
	
	while (!vrsta.empty()) {
		stanje t = vrsta.top();	vrsta.pop();
		
		//cout << t.p << endl;
		
		if (t.pos == 1) {
			if (best_p == -1) {
				best_p = t.p;
			}
			if (best_p == t.p) {
				best_z = max(best_z, t.z);
			}
			if (t.p > best_p)
				break;
		}
		
		visited[t.pos] = true;
		
		for (int i = 0; i < pov[t.pos].size(); i++) {
			if (!visited[pov[t.pos][i]])
			vrsta.push(stanje(t, pov[t.pos][i]));
		}
	}
	
	
	cout << best_p - 2 << " " << best_z - (best_p - 2) << endl;	
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		//printf("%d\n", task());
		task();
	}
}

