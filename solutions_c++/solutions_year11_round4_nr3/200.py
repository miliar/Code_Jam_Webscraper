#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <cmath>
#include <limits>
#define FWD(a,b,c) for(int a=(b); a<(c); a++)
#define BCK(a,b,c) for(int a=(b); a>(c); a--)
#define FE(a,b) for(typeof(b.end()) a=b.begin(); a!=b.end(); a++)
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) erase(unique(a.begin(), a.end()), a.end())
#define LL long long
#define ULL unsigned long long
#define PII pair<int, int>
#define PDD pair<double, double>
#define x first
#define y second
#define PACKS(a) int a; scanf("%d", &a); a++; while(--a)

//#define DEBUG
#ifdef DEBUG
	#define debug printf
#else
	#define debug
#endif

using namespace std;

long long n, r, q;
long long P[1000000];
int p;
bool k;

int main(){
	P[0] = 2;
	p = 1;
	for(long long i=3; i<1000010; i+=2){
		k = 1;
		for(int j=0; j<p && P[j]*P[j]<=i; ++j)
			if(i % P[j] == 0){
				k = 0;
				break;
			}
		if(k)
			P[p++] = i;
	}
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		r = 1;
		scanf("%lld", &n);
		if(n == 1)
			r = 0;
		else
			FWD(i,0,p){
				q = P[i];
				q = q*q;
				if(q > n) break;
				do{
					++r;
					q *= (long long)P[i];
				}while(q <= n);
			}
		printf("Case #%d: %lld\n", z, r);
	}
	return 0;
}

