#include <algorithm>
#include <cstdio>
#include <utility>
#include <vector>
using namespace std;

int time_to_int(int h, int m) {
	return h*60+m;
}

typedef pair<int, int> pii;

int calc_required(vector<pii>& A) {
	int count = 0, waiting = 0;
	for (vector<pii>::iterator i=A.begin(); i!=A.end(); i++) {
		if (i->second == +1) {		//odjazd
			if (waiting) waiting--;
			else count++;
		} else waiting++;			//przyjazd
	}
	return count;
}

int main() {
	int N;
	scanf("%d", &N);
	for (int n=1; n<=N; n++) {
		int T, NA, NB;
		scanf("%d%d%d", &T, &NA, &NB);
		vector<pii> A, B;
		for (int i=0; i<NA; i++) {
			int h, m;
			scanf("%d:%d", &h, &m);
			A.push_back(make_pair(time_to_int(h, m), +1));
			scanf("%d:%d", &h, &m);
			B.push_back(make_pair(time_to_int(h, m)+T, -1));
		}
		for (int i=0; i<NB; i++) {
			int h, m;
			scanf("%d:%d", &h, &m);
			B.push_back(make_pair(time_to_int(h, m), +1));
			scanf("%d:%d", &h, &m);
			A.push_back(make_pair(time_to_int(h, m)+T, -1));
		}
		sort(A.begin(), A.end());
		sort(B.begin(), B.end());

		printf("Case #%d: %d %d\n", n, calc_required(A), calc_required(B));
	}
	return 0;
}