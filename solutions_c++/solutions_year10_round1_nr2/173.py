#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
#define INF 10000000
using namespace std;
int F[105][256];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int ans = INT_MAX,D,I,M,N;
		scanf("%d%d%d%d",&D,&I,&M,&N);
		memset(F[0],0,sizeof(F[0]));
		for(int i=1;i<=N;++i) {
			int a;
			scanf("%d",&a);
			for(int v=0;v<256;++v) {
				F[i][v] = F[i-1][v] + D;
				for(int k=0;k<256;++k) {
					if(!M && v != k) continue;
					if(!M) F[i][v] = min(F[i][v],F[i-1][k] + abs(v-a));
					else F[i][v] = min(F[i][v],F[i-1][k] + I*(max(0,abs(v-k)-1)/M) + abs(v-a));
				}
			}
		}
		for(int v=0;v<256;++v) ans = min(ans,F[N][v]);
		printf("Case #%d: %d\n",cn,ans);
	}
}
