#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

std::vector<int> prm;

#define MAXN	(2000000)
static struct ZBIOR {
	int p, r;
} zbiory[MAXN];

static int findSet(int x) {
	int s = x;
	while(zbiory[x].p!=x) {
		x = zbiory[x].p;
	}
	while(zbiory[s].p!=s) {
		int ns = zbiory[s].p;
		zbiory[s].p = x;
		s = ns;
	}
	return x;
}
static void linkSet(int x, int y) {
	x = findSet(x);
	y = findSet(y);
	if(zbiory[x].r > zbiory[y].r) {
		zbiory[y].p = x;
	} else {
		zbiory[x].p = y;
		if(zbiory[x].r == zbiory[y].r)
			zbiory[y].r++;
	}
}

static void makeSet(int x) {
	zbiory[x].p = x;
	zbiory[x].r = 0;
}


int wynik(long long A,long long B,long long P) {
	if(P>(B-A)) return B+1-A;
	int N = (B+1-A);
	for(int i=0;i<N;i++)
		makeSet(i);

	for(int ip=0; ip<(int)prm.size(); ip++) {
		int p = prm[ip];
		if(p>N) break;
		if(p<P) continue;
		long long a = (A/p)*p;
		if(a<A) a+=p;

		long long j1=a, j2=a+p;
		while(j2<=B) {
			//printf("lacze %lld - %lld\n",j1,j2);
			linkSet(j1-A,j2-A);
			j1 += p;
			j2 += p;
		}
	}

	int suma = 0;
	for(int i=0;i<N;i++) {
		if(zbiory[i].p == i)
			suma ++;
	}
	return suma;
}

int main() {
	static bool prime[MAXN];
	for(int p=0;p<MAXN;p++) {
		prime[p] = true;
	}
	//memset(prime,-1,sizeof(prime));
	prime[0]=0, prime[1]=0;
	for(int p=2;p<MAXN;p++) {
		if(!prime[p]) continue;
		for(int i=2*p;i<MAXN;i+=p)
			prime[i] = 0;
	}
	for(int p=2;p<MAXN;p++) {
		if(prime[p]) {
			//printf("%d\n",p);
			prm.push_back(p);
		}
	}

	int N; scanf("%d",&N);
	for(int iN=1;iN<=N;iN++) {
		long long A,B,P;
		scanf("%lld%lld%lld",&A,&B,&P);
		printf("Case #%d: %d\n",iN,wynik(A,B,P));
	}
	return 0;
}

