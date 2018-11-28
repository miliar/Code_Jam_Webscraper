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

int n, m, r, mp, ap, l;
char T[210][110];
int L[210];

int main(){
	int z;
	scanf("%d", &z);
	z++;
	FWD(q,1,z){
		RINT(n), RINT(m);
		r=0;
		FWD(i,0,n+m) RSTR(T[i]), L[i]=strlen(T[i]), T[i][L[i]++]='/';
		FWD(i,n,n+m){
			mp=0;
			FWD(j,0,i){
				ap=0;
				while(ap<L[i] && ap<L[j]&& T[i][ap]==T[j][ap]) ap++;
				mp=max(ap, mp);
			}
			mp--;
			while(mp>=0 && T[i][mp]!='/') mp--;
			if(mp<0) mp=0;
			FWD(j,mp,L[i]-1){
				if(T[i][j]=='/') r++;
			}
		}
		printf("Case #%d: %d\n", q, r);
	}
}

