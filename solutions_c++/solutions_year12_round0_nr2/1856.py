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

int main(){
	int z, n, s, p, a, r;
	scanf("%d\n", &z);
	FWD(i,1,z+1){
		r = 0;
		scanf("%d %d %d", &n, &s, &p);
		FWD(j,0,n){
			scanf("%d", &a);
			if(a >= 3*p-2)
				++r;
			else if(p!=1 && s && a >= 3*p-4){
				--s;
				++r;
			}
		}
		printf("Case #%d: %d\n", i, r);
	}
	return 0;
}
