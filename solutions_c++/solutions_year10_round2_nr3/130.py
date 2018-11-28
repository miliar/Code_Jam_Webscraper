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

int n;
int T[1020][1020];
int S[510];

int main(){
	int z;
	scanf("%d", &z);
	z++;
	FWD(i,0,1020) T[i][0]=0, T[0][i]=1;
	//FWD(i,0,10) printf("%d ", T[0][i]);
	//printf("\n");
	FWD(i,1,1020){
		//printf("%d ", T[i][0]);
		FWD(j,1,1020){
			T[i][j]=0;
			FWD(p,max(i-j,0),i) T[i][j]=(T[i][j]+T[p][j])%100003;
			//printf("%d ", T[i][j]);
		}
		//printf("\n");
	}
	FWD(i,1,505){
		S[i]=0;
		FWD(j,0,i+1){
			S[i]=(S[i]+T[j][i-j])%100003;
		}
		//printf("%d\n", S[i]);
	}
	FWD(q,1,z){
		scanf("%d", &n);
		printf("Case #%d: %d\n", q, S[n-1]);
	}
}
