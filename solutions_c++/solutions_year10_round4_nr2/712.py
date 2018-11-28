#include <cstdio>
#include <algorithm>

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define FOR_R(i,a,b)	for(int i=(b)-1;i>=(int)(a);--i)

int main(){
	int T;
	int M[1024];
	int map[10][1024];
	int buf[10];
	scanf("%d ", &T);
	for(int xxx = 1; xxx <= T; ++xxx){
		int P;
		scanf("%d ", &P);
		int team = 1 << P;
		FOR(i, 0, team){
			scanf("%d ", M+i);
			M[i] = P - M[i];
		}
		FOR_R(i, 1, P+1){
			int count = 1 << (i - 1);
			FOR(j, 0, count) scanf("%d ", &(map[P - i][j]));
		}
		int ret = 0;
		while(1){
			const int max_e = std::max_element(M, M + team) - M;
			int m = M[max_e];
			if(!m) break; else M[max_e] = 0;
			int e = max_e, count = 0;
			FOR(i, 0, P){
				buf[i] = e >>= 1;
				if((count += (map[i][e] < 0)) >= m) break;
			}
			if(count < m){
				count = m - count;
				FOR_R(i, 0, P){
					if(map[i][buf[i]] < 0) continue;
					ret += map[i][buf[i]];
					map[i][buf[i]] = -1;
					if((--count) <= 0) break;
				}
			}
		}
		printf("Case #%d: %d\n", xxx, ret);
	}
	return 0;
}
