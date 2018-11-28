#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <set>

using namespace std;



int main(int argc, char **argv) {

	int nbTests;
	int res;
	bool *done = new bool[2000001];
	char b1[11], b2[11];
	int a, b;
	int ll;
	
	scanf("%d", &nbTests);

	for(int n=1; n<=nbTests; ++n) {
		res = 0;
		memset(done, 0, 2000001*sizeof(bool));
		memset(b1, 0, sizeof(b1));
		memset(b2, 0, sizeof(b2));
		scanf("%d%d", &a, &b);
		itoa(a, b1, 10);
		ll = strlen(b1);

		for(int ii=a, s=b; ii<=s; ++ii) {
			if(!done[ii]) {
				done[ii] = true;
				itoa(ii, b1, 10);
				set<int> si;

				for(int i=1; i<ll; ++i) {
					memcpy(b2, &b1[ll-i], i*sizeof(char));
					memcpy(&b2[i], b1, (ll-i)*sizeof(char));

					int nn = atoi(b2);
					if(nn>=a && nn<=b && !done[nn] && si.find(nn) == si.end()) {
						si.insert(nn);
						res++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", n, res);
	}

	delete[] done;
	return 0;
}
