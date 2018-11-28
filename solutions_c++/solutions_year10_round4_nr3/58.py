#include <stdio.h>
#include <map>

using namespace std;

int dat[130][130];
int next[130][130];
int R;
int main(){
	int T;
	int testcase = 0;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	while(T-- > 0) { 
		++testcase;
		int ans = 0;
		scanf("%d",&R);
		int i,j,k;
		for(i=0;i<=100;i++){
			for(j=0;j<=100;j++){
				dat[i][j] = 0;
			}
		}
		for(i=0;i<R;i++){
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(j=x1;j<=x2;j++){
				for(k=y1;k<=y2;k++){
					dat[j][k] = 1;
				}
			}
		}


		for(ans=0;;ans++){
			int flg = 0;
			for(j=0;j<=100;j++){
				for(k=0;k<=100;k++){
					if(dat[j][k]){
						flg = 1;
						if(dat[j-1][k] == 0 && dat[j][k-1] == 0){
							next[j][k] = 0;
						}else{
							next[j][k] = dat[j][k];
						}
					}
					if(dat[j][k] == 0 && j && k){
						if(dat[j-1][k] && dat[j][k-1]){
							next[j][k] = 1;
						}
					}
				}
			}
			if(flg == 0) break;

			memcpy(dat,next,sizeof(next));
		}


		printf("Case #%d: %d\n",testcase, ans);

	}
	return 0;
}

