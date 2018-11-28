#include <cstdio>
#include <algorithm>
using namespace std;

int T , N;
int d[10005], l[10005];
bool ok[10005][10005];

bool yes;

void dfs(int i,int j){
	if (ok[i][j]) return;
	ok[i][j] = true;
	
	if (j==N-1) yes = true;

	for (int k=j+1;!yes && k<N && d[j]+min(l[j],d[j]-d[i]) >= d[k];++k){
		if (!ok[j][k]) dfs(j,k);
	}
	for (int k=i-1;!yes && k>=0 && d[i]-min(l[i],d[j]-d[i]) <= d[k];--k){
		if (!ok[k][i]) dfs(k,i);
	}
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		scanf("%d", &N);
		for (int i=0;i<N;++i){
			scanf("%d%d", &d[i], &l[i]);
		}
		
		scanf("%d", &d[N]);
		l[N] = 0;
		++N;
		
		
		for (int i=0;i<N;++i){
			for (int j=0;j<N;++j) ok[i][j] = false;
		}
		
		yes  = false;
		for (int i=1;i<N;++i){
			if (d[i] <= d[0]*2){
				dfs(0,i);
				//ok[0][i] = true;
			}
		}
		
		
		printf("Case #%d: ", tc);
		if (yes) puts("YES");
		else puts("NO");
	}
	return 0;
}
