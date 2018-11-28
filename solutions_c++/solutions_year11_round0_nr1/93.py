#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

int cmp(int a, int b) {
	return (a < b) ? -1 : (a > b);
}

int main () {
	int T, t = 1;
	
	cin >> T;
	while (T--) {
		int n;
		
		cin >> n;
		
		vector < pair<char,int> > v(n);
		
		for (int i=0; i < n; ++i) {
			cin >> v[i].first >> v[i].second;
		}
		
		vector <int> nextb(n+1,1), nexto(n+1,1);
		
		for (int i=n-1; i >= 0; --i) {
			nextb[i] = nextb[i+1], nexto[i] = nexto[i+1];
			if (v[i].first == 'B') nextb[i] = v[i].second;
			else nexto[i] = v[i].second;
		}
		
		int posb = 1, poso = 1;
		int time = 0;
		
		for (int i=0; i < n; ++i) {
			if (v[i].first == 'B') {
				int inc = abs(v[i].second - posb) + 1;
				posb = v[i].second;
				poso += cmp(nexto[i],poso) * min(inc,abs(poso-nexto[i]));
				time += inc;
			}
			else {
				int inc = abs(v[i].second - poso) + 1;
				poso = v[i].second;
				posb += cmp(nextb[i],posb) * min(inc,abs(posb-nextb[i]));
				time += inc;
			}
		}
		
		printf("Case #%d: %d\n",t++,time);
	}
	
	return 0;
}
