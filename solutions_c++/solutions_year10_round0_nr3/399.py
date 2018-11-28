#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#define FWD(a,b,c) for(int a=(b); a<(c); a++)
#define BCK(a,b,c) for(int a=(b); a>(c); a--)
#define FE(a,b) for(typeof(b.end()) a=b.begin(); a!=b.end(); a++)
#define ALL(a) a.begin(), a.end()
#define RINT(a) scanf("%d", &a)
#define DRINT(a) int a, scanf("%d", &a)
#define RLL(a) scanf("%lld", &a)
#define RSTR(a) scanf("%s", a)
#define UNIQUE(a) erase(unique(a.begin(), a.end()), a.end())
#define ULL unsigned long long
#define PII pair<int, int>
#define PACKS(a) int a; scanf("%d", &a); a++; while(--a)

//#define DEBUG
#ifdef DEBUG
	#define debug printf
#else
	#define debug
#endif

using namespace std;

int t, r, k, n, p;
long long G[1010];
long long z;
long long Z[1010];
int P[1010];

int main(){
	scanf("%d", &t);
	t++;
	FWD(i,1,t){
		scanf("%d %d %d", &r, &k, &n);
		FWD(j,0,n) scanf("%lld", &G[j]);
		printf("Case #%d: ", i);
		FWD(j,0,n){
			z=G[j];
			p=(j+1)%n;
			while(z+G[p]<=k && p!=j) z+=G[p], p=(p+1)%n;
			Z[j]=z;
			P[j]=p;
		}
		p=0;
		z=0;
		FWD(j,0,r){
			z+=Z[p];
			p=P[p];
		}
		printf("%lld\n", z);
	}
}

