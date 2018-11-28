#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <sstream>
#include <cassert>

using namespace std;

void solve(int t);

inline void openFiles() {
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
}

void pr(int t) {
	std::cout << t << "\n";
}

int main() {
#ifndef ONLINE_JUDGE
	openFiles();
#endif
	int t; scanf("%d\n", &t);
	for (int i = 0; i < t; ++i)
		solve(i + 1);
	return 0;
}

struct Point {
	int hour; 
	int min;
	bool fromA;
	bool arrive; 
	bool operator<(const Point& p) const {
		if (hour != p.hour)
			return this->hour < p.hour;
		if (this->min != p.min)
			return this->min < p.min;
		return arrive > p.arrive;
	}
	void add(int t) {
		min += t;
		while (min >= 60) {
			min -= 60;
			hour += 1;
		}
	}
};

void solve(int t) {
	int time; scanf("%d\n", &time);
	int na, nb; scanf("%d %d\n", &na, &nb);
	std::multiset<Point> s; int reta = 0, retb = 0;
	for (int i = 0; i < na; ++i) {
		int a, b, c, d; scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
		Point p; p.arrive = false; p.fromA = true; p.hour = a; p.min = b;
		s.insert(p);
		p.arrive = true; p.fromA = true; p.hour = c; p.min = d;
		p.add(time);
		s.insert(p);
	}
	for (int i = 0; i < nb; ++i) {
		int a, b, c, d; scanf("%d:%d %d:%d\n", &a, &b, &c, &d);
		Point p; p.arrive = false; p.fromA = false; p.hour = a; p.min = b;
		s.insert(p);
		p.arrive = true; p.fromA = false; p.hour = c; p.min = d;
		p.add(time);
		s.insert(p);			
	}
	int ina = 0, inb = 0;
	for (std::set<Point>::iterator it = s.begin(); it != s.end(); ++it) {
		if (it->arrive) {
			if (it->fromA) ++inb;
			else ++ina;				
			continue;
		}
		if (it->fromA) {
			if (ina == 0) reta += 1;
			else ina -= 1;
		} else {
			if (inb == 0) retb += 1;
			else inb -= 1;
		}
	}
	printf("Case #%d: %d %d\n", t, reta, retb);
}
