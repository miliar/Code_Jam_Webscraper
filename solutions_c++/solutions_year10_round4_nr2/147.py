#include <stdio.h>
#include <algorithm>
using namespace std;

int dat[1024];
int p[10][1024];
int dy[10][1024][12];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, n ,t, i, j, k, l, q;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		memset(dy, 63, sizeof(dy));
		scanf("%d",&n);
		for(i=0;i<(1<<n);i++)	scanf("%d",&dat[i]);
//		sort(dat, dat+(1<<n));
		for(i=0;i<(1<<n);i++) dat[i] = n-dat[i];
		for(i=0;i<n;i++){
			for(j=0, k=0;j<(1<<(n-i-1));j++, k+=(1<<(i+1))){
				scanf("%d",&p[i][j]);
				if(true){
					if(i == 0){
						dy[i][j][max(dat[k],dat[k+1])] = 0;
						if(max(dat[k],dat[k+1]) > 0) dy[i][j][max(dat[k],dat[k+1])-1] = p[i][j];
					}
					for(l=0;l<12;l++){
						if(i > 0){
							dy[i][j][l] = /*min(*/min(dy[i][j][l], dy[i-1][j*2][l] + dy[i-1][j*2+1][l]);/*, dy[i-1][j*2][k+(1<<i)][l] + dy[i-1][j*2+1][k][l])*/;
							dy[i][j][l] = min(dy[i][j][l], dy[i-1][j*2][l+1] + dy[i-1][j*2+1][l+1] + p[i][j]);
							//dy[i][j][k][l] = min(dy[i][j][k][l], dy[i-1][j*2][k+(1<<i)][l+1] + dy[i-1][j*2+1][k][l+1] + p[i][j]);
						}
						if(l > 0)dy[i][j][l] = min(dy[i][j][l], dy[i][j][l-1]);
					}
				}
			}
		}
		printf("Case #%d: %d\n", t, dy[n-1][0][0]);
	}
	return 0;
}