#define _CRT_SECURE_NO_DEPRECATE

#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#include <map>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned char byte;
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

typedef pair<int, int> pii;

struct atom {
	int x, y;
	atom(int x = 0, int y = 0) : x(x), y(y) {}
	bool operator < (const atom &rhs) const {
		if (x != rhs.x) return (x < rhs.x);
		return (y < rhs.y);
	}
};

int main() {
	int t, c;
	int i, r, x, y, x1, y1, x2, y2;
	atom a;
	set<atom> s, qi, qe, q0, q1;
	set<atom>::iterator it, ito, itw, itn;
	
	scanf("%d", &c);
	for (t = 1; t <= c; t++) {
		s.clear();
		q0.clear();
		q1.clear();
		
		scanf("%d", &r);
		for (i = 0; i < r; i++) {
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (x = x1; x <= x2; x++) {
				for (y = y1; y <= y2; y++) {
					s.insert(atom(x, y));
					q0.insert(atom(x, y));
					q0.insert(atom(x + 1, y));
					q0.insert(atom(x, y + 1));				}
			}
		}
		
		for (r = 0; !s.empty(); r++) {
			qi.clear();
			qe.clear();
			q1.clear();
			for (it = q0.begin(); it != q0.end(); it++) {
				ito = s.find(atom(it->x, it->y));
				itw = s.find(atom(it->x - 1, it->y));
				itn = s.find(atom(it->x, it->y - 1));
				if (itw != s.end() && itn != s.end() && ito == s.end()) {
					qi.insert(atom(it->x, it->y));
					q1.insert(atom(it->x, it->y));
					q1.insert(atom(it->x + 1, it->y));
					q1.insert(atom(it->x, it->y + 1));
					continue;
				}
				if (itw == s.end() && itn == s.end() && ito != s.end()) {
					qe.insert(atom(it->x, it->y));
					q1.insert(atom(it->x, it->y));
					q1.insert(atom(it->x + 1, it->y));
					q1.insert(atom(it->x, it->y + 1));
					continue;
				}
			}
			for (it = qi.begin(); it != qi.end(); it++)
				s.insert(*it);
			for (it = qe.begin(); it != qe.end(); it++)
				s.erase(*it);
			q0.swap(q1);
		}
		
		printf("Case #%d: %d\n", t, r);
	}
	
	return (0);
} 
