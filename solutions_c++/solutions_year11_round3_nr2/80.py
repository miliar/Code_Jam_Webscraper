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
#include <tr1/unordered_set>
#include <tr1/unordered_map>
#include <gmpxx.h>

using namespace std;
using namespace tr1;

typedef mpz_class number;

struct Gap {
	int index;
	int A, B; // total time = A*v + B
	Gap(int a, int b, int i) {
		index = i;
		A = a, B = b;
	}
	bool operator <(const Gap &G) const {
		if (A != G.A) return A > G.A;
		return index < G.index;
	}
};

int main () {
	int T, tt = 1;
	
	cin >> T;
	while (T--) {
		int L, N, C;
		long long t;
		
		vector < pair <int,int> > dists; // dist, number of times used
		
		cin >> L >> t >> N >> C;
		
		for (int i=0; i < C; i++) {
			int a;
			cin >> a;
			dists.push_back(make_pair(a,N / C + (i < N % C)));
		}
		
		long long time = 0;
		int pos = 0;
		
		for ( ; pos < N && time+2*dists[pos%C].first <= t; pos++) {
			time += 2 * dists[pos%C].first;
		}
		
		vector <Gap> v;
		
		if (pos < N) {
			int slow = (t - time) / 2;
			v.push_back(Gap( dists[pos%C].first - slow, slow, pos ));
		}
		
		for (int i=pos+1; i < N; i++) {
			v.push_back(Gap( dists[i%C].first, 0, i ));
		}
		
		sort(v.begin(), v.end());
		
		for (int i=0; i < v.size(); i++) {
			if (L-- > 0) {
				time += v[i].A + v[i].B * 2;
			}
			else {
				time += v[i].A * 2 + v[i].B * 2;
			}
		}
		
		printf("Case #%d: %lld\n", tt++, time);
	}
	
	return 0;
}
