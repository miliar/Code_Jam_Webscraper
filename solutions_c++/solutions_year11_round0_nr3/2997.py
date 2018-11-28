#include <stdio.h>
#include <string.h>
#include <vector>
//#include <algorithm>
#include <queue>
#define FOR(A,B) for(A = 0; A < B; A++)
#define MAXN 20

//using namespace std;

int op(int x, int y)
{
	return ((~(x&y))&x|(~(x&y)&y));
}
int max, N, C[MAXN];

void bt(int firstPile, int fcount, int secondPile, int seansSum, int k)
{
//	printf("Called bt(%d, %d, %d, %d).\n", firstPile, secondPile, seansSum, k);
	if(fcount > 0 && fcount != N && firstPile == secondPile && seansSum > max && k == N) {
		max = seansSum;
	}
	if(k >= N) return;
	bt(op(firstPile, C[k]), fcount+1, secondPile, seansSum+C[k], k+1);
	bt(firstPile, fcount, op(secondPile, C[k]), seansSum, k+1);
}

int main()
{
	int T;
	scanf("%d", &T);
	int t = 0;
	FOR(t, T) {
		max = -1;
		int i, j, k;
		scanf("%d", &N);
		FOR(i, N) scanf("%d", &C[i]);
		bt(0, 0, 0, 0, 0);
		printf("Case #%d: ", t+1);
		if(max == -1) printf("NO");
		else printf("%d", max);
		printf("\n");
	}
	/*int i,j,k;
	FOR(i, 100) FOR(j, 100) FOR(k, 100) {
		if(op(k, op(i, j)) != op(i, op(j, k)) || op(k, op(i,j)) != op(j, op(i, k))) printf("FUUUU");
	}*/
//	printf("%d %d %d %d", op(op(12,2),5), op(2,op(12,5)), op(7,9), op(50,10));
}
