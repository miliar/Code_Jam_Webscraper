#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
	
		int ans = 0;
		
		int N;
		vector <int> L, P;
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			int l;
			scanf("%d", &l);
			L.push_back(l);
		}
		for (int i = 0; i < N; i++) {
			int p;
			scanf("%d", &p);
			P.push_back(p);
		}
		
		vector < pair < pair <double, double>, int> > expected_time;
		for (int i = 0; i < N; i++) {
			expected_time.push_back(make_pair(
				make_pair( -100.0 / (100.0 - P[i]), -L[i]), i));
		}
		sort(expected_time.begin(), expected_time.end());
		
		printf("Case #%d: ", testcase);	
		for (int i = 0; i < N; i++) {
			printf("%d ", expected_time[i].second);
		}
		printf("\n");
	}

	return 0;
}