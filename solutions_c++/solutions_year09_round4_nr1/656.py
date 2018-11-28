#include <stdio.h>

int n;
int dat[41];

int main(){
	int TT,T;
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		int i;
		int j,k;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			dat[i] = 0;
			for(j=0;j<n;j++){
				int tmp;
				scanf("%1d",&tmp);
				if(tmp == 1){
					dat[i] = j;
				}
			}
		}
		int ans = 0;

		for(i=0;i<n;i++){
			if(dat[i] > i){
				for(j=i+1;j<n;j++){
					if(dat[j] <= i){
						int tmp = dat[j];
						for(k=j-1;k>=i;k--){
							dat[k+1] = dat[k];
						}
						dat[i] = tmp;
						ans += j-i;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n",TT,ans);
	}
	return 0;
}
