#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

int read_time() {
	int h, m;
	scanf(" %d:%d", &h, &m);
	return h * 60 + m;
}

struct event {
	int time, st;
	int type; // 0 --- arrival, 1 -- departure
	event(int _time, int _st, int _type) : time(_time), st(_st), type(_type) { }
	
	bool operator < (const event& ev) const {
		if(time != ev.time) return time < ev.time;
		if(type != ev.type) return type < ev.type;
		return st < ev.st;
	}
};

std::multiset<event> evs;
int avail[2], req[2];

int main() {
	int t = 1, tc, i, j, n[2], dt, st, nd;
	for(scanf("%d", &tc); t <= tc; t++) {
		scanf("%d", &dt);
		scanf("%d%d", n+0, n+1);
		evs.clear();
		for(j = 0; j < 2; j++)
			for(i = 0; i < n[j]; i++) {
				st = read_time();
				nd = read_time();
				evs.insert(event(st, j, 1));
				evs.insert(event(nd+dt, 1-j, 0));
			}
		for(j = 0; j < 2; j++) avail[j] = req[j] = 0;
		while(!evs.empty()) {
			event ev = *evs.begin();
			evs.erase(evs.begin());
			if(ev.type == 0) {
				avail[ev.st]++;
				continue;
			}
			if(avail[ev.st] > 0) avail[ev.st]--;
			else req[ev.st]++;
		}
		printf("Case #%d: %d %d\n", t, req[0], req[1]);
	}
	return 0;
}
