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

int p;
int T[15][1024];
int L[15][1024];
int w;

int main(){
	int z;
	scanf("%d", &z);
	z++;
	FWD(q,1,z){
		scanf("%d", &p);
		FWD(j,0,1<<p){
			scanf("%d", &L[p][j]);
		}
		w=0;
		BCK(i,p-1,-1){
			FWD(j,0,1<<i){
				scanf("%d", &T[i][j]);
				L[i][j]=min(L[i+1][2*j], L[i+1][2*j+1]);
				if(L[i][j]){
					L[i][j]--;
				}else{
					w++;
				}
			}
		}
		printf("Case #%d: %d\n", q, w);
	}
}
