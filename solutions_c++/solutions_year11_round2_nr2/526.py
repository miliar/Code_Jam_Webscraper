#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
		int D, C, N = 0;
		scanf("%d %d", &C, &D);
		vector < int > A;
		A.clear();
		for (int i = 0; i < C; i++) {
			int p, v;
			scanf("%d %d", &p, &v);
			for (int j = 0; j < v; j++)
				A.push_back(p);
			N += v;
		}
		
		double s = 0, e = 200000000.0;
		while (e - s > 1e-8) {
			double m = (e + s) / 2.0;
			double x = A[0] - m;
			bool check = true;
			for (int i = 1; i < N; i++) {
				double y = A[i];
				if (y > x + D) {
					if (y - m <= x + D) {
						x = x + D;
					} else {
						x = y - m;
					}
				} else {
					if (y + m >= x + D) {
						x = x + D;
					} else {
						check = false;
						break;
					}	
				}
			}		
			if (check)
				e = m;
			else
				s = m;
		}	
		
		printf("Case #%d: %.10lf\n", testcase, e);
	}
	return 0;
}