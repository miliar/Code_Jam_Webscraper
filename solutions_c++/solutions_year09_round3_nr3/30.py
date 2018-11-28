#include <stdio.h>
#define MAX 99999999
int pri[ 103 ];
int dy[ 103 ][ 103 ];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, P, Q;
	scanf("%d",&T);
	int t;
	for(t=1;t<=T;t++)
	{
		scanf("%d %d",&P,&Q);
		int i, j, k;
		for(i=1;i<=Q;i++)scanf("%d",&pri[i]);
		pri[0] = 0;
		pri[Q+1] = P+1;
		for(i=1;i<=Q;i++) for(j=1;j<=Q;j++) dy[i][j] = 0;
		for(i=1;i<=Q;i++){
			dy[i][i] = pri[i+1] - pri[i-1] - 2;
		}
		for(i=1;i<=Q;i++){
			for(j=1;i+j<=Q;j++){
				dy[j][i+j] = MAX;
				for(k=j;k<=i+j;k++){
					int tdy;
					tdy = pri[i+j+1] - pri[j-1] - 2 + dy[j][k-1] + dy[k+1][i+j];
					if(dy[j][i+j] > tdy){
						dy[j][i+j] = tdy;
					}
				}
			}
		}
		printf("Case #%d: %d\n",t, dy[1][Q]);
	}
	return 0;
}