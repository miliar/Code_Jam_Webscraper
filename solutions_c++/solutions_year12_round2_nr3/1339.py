#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

#define MAX 505
long long int S[MAX];

vector<long long> sum; // subset sum
map<long long, long long> pack;

int main()
{
	int kase, serial=0, n;
	long long new_sum, z, element;
	bool nothing;

	scanf("%d", &kase);
	while (kase--) {

		sum.clear();
		sum.push_back(0);

		pack.clear();
		pack[0] = 0;

		nothing = true;

		scanf("%d", &n);
		for (int i=0; i<n; ++i) {
			scanf("%lld", S+i);
		}
		sort(S, S+n);

//		for (int i=0; i<n; ++i) {
//			printf("%d ", S[i]);
//		}
//		puts("");

		printf("Case #%d:\n", ++serial);
		for (int i=0; i<n && nothing; ++i) {
//			printf("R#%d:\n", i);

			for (int k=0, m=sum.size(); k<m; ++k) {
				new_sum = sum[k] + S[i];
//				printf("%d + %d = %d", sum[k], S[i], new_sum);
				if (pack.find(new_sum) == pack.end()) {
					sum.push_back(new_sum);
					pack[new_sum] = sum[k];
//					puts(" add");
				} else {
					nothing = false;
//					puts(" found");
					z = new_sum;
					while (z) {
						element = z - pack[z];
						printf("%lld", element);
						z = pack[z];
						if (z)
							putchar(' ');
					}
					puts("");

					printf("%lld", S[i]);
					z = sum[k];
					while (z) {
						element = z - pack[z];
						printf(" %lld", element);
						z = pack[z];
					}
					puts("");

					break;
				}
			}
		}

		if (nothing) {
			puts("Impossible");
		}
	}
	return 0;
}
