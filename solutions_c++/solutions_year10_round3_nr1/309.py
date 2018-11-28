#include <iostream>
#include <vector>
#include <map>
using namespace std;
int main() {
	int T, cs = 1;
	scanf("%d", &T);
	while(T--) {
		int N;
		vector<pair<int, int> > vp;
		scanf("%d", &N);
		for(int i = 0; i < N; ++i) {
			int u, v;
			scanf("%d%d", &u, &v);
			vp.push_back(make_pair(u, v));
		}
		sort(vp.begin(), vp.end());
		int count = 0;
		for(int i = 0; i < vp.size(); ++i) {
			for(int j = i + 1; j < vp.size(); ++j)
				if(vp[i].second > vp[j].second)
					++count;
		}
		printf("Case #%d: %d\n", cs, count);
		cs++;
	}
	return 0;
}
