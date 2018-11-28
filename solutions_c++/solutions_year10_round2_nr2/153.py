#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <string>
#include <map>

using namespace std;

struct Ele {
	int pos, velo;
	
	bool operator <(const Ele& e) const {
		if (pos < e.pos) {
			return true;
		} else if (pos == e.pos) {
			return velo > e.velo;
		} else {
			return false;
		}
	}
};

int N, K, B, T;
Ele ele[210];

void read() {
	scanf("%d%d%d%d", &N, &K, &B, &T);
	
	for (int i = 0; i < N; i++) {
		scanf("%d", &ele[i].pos);
	}
	
	for (int i = 0; i < N; i++) {
		scanf("%d", &ele[i].velo);
	}
}

void process() {
	sort(ele, ele+N);
	
	int qtdSim;
	long long tot;
	for (int i = 0; i < N; i++) {
	
		qtdSim = 0;
		tot = 0;
		for (int j = i; j < N; j++) {
			if (ele[j].pos+ele[j].velo*T >= B) {
				qtdSim++;
			} else {
				tot += qtdSim;
			}
		}
		
		if (qtdSim == K) {
			break;
		}
	}
	
	if (qtdSim < K) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%lld\n", tot);
	}
}

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int casos;
	scanf("%d", &casos);
	
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}

