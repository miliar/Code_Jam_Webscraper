#include <stdio.h>
int T, n;
char map[100][100];
int dd[100];
int dt[100];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	while(T>0){
		scanf("%d",&n);
		int i, j;
		for(i=0;i<n;i++) scanf("%s",map[i]);
		for(i=0;i<n;i++){
			int tj;
			tj = 0;
			for(j=0;j<n;j++){
				if(map[i][j] == '1') tj = j;
			}
			dd[i] = tj;
		}
		for(i=0;i<n;i++) dt[i] = -1;
		for(j=n-1;j>=0;j--){
			for(i=0;i<n;i++){
				if(dd[i] <= n-j-1){
					if(dt[i] == -1){
						dt[i] = j;
						break;
					}
				}
			}
		}
		int cc;
		cc = 0;
		for(i=0;i<n;i++){
			for(j=i+1;j<n;j++){
				if(dt[i] < dt[j]){
					cc ++;
				}
			}
		}
		static int tt=1;
		printf("Case #%d: %d\n",tt++,cc);

		T --;
	}
	return 0;
}