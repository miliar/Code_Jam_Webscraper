#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <iostream>
#include <cmath>
#include <set>
#include <utility>

using namespace std;

int R;
set< pair<int,int> > conj[2];
int process() {
	conj[0].clear();
	conj[1].clear();
	
	scanf("%d", &R);
	int x1,y1,x2,y2;
	for (int i = 0 ; i < R ; i++) {
		scanf("%d%d%d%d", &x1,&y1,&x2,&y2);
		for (int x = x1 ; x <= x2 ; x++) {
			for (int y = y1 ; y <= y2 ; y++) {
				conj[0].insert( pair<int,int>(x,y));
			}
		}
	}
	
	pair<int,int> s;
	for (int t = 0; ; t++) {
		if (conj[t&1].empty()) {
			return t;
		}
		int a = t&1;
		int b = a?0:1;
		
		for (set< pair<int,int> >::iterator it = conj[a].begin() ; it != conj[a].end() ; it++) {
			s = *it;
			if (conj[a].find(pair<int,int>(s.first-1, s.second)) != conj[a].end() ||
			    conj[a].find(pair<int,int>(s.first, s.second-1)) != conj[a].end()) {
				conj[b].insert(s);
			}
			
			if (conj[a].find(pair<int,int>(s.first+1, s.second-1)) != conj[a].end()) {
				conj[b].insert(pair<int,int>(s.first+1, s.second));
			}
		}
		
		conj[a].clear();
	}
	
}

int main() {
	
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 0 ; i < T ; i++) {
		cerr << "calc " << i << endl;
		printf("Case #%d: %d\n", i+1, process());
	}
	
	return 0;
}
