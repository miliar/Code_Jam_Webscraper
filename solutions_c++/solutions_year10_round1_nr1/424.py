#include <cstdio>

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)

#define PUT_LEFT(n)		((n))
#define PUT_RIGHT(n)	((n)*60)
#define PUT_ROW(n)		((n)*60*60)
#define PUT_COL(n)		((n)*60*60*60)
#define GET_LEFT(n)		(((n))%60)
#define GET_RIGHT(n)	(((n)/60)%60)
#define GET_ROW(n)		(((n)/60/60)%60)
#define GET_COL(n)		(((n)/60/60/60)%60)
#define VALUE(N,a,x,y)	(0<=(x)&&(x)<(N)&&0<=(y)&&(y)<(N)?(a)[x][y]:0)

const char* RET[] = {"Neither", "Red", "Blue", "Both"};

int main(){
	char buf[100];
	int T;
	scanf("%d ", &T);
	for(int i = 1; i <= T; i++){
		int arr[50][50] = {{0}};
		int cache[50] = {0};
		int N, K;
		scanf("%d %d ", &N, &K);
		REP(j, N){
			scanf("%s ", buf);
			int idx = 0;
			REP(k, N){
				switch(buf[k]){
				case 'R':	cache[idx++] =  1;	break;
				case 'B':	cache[idx++] = -1;	break;
				default:	continue;
				}
			}
			REP(k, idx) arr[j][N - idx + k] = cache[k];
		}
		int ret = 0;
		int tmp[50][50] = {{0}};
		REP(j, N){
			REP(k, N){
				int a = arr[j][k];
				if(!a) continue;
				int a_lt = VALUE(N, arr, j - 1, k - 1);
				int a_t  = VALUE(N, arr, j - 1, k    );
				int a_rt = VALUE(N, arr, j - 1, k + 1);
				int a_l  = VALUE(N, arr, j,     k - 1);
				int c_lt = VALUE(N, tmp, j - 1, k - 1);
				int c_t  = VALUE(N, tmp, j - 1, k    );
				int c_rt = VALUE(N, tmp, j - 1, k + 1);
				int c_l  = VALUE(N, tmp, j,     k - 1);
				int n_lt = a == a_lt ? GET_LEFT (c_lt) + 1 : 1;
				int n_t  = a == a_t  ? GET_RIGHT(c_t ) + 1 : 1;
				int n_rt = a == a_rt ? GET_ROW  (c_rt) + 1 : 1;
				int n_l  = a == a_l  ? GET_COL  (c_l ) + 1 : 1;
				if(n_lt >= K) ret |= a > 0 ? 1 : 2;
				if(n_t  >= K) ret |= a > 0 ? 1 : 2;
				if(n_rt >= K) ret |= a > 0 ? 1 : 2;
				if(n_l  >= K) ret |= a > 0 ? 1 : 2;
				tmp[j][k] = PUT_LEFT(n_lt) + PUT_RIGHT(n_t) + PUT_ROW(n_rt) + PUT_COL(n_l);
			}
		}
		printf("Case #%d: %s\n", i, RET[ret]);
	}
	return 0;
}
