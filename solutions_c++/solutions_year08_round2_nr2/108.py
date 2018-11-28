#include <iostream>
#include <vector>

using namespace std;

const long long MP = 1000010;
long long cnt[4][3][3];
bool isprime[MP];
vector<int> primes;

int root[1000010];

int getRoot(int x) {
   if (root[x] <0) return x;
   return root[x] = getRoot(root[x]);
}

void Union(int a, int b) {
   int ra = getRoot(a);
   int rb = getRoot(b);
   if (ra != rb) {
      root[ra] += root[rb];
      root[rb] = ra;
   }
}


int main() {
	int cases;
	cin >> cases;

	for(int i=0; i<MP; i++) isprime[i] = 1;
	isprime[0] = isprime[1] = 0;
	for(long long i=2; i<MP; i++) if (isprime[i]) {
		for(long long j=i*i; j<MP; j+=i) { isprime[j] = 0; }
		primes.push_back(i);
	}

	for(int c=0; c<cases; c++) {
		long long A, B, P;
		cin >> A >> B >> P;

		for(int i=0; i<=B-A; i++) root[i] = -1;

		for(int pi=0; pi<primes.size(); pi++) {
			long long p = primes[pi];
			if (p < P) continue;

			/*
			int fst = -1;
			for(long long x=A; x<=B; x++) {
				if (x%p != 0) continue;

				if (fst == -1) fst = x;
				else Union(x-A, fst-A);
			}
			*/

			long long x = (A / p) * p;
			while(x < A) x += p;

			while(x + p <= B) {
				Union(x-A, x-A+p);
				x+=p;
			}
		}

		int ans=0;
		for(int i=0; i<=B-A; i++) if(root[i] < 0) ans++;
		cout << "Case #" << (c+1) << ": " << ans<<endl;
	}
}
