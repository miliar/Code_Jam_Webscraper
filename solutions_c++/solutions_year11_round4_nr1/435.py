#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define REP(i, n) for (int i(0), _n(n); i!=_n; ++i)
#define CL(v, x) memset((v), (x), sizeof(v))
#define SZ(v) (int)((v).size())

// Definition goes here
vector<pair<int, int> > roads; 
const double eps = 1e-9;

int main() {
	int T;
	scanf("%d", &T);
	
	REP(tc, T) {
		// add code here
		
		int x, s, r, t, n;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		roads.clear();
		REP(i, n) {
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			roads.push_back(make_pair(w, e - b));
			x -= e - b;
		}
		if (x > 0) roads.push_back(make_pair(0, x));
		sort(roads.begin(), roads.end());
		
//			REP(i, SZ(roads)) printf("%d %d\n", roads[i].first, roads[i].second);
		
		double cur = t, ret = 0;
		REP(i, SZ(roads)) {
			double need = double(roads[i].second) / (roads[i].first + s);
			
			if (cur < eps) ret += need;
			else {
				double faster = double(roads[i].second) / (roads[i].first + r);
				if (faster < cur + eps) {
					ret += faster;
					cur -= faster;
				}
				else {
					ret += cur + double(roads[i].second - (roads[i].first + r) * cur) / (roads[i].first + s);
					cur = 0;
				}
			}
		}
		
		printf("Case #%d: %.8lf\n", tc + 1, ret);
		// printf solution here
		
	}
	
	return 0;
}