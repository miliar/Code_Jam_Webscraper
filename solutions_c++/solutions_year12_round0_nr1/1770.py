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

#define MAX_N 200010

char A[] = "ejpmysljylckdkxveddknmcrejsicpdrysi";
char B[] = "ourlanguageisimpossibletounderstand";
char C[] = "rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd";
char D[] = "therearetwentysixfactorialpossibilities";
char E[] = "dekrkdeoyakwaejtysrreujdrlkgcjv";
char F[] = "soitisokayifyouwanttojustgiveup";
char S[512];
char T[120];

int main(){
	FWD(i,'a','z'+1)
		S[i] = i+'A'-'a';
	int n, z;
	n = strlen(A);
	FWD(i,0,n)
		S[A[i]] = B[i];
	n = strlen(C);
	FWD(i,0,n)
		S[C[i]] = D[i];
	n = strlen(E);
	FWD(i,0,n)
		S[E[i]] = F[i];
	S['z'] = 'q';
	S['q'] = 'z';

	scanf("%d\n", &z);
	FWD(i,1,z+1){
		printf("Case #%d: ", i);
		scanf("%[^\n]\n", T);
		n = strlen(T);
		FWD(i,0,n)
			if(T[i] == ' ')
				printf(" ");
			else
				printf("%c", S[T[i]]);
		printf("\n");
	}
	return 0;
}
