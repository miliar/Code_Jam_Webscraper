#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

vector<int> primes;

int inv(int x, int p) {
	int P = p;
	int a1=1, a2=0, b1=0, b2=1;
	while (x != 1) {
		int m = p/x;
		int tmp = p%x;
		p = x;
		x = tmp;
		a2 -= a1*m;
		b2 -= b1*m;
		a2 %= P;
		b2 %= P;
		swap(a1,a2); swap(b1,b2);
	}
	return ((a1%P)+P)%P;
}

int main() {
	{
	vector<bool> sieve = vector<bool>(1000000,0);
	for (int i = 2; i < 1000000; i++) {
		if (sieve[i]) continue;
		primes.push_back(i);
		for (int j = 2*i; j < 1000000; j += i) sieve[j] = 1;
	}
	}

	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);

		int D;
		int K; scanf("%d%d",&D,&K);
		long long tentoD=1; for (int i = 0; i < D; i++) tentoD *= 10;
		long long v[20]; for(int i = 0; i < K; i++) {scanf("%lld",&v[i]);}
		
		long long ans = -1;
		bool fail = 0;
		
		if (K > 2 && v[0] != v[1]) {
			for (int i = 0; i < primes.size(); i++) {
				int P = primes[i];
				if (P >= tentoD) break;
				bool possible=1;
				for (int j = 0; j < K; j++) {
					if (P <= v[j]) possible=0;
				}
				if (!possible) continue;
				// get inverses
				long long A = (inv((P+v[0]-v[1])%P,P) * (v[1]-v[2]));
				long long B = (inv((P+v[0]-v[1])%P,P) * (((v[0]*v[2])%P)-((v[1]*v[1])%P)));
				A = ((A%P)+P)%P;
				B = ((B%P)+P)%P;

				for (int i = 0; i+1 < K; i++) {
					if ((A*v[i]+B)%P != v[i+1]) possible=0;
				}
				if (!possible) continue;

				if (possible) {
					long long newans = (A*v[K-1]+B)%P;
					if (ans == -1 || ans == newans) {
						ans = newans;
					} else  {
						fail = 1;
					}
				}
			}
		} else {
			if (K >= 2 && v[0] == v[1]) {
				ans = v[0];
			} else {
				fail = 1;
			}
		}
		
		printf("Case #%d: ",test);
		if (fail) {
			printf("I don't know.");
		} else {
			assert(ans!=-1);
			printf("%lld",ans);
		}
		printf("\n");
	}

}
