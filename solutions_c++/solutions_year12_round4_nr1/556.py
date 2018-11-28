#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<vector>
struct node {
	int L, x;
	void get() {
		scanf("%d%d", &x, &L);
	}
} ;

using namespace std;
node P[10005];
int S[10005];
int N;

inline int min(int a, int b) {
	if ( a < b )
		return a;
	return b;
}

int main()
{
	int T;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		scanf("%d", &N);
		for ( int i = 0 ; i < N ; i++ ) {
			P[i].get();
		}
		scanf("%d", &P[N].x);
		P[N].L = 1;
		memset(S,0,sizeof(S));
		S[0] = min(P[0].x, P[0].L);
		for ( int i = 0 ; i < N ; i++ ) {
			for ( int j = i+1 ; j <= N ; j++ ) {
				if ( S[i]+P[i].x >= P[j].x ) {
					int A = min(P[j].L, P[j].x - P[i].x);
					if ( S[j] < A ) {
						S[j] = A;
					}
				}
				else break;
			}
		}
		if ( S[N] )
			printf("Case #%d: YES\n", t);	
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}
