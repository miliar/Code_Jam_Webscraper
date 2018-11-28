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

int C, D, N, M;
char P[256][256];
bool Q[256][256];
char S[110];
char T[110];
int U[256];

int main(){
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		M = 0;
		FWD(i,'A','Z'+1)
			FWD(j,'A','Z'+1){
				P[i][j] = '#';
				Q[i][j] = 0;
				U[j] = 0;
			}
		scanf("%d", &C);
		FWD(i,0,C){
			scanf("%s", S);
			P[S[0]][S[1]] = P[S[1]][S[0]] = S[2];
		}
		scanf("%d", &D);
		FWD(i,0,D){
			scanf("%s", S);
			Q[S[0]][S[1]] = Q[S[1]][S[0]] = 1;
		}
		scanf("%d %s", &N, S);
		FWD(i,0,N){
			++U[S[i]];
			T[M++] = S[i];
			while(M>1){
				if(P[T[M-2]][T[M-1]] != '#'){
					--U[T[M-2]];
					--U[T[M-1]];
					++U[P[T[M-2]][T[M-1]]];
					T[M-2] = P[T[M-2]][T[M-1]];
					--M;
				}else{
					break;
				}
			}
			if(M>0){
				FWD(j,'A','Z'+1){
					if(U[j] && 	Q[T[M-1]][j]){
						M = 0;
						FWD(k,'A','Z'+1)
							U[k] = 0;
						break;
					}
				}
			}
			T[M] = 0;
		}
		printf("Case #%d: [", z);
		FWD(i,0,M-1)
			printf("%c, ", T[i]);
		if(M) printf("%c", T[M-1]);
		printf("]\n");
	}
	return 0;
}

