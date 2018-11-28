#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXSIEVE 1000000
#define MAXPRIMES 100000
#define i64 __int64

i64 n;

char p[MAXSIEVE+5];
int primes[MAXPRIMES];
int ct;

void sieve() {
	int i,j;
	memset(p,0,sizeof(p));
	for(i=2;i*i<=MAXSIEVE;i++) for(j=i*i;j<=MAXSIEVE;j+=i) p[j] = 1;
	ct = 0;
	for(i=2;i<=MAXSIEVE;i++) if(!p[i]) primes[ct++] = i;
}

int main() {
	sieve();
	int T,kase=1;
	i64 r,t,x;
	int i;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %I64d",&n);
		r = 0;
		if(n > 1) r++;
		for(i=0;i<ct;i++) {
			t = primes[i] * (i64)primes[i];
			if(t > n) break;
			x = n;
			while(1) {
				r++;
				x /= primes[i];
				if(x < primes[i]) break;
			}
			r--;
		}
		printf("%I64d\n",r);
	}
	return 0;
}