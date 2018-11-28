#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int p[100000];
int main()
{
	int T;
	scanf("%d",&T);
	for (int test=1; test<=T; ++test)  {


		int N, L, H;
		scanf("%d%d%d",&N, &L, &H);
		for (int i=0; i<N; ++i) {
			scanf("%d",&p[i]);
		}

		bool found = false;
		for (int i=L; i<=H; ++i) {
			found = true;
			for (int j=0; j<N; ++j) {
				if (p[j] % i == 0 ||  i % p[j] == 0) {
					continue;
				}
				found = false;
				break;
			}
			if (found) {
				printf("Case #%d: ", test);
				printf("%d\n",i);
				break;
			}
		}
		if (!found) {
			printf("Case #%d: NO\n", test);
		}
	}
	return 0;
}
