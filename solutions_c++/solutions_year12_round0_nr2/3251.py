#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main(void) {
	int testnum;
	scanf("%d\n", &testnum);

	for (int testcase = 1; testcase <= testnum; testcase++) {
		int ans = 0;
		int N, S, p;
		int Total[100];
		
		scanf("%d %d %d", &N, &S, &p);
		for (int i = 0; i < N; i++) {
			scanf("%d", &Total[i]);
		}
		
		int surprising[100], good_surprising[100];
		int not_surprising[100], good_not_surprising[100];
		int d[100][101];
		
		for (int i = 0; i < N; i++) {
			int r = Total[i] % 3;
			int q = Total[i] / 3;
			// Total[i] = q * 3 + r;
			
			surprising[i] = 0;
			not_surprising[i] = 0;
			good_surprising[i] = 0;
			good_not_surprising[i] = 0;
			for (int j = 0; j <= S; j++) {
				d[i][j] = 0;
			}
			
			if (r == 0) {
				// q, q, q
				not_surprising[i] = 1;
				if (q >= p)
					good_not_surprising[i] = 1;
				
				// q - 1, q, q + 1 surprising
				if (q - 1 >= 0 && q + 1 <= 10) {
					surprising[i] = 1;
					if (q + 1 >= p)
						good_surprising[i] = 1;					
				}				
			} else if (r == 1) {
				// q, q, q + 1
				if (q + 1 <= 10) {
					not_surprising[i] = 1;
					if (q + 1 >= p)
						good_not_surprising[i] = 1;
				}
				// q - 1, q + 1, q + 1 surprising
				if (q - 1 >= 0 && q + 1 <= 10) {
					surprising[i] = 1;
					if (q + 1 >= p)
						good_surprising[i] = 1;					
				}			
			} else if (r == 2) {
				// q, q, q + 2 surprising
				if (q + 2 <= 10) {
					surprising[i] = 1;
					if (q + 2 >= p)
						good_surprising[i] = 1;					
				}
				
				// q, q + 1, q + 1
				if (q + 1 <= 10) {
					not_surprising[i] = 1;
					if (q + 1 >= p)
						good_not_surprising[i] = 1;
				}			
			}
		}
		
		d[0][0] = not_surprising[0] && good_not_surprising[0];
		d[0][1] = surprising[0] && good_surprising[0];
		
		for (int i = 1; i < N; i++) {
			if (surprising[i]) {
				for (int j = 1; j <= S; j++)
					d[i][j] = d[i - 1][j - 1] + good_surprising[i];
			}
			if (not_surprising[i]) {
				for (int j = 0; j <= S; j++)
					d[i][j] = max(d[i][j], d[i - 1][j] + good_not_surprising[i]);
			}
		}
		
		for (int i = 0; i < N; i++) {
			ans = max(ans, d[i][S]);
		}

		printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}

