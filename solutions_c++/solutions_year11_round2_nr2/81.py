#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <math.h>
using namespace std;

int T;

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		int C, D;
		scanf("%d %d", &C, &D);
		vector<pair<int,int> > ppos;
		for (int i = 0; i < C; i++) {
			int p, v;
			scanf("%d %d", &p, &v);
			ppos.push_back(make_pair(p, v));
		}
		sort(ppos.begin(), ppos.end());
		vector<int> pos;
		for (int i = 0; i < C; i++) {
			for (int k = 0; k < ppos[i].second; k++)
				pos.push_back(ppos[i].first);
		}
		long long ma = -1000000000000000000ll;
		long long mat = 0;
		for (int i = 0; i < (int)pos.size(); i++) {
			ma = max(ma, pos[i]-i*(long long)D);
			mat = max(mat, ma-pos[i]+i*(long long)D);
		}
		printf("%lf\n", mat*0.5);
	}
	return 0;
}
