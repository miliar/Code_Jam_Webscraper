#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
		int S, R, T, X, N;
		scanf ( "%d %d %d %d %d", &X, &S, &R, &T, &N);
		vector <int> B, E, W;
		int before_x = 0;
		for ( int i = 0; i < N; i++) {
			int b, e, w;
			scanf("%d %d %d", &b, &e, &w);
			if (before_x < b) {
				B.push_back(before_x);
				E.push_back(b);
				W.push_back(0);
			}
			B.push_back(b);
			E.push_back(e);
			W.push_back(w);
			before_x = e;
		}	
		int n = B.size();
		if (E[n - 1] != X) {
			B.push_back(E[n - 1]);
			E.push_back(X);
			W.push_back(0);
			n++;
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				double t1 = (E[i] - B[i]) / (double)(W[i] + S)
					- (E[i] - B[i]) / (double)(W[i] + R);
				double t2 = (E[j] - B[j]) / (double)(W[j] + S)
					- (E[j] - B[j]) / (double)(W[j] + R);
				if (W[i] > W[j]) {
					swap(B[i], B[j]);
					swap(E[i], E[j]);
					swap(W[i], W[j]);
				}
			}
		}	
		
		double t = 0;
		double remainT = T;
		for (int i = 0; i < n; i++) {
			if ( (E[i] - B[i]) / (double)(W[i] + R) < remainT) {
				t += (E[i] - B[i]) / (double)(W[i] + R);
				remainT -= (E[i] - B[i]) / (double)(W[i] + R);
			} else {
				t += remainT;
				t += (E[i] - B[i] - (W[i] + R) * remainT) / (double)(W[i] + S);
				remainT = 0;
			}
		}		
		printf("Case #%d: %lf\n", testcase, t);
	}
	return 0;
}