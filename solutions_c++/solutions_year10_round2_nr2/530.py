#include <stdio.h>
#include <iostream>

using namespace std;

int T;
int x[100];
int v[100];

int main() {
	scanf("%d", &T);

	for (int cs = 1; cs <= T; ++cs) {                                                                                                                      
		printf("Case #%d: ", cs);                                                                                                                      

		int n,k,b,t;
		scanf("%d %d %d %d", &n,&k,&b,&t);

		for (int i=0; i < n; ++i) {
			scanf("%d", &x[i]);
		}
		for (int i=0; i < n; ++i) {
			scanf("%d", &v[i]);
		}

/*		for (int i=0; i < n; ++i) {
			printf("%d \n", x[i] );
		}
*/

		int keep = 0;
		int ans = 0;
		int pos = 1;
		int last = 0;
		for (int i=n-1; i >= 0; --i) {
			if (keep == k) {
				break;
			}

			int time = (b - x[i]) / v[i];
			if ((b - x[i]) % v[i] != 0) {
				time++;
			}
//			cerr << x[i] << " " << time << endl;
			//printf("%d\n", time);
			
			if (time <= t) {
				keep++;
				ans += last;
			} else {
				last++;
			}
		}

		if (keep == k) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}

}
