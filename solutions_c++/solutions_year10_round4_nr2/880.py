#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

#define TRACE(x) 
#define PRINT(x...) TRACE(printf(x))

int heap[(1<<12)];
int mark[(1<<12)];
int M[(1<<12)];

int teams;
int P;

vector< pair<int, pair<int,int> > > tickets(int idx) {
	idx += teams - 1;
	vector< pair<int, pair<int,int> > > v;

	do {
		idx = (idx-1) / 2;
		v.push_back( make_pair( mark[idx], make_pair(heap[idx], idx) ) );
	} while (idx > 0);

	sort(v.begin(), v.end());
	return v;
}

int main() {
	int T, _42=0;
	scanf(" %d", &T);
	while (T--) {
		memset(mark, 0, sizeof(mark));
		long long ans = 0;

		scanf(" %d", &P);
		
		teams = 1 << P;
		for (int i=0; i < teams; i++) scanf(" %d", &M[i]);

		int tmp = teams / 2;
		while (tmp > 0) {
			//int pos = (1 << (tmp / 2)) - 1;
			int pos = tmp - 1;
			for (int i=0; i < tmp; i++) scanf(" %d", &heap[i+pos]);
			tmp /= 2;
		}
TRACE(
		for (int i=0; i+1 < (1 << P); i++) printf("%d ", heap[i]); printf("\n");
)

		vector< pair<int,int> > vm;
		for (int i=0; i < teams; i++) {
			vm.push_back( make_pair( M[i], i ) );
		}
		sort(vm.begin(), vm.end());

		for (int i=0; i < (int)vm.size(); i++) {
			PRINT("vm[i]: <%d,%d>\n", vm[i].first, vm[i].second);
			vector< pair<int, pair<int,int> > > v = tickets(vm[i].second);
			int faltam = P - vm[i].first;
			for (int j=0; j < (int)v.size(); j++) {
				if (!faltam) break;
				PRINT("v[j]: <%d,<%d,%d>>\n", v[j].first, v[j].second.first, v[j].second.second);
				if (!v[j].first) {
					mark[ v[j].second.second ] = -1;
					ans += v[j].second.first;
					PRINT("comprei ticket: %d\n", v[j].second.first);
				}
				faltam--;
			}
		}

		printf("Case #%d: %lld\n", ++_42, ans);
	}
	return 0;
}
