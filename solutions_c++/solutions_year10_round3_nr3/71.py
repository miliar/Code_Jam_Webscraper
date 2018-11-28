#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define REP(i,n) for(int i=0;i<n;++i)
#define SZ(v) (int)(v.size())
#define PB push_back
#define MP make_pair
#define CL(v,x) memset(v,x,sizeof(v))

int G[520][520];
int row[520][520], col[520][520];
int cover[520];
int N, M;
char line[100];

inline bool valid(int x, int y, int L) {
	if (col[x][y] < L) return false;
	for (int j=y;j<y+L;++j) if ((G[x][j]==-1) || (row[x][j] < L)) return false;
	//for (int i=x;i<x+L;++i) if (col[i][y] < L) return false;
	return true;
}

inline void fill(int x, int y, int L) {
	for (int i=x;i<x+L;++i) for (int j=y;j<y+L;++j)
		G[i][j] = -1;
}

int main(){
	FILE* fin=freopen("input.in", "r", stdin);
	int T;
	scanf("%d\n", &T);

	for (int t=0;t<T;++t) {
		CL(G,-1);
		CL(row,0);
		CL(col,0);
		scanf("%d%d", &M, &N);
		gets(line);
		int len = N / 4;
		REP(i,M) {
			gets(line);
			REP(j,len) {
				int val;
				if ((line[j]>='0')&&(line[j]<='9')) {
					val = line[j] - '0';
				}
				else val = line[j] - 'A' + 10;
				REP(k, 4) {
					G[i][j*4+3-k] = val & 1;
					val /= 2;
				}
			}
		}

		CL(cover, 0);
		len = min(N, M);
		int cnt=0;
		for (int L=len;L>=1;--L){
			int maxl= 0;
			for (int i=M-1;i>=0;--i) {
				for (int j=N-1;j>=0;--j) {
					if (G[i][j] == -1) {
						row[i][j] = 0;
						col[i][j] = 0;
						continue;
					}
					
					if (G[i][j]+G[i][j+1]==1) 
						col[i][j] = col[i][j+1] + 1;
					else
						col[i][j] = 1;
					if (col[i][j] > maxl) maxl = col[i][j];
					
					if (G[i][j]+G[i+1][j]==1)
						row[i][j] = row[i+1][j] + 1;
					else 
						row[i][j] = 1;
					if (row[i][j] > maxl) maxl = row[i][j];
				}
			}
			if (maxl < L) L = maxl;
			

			//printf("%d\n", L);
			//REP(i,M) {
				//REP(j,N) printf("%d ", col[i][j]);
				//printf("\n");
			/*}*/


			REP(i,M) REP(j,N) if (G[i][j]!=-1) {
				if (valid(i, j, L)) {
					cover[L]++;
					if (cover[L]==1) cnt++;
					fill(i, j, L);
				}
			}

		}

		printf("Case #%d: %d\n", t+1, cnt);
		for (int L=len;L>=1;--L) if (cover[L] > 0) 
			printf("%d %d\n", L, cover[L]);

	}

	return 0;
}
