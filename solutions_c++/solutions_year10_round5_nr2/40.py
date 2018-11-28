#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int dy[100000], B[100];
vector<int> dd[100000];


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, N;
	long long L, mx;
	scanf("%d",&T);
	int t, i, j, k;
	for(t=1;t<=T;t++){
		printf("Case #%d: ", t);
		scanf("%I64d %d", &L, &N);
		for(i=0;i<N;i++){
			scanf("%d",&B[i]);
			if(i==0 || B[i] > mx) mx = B[i];
		}
		for(i=0;i<mx;i++) dy[i] = -1;
		dy[0] = 0;

		for(i=0;i<N;i++){
			if(B[i] == mx) continue;
			for(j=0;j<mx;j++) dd[j].clear();
			for(j=0;j<mx;j++){
				if(dy[j] >= 0) dd[ dy[j] ].push_back(j);
			}

			for(j=0;j<mx;j++){
				for(k=0;k<dd[j].size();k++){
					if(dy[dd[j][k]] == j){
						int ttt = dd[j][k] + B[i], minus = 0;
						if(ttt >= mx){
							ttt -= (int)mx;
							if(dy[ttt] == -1 || dy[ttt] > j) {
								dy[ttt] = j;
								dd[j].push_back(ttt);
							}
						}
						else{
							if(dy[ttt] == -1 || dy[ttt] > j+1){
								dy[ttt] = j+1;
								dd[j+1].push_back(ttt);
							}
						}
					}
				}
			}
		}
		if(dy[L%mx] == -1) printf("IMPOSSIBLE\n");
		else printf("%I64d\n", (L / mx) + dy[L%mx]);

	}
	return 0;
}