#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <map>

#define min(a, b) ((a) > (b) ? (b) : (a))

using namespace std;


bool solveone() {
	int n, D, t;
	map<int, int> l, low;

	cin >> n;

	for(int i = 0; i < n; i++) { 
		cin >> t;
		cin >> l[t];
	}

	cin >> D;

	l[D] = D;

	low[(*(l.begin())).first] = (*(l.begin())).first;
	
	for(map<int, int> :: iterator current = l.begin(); current != l.end(); current++) {
		for(map<int, int> :: iterator next = current; next != l.end() && low[(*current).first] >= ((*next).first - (*current).first); next++) {
			int ln = min(((*next).first - (*current).first), (*next).second);
			if(ln <= (*next).second && ln > low[(*next).first])
				low[(*next).first] = ln;
		}
	}

	return low[D] != 0;
}

int main() {
	int t, i;	
	cin >> t;
	for(int i = 1; i <= t; i++)
		printf("Case #%d: %s\n", i, solveone() ? "YES" : "NO");
}