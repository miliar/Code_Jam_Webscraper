#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
	
		int ans = 0;
		
		int N, W, L;
		scanf("%d %d %d", &N, &W, &L);
		vector < int > R, idx, idx2;
		
		R.clear();		
		idx.clear();
		
		for (int i = 0; i < N; i++) {
			int tmp;
			scanf("%d", &tmp);
			R.push_back(tmp);
			idx.push_back(i);
			idx2.push_back(i);
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				if (R[i] < R[j]) {
					int t = R[i];
					R[i] = R[j];
					R[j] = t;
					t = idx[i];
					idx[i] = idx[j];
					idx[j] = t;
				}
			}
		}
		for (int i = 0; i < N; i++) {
			idx2[idx[i]] = i;
		}
		
		vector < double > X, Y;
		priority_queue < pair < double, double > > candidates;
		X.clear();
		Y.clear();
		
		candidates.push(make_pair(0, 0));
		candidates.push(make_pair(W, 0));
		candidates.push(make_pair(0, L));
		candidates.push(make_pair(W, L));				

		for (int i = 0; i < N; i++) {
			double x = -1, y = -1;
			while (!candidates.empty()) {
				double tx = candidates.top().first;
				double ty = candidates.top().second;
				candidates.pop();
				
				bool is_valid = true;
				for (int j = 0; j < i; j++) {
					if (fabs(X[j] - tx) < 2 * R[j] && fabs(Y[j] - ty) < 2 * R[j]) {
						is_valid = false;
						break;
					}
				}			
				if (is_valid) {
					x = tx;
					y = ty;
					break;
				} else {
//					printf("invalid: %lf %lf\n", tx, ty);
				}
			}
			
			if (x == -1 && y == -1) {
				printf("\nError\n");
				return 0;
			}
			
			// printf("%lf %lf\n", x, y);

			X.push_back(x);
			Y.push_back(y);
			candidates.push(make_pair(max(0.0, x - 2 * R[i]), max(0.0, y - 2 * R[i])));
			candidates.push(make_pair(max(0.0, x - 2 * R[i]), min((double)L, y + 2 * R[i])));
			candidates.push(make_pair(min((double)W, x + 2 * R[i]), max(0.0, y - 2 * R[i])));
			candidates.push(make_pair(min((double)W, x + 2 * R[i]), min((double)L, y + 2 * R[i])));
			
//			printf("add: %lf %lf\n", max(0.0, x - R[i]), max(0.0, y - R[i]));
//			printf("add: %lf %lf\n", max(0.0, x - R[i]), min((double)L, y + R[i]));
//			printf("add: %lf %lf\n", min((double)W, x + R[i]), max(0.0, y - R[i]));
//			printf("add: %lf %lf\n", min((double)W, x + R[i]), min((double)L, y + R[i]));
		}
	
		printf("Case #%d: ", testcase);	
		for (int i = 0; i < N; i++) {
			printf("%lf %lf ", X[idx2[i]], Y[idx2[i]]);
		}
		printf("\n");
	}

	return 0;
} 