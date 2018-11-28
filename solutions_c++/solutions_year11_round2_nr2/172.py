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

long long d;
int c, v;
long long r;
long long p, k;
vector<long long> P;

bool check(long long t){
	long long r = -10000000000000LL;
	FE(p,P){
		if(*p > r + d){
			r = max(r + d, *p - t);
		}else{
			if(*p + t < r + d)
				return 0;
			r = r + d;
		}
	}
	return 1;
}

int main(){
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		P.clear();
		scanf("%d %lld", &c, &d);
		d *= 2LL;
		FWD(i,0,c){
			scanf("%lld %d", &r, &v);
			FWD(j,0,v)
				P.push_back(2*r);
		}
		p = 0;
		k = 10000000000000LL;
		if(check(p)){
			printf("Case #%d: 0\n", z);
		}else{
			while(k - p > 1){
				if(check((k+p)/2))
					k = (k+p)/2;
				else
					p = (k+p)/2;
			}
			printf("Case #%d: %.1lf\n", z, ((double)k)/2.0);
		}
	}
	return 0;
}

