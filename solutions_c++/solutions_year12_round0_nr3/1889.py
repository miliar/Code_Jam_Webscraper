#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <stack>
#define FWD(a,b,c) for(int a=(b); a<(c); a++)
#define BCK(a,b,c) for(int a=(b); a>(c); a--)
#define FE(a,b) for(typeof(b.end()) a=b.begin(); a!=b.end(); a++)
#define ALL(a) a.begin(), a.end()
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

int M[2000010];

int len(int x){
	int r = 0;
	while(x){++r;x/=10;}
	return r;
}

int min(int a){
	int r, d = len(a), p = 1, w = a;
	for(int i=1; i<d; ++i) p*= 10;
	for(int i=0; i<20; ++i){
		a = a/10 + (a%10)*p;
		w = min(w, a);
	}
	return w;
}

int main(){
	int z, a, b;
	long long r;
	scanf("%d\n", &z);
	FWD(i,1,z+1){
		r = 0;
		scanf("%d %d", &a, &b);
		FWD(i,0,b+1)
			M[i] = 0;
		FWD(j,a,b+1){
			r += (long long)M[min(j)];
			++M[min(j)];
		}
		printf("Case #%d: %lld\n", i, r);
	}
	return 0;
}
