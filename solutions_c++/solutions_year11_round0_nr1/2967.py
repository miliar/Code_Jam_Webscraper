#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <queue>
#define FOR(A,B) for(A = 0; A < B; A++)
#define MAXT 111
#define MAXN 111

using namespace std;
typedef struct
{
	int posO, posB;
	int time;
	int currentMove;
} state;
char R[1000];
int P[1000];
int d[8][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}, {1,1}, {-1,-1},{-1,1},{1,-1}};
int main()
{
	int T;
	scanf("%d", &T);
	int t = 0;
	FOR(t, T) {
		int N, i, j, k;
		scanf("%d\n", &N);
		FOR(i, N) { char b[5]; scanf("%s %d", b, &P[i]); R[i] = b[0]; } 
		state first; first.posO = 1; first.posB = 1;
		bool visited[MAXT][MAXT][MAXN];
		FOR(i, MAXT) FOR(j, MAXT) FOR(k, MAXN) visited[i][j][k] = false;
		first.time = 0;
		first.currentMove = 0;
		queue<state> q;
		q.push(first);
	//	FOR(i, N) {printf("%c %d ", R[i], P[i]);}
	//	printf("\n");
		while(!q.empty())
		{
			state x = q.front(); q.pop();
			//if(t == 2) printf("Reached state: time=%d, posO=%d, posB=%d, cM=%d\n", x.time, x.posO, x.posB, x.currentMove);
			if(x.currentMove == N)
			{
				printf("Case #%d: %d\n", t+1, x.time);
				break;
			//;	return 0;
			}
			int r = R[x.currentMove];
			int p = P[x.currentMove];
			int cM = x.currentMove;
			int Ti = x.time+1;
			state n;
			int posO = 9999;
			int posB = 9999;
			if(r == 'O' && x.posO == p) {
				cM++;
				posO = x.posO;
			}
			if(r == 'B' && x.posB == p) {
				cM++;
				posB = x.posB;
			}
			n.time = Ti;
			n.currentMove = cM;
			FOR(i, 8) {
				int nposO = posO == 9999 ? x.posO+d[i][0] : posO;
				int nposB = posB == 9999 ? x.posB+d[i][1] : posB;
				if(nposO >= 1 && nposO <= 100 && nposB >= 1 && nposB <= 100) {
					n.posO = nposO; n.posB = nposB;
					if(!visited[n.posO][n.posB][n.currentMove])
					{
						q.push(n);
						visited[n.posO][n.posB][n.currentMove] = true;
					}
				}
			}
		}
	}
	return 0;
}
