#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>

#define C(x) memset(x, -1, sizeof(x))
#define INF 1000000000

//int l[2][200][200];
int c[200][200];

int T, K;

inline bool inmap(int x, int y){
	if(x > K+K || x < 0 || y > K+K || y < 0)return 0;
	if(c[x][y] == -1) return 0;
	return 1;
}

int abs(int a){
	return a>0 ? a : -a;
}

int calc(int ii, int jj){
/*for(int i=0; i<K; i++){
		for(int j=K-i-1; j<K+i; j++){
			//scanf("%d", &c[i][j]);
			int ni, nj;
			ni = 2*ii-i; nj = 2*jj-i;
			if(inmap(ni, nj) && c[ni][nj] != c[i][j]) return INF;
			if(inmap(i, nj) && c[i][nj] != c[i][j]) return INF;
			if(inmap(ni, j) && c[ni][j] != c[i][j]) return INF;
		}
	}
	for(int i=K-2; i>=0; i--){
		for(int j=K-i-1; j<K+i; j++){
			//scanf("%d", &c[i+K][j]);
			int ni, nj;
			ni = 2*ii-i-K; nj = 2*jj-i;
			if(inmap(ni, nj) && c[ni][nj] != c[i+K][j]) return INF;
			if(inmap(i+K, nj) && c[i+K][nj] != c[i+K][j]) return INF;
			if(inmap(ni, j) && c[ni][j] != c[i+K][j]) return INF;
		}
	}*/
	int cost = 0, max = 0, d;
	for(int i=0; i<K+K; i++)
		for(int j=0; j<K+K; j++){
		//	if(ii==5&&jj==0&&i==6&&j==2)printf("%d: %d %d   %d\n", inmap(i,j), i, j, c[i][j]);
			if(!inmap(i,j))continue;
			d = abs(i-ii) + abs(j-jj);
			max = d>max ? d : max;
			int ni=2*ii-i, nj=2*jj-j;
	//		if(ii==4&&jj==1)printf("%d %d to %d %d\n", i, j, ni, nj);
		//	if(ii==5&&jj==0&&i==6&&j==2)printf("%d %d\n", ni, nj);
			if(inmap(ni, nj)&&c[ni][nj] != c[i][j])return INF;
			//else cost++;
			if(inmap(i, nj)&&c[i][nj] != c[i][j]) return INF;
			//else cost++;
			if(inmap(ni, j)&&c[ni][j] != c[i][j]) return INF;
			//else cost++;
		}
	max++;
//	printf("midst %d %d : cost %d\n", ii, jj, max*max);
	return max*max;
}

int main(){
	scanf("%d", &T);
	for(int cc=1; cc<=T; cc++){
		scanf("%d", &K);
		int tt, min = INF;
	//	C(l);
		for(int i=0; i<200; i++)
			for(int j=0; j<200; j++)
				c[i][j]= -1;
		for(int i=0; i<K; i++){
			for(int j=0; j<=i; j++){
			//for(int j=K-i-1; j<K+i; j++){
				scanf("%d", &c[i][j*2+K-i-1]);
			//	printf("get %d %d\n", i, j*2+K-i-1);
			}
		}
		int cnt= K;
		for(int i=K-2; i>=0; i--){
			for(int j=0; j<=i; j++){
			//for(int j=K-i-1; j<K+i; j++){
				scanf("%d", &c[cnt][j*2+K-i-1]);
			//	printf("get %d %d\n", i, j*2+K-i-1);
			}
			cnt++;
		}
		int bi, bj;
		for(int i=-2; i<=K+K+2; i++){
			for(int j=-2; j<K+K+2; j++){
				int t = calc(i, j);
				if(min > t){
					bi=i; bj=j;
					min= t;
				}
			}
		}
	//	printf("%d %d\n", bi, bj);
		printf("Case #%d: %d\n", cc, min-K*K);
	}
}
