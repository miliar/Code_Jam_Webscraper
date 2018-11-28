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
#define RCH(a) scanf("%c", &a)
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

int n,k,b,t,s,r;
int X[55];
int V[55];
int F[55];

int main(){
	int z;
	scanf("%d", &z);
	z++;
	FWD(q,1,z){
		s=0;
		r=0;
		scanf("%d %d %d %d", &n, &k, &b, &t);
		FWD(i,0,n) scanf("%d", &X[i]);
		FWD(i,0,n) scanf("%d", &V[i]);
		FWD(i,0,n) F[i]=( (X[i]+V[i]*t) >= b );
		BCK(i,n-1,-1){
			if(k==0) break;
			if(F[i]){
				s+=r;
				k--;
			}else{
				r++;
			}
		}
		if(k==0) printf("Case #%d: %d\n", q, s); else printf("Case #%d: IMPOSSIBLE\n", q);
	}
}
