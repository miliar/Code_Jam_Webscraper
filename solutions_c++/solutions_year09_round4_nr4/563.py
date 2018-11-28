#include <stdio.h>
#include <math.h>
int n;
struct plant{
	int x,y,r;
} dat[50];
int main(){
	int TTT,testcase;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&TTT);
	for(testcase=1;testcase <= TTT;testcase ++){
		int i;
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d%d",&dat[i].x,&dat[i].y,&dat[i].r);
		}
		if(n == 1){
			printf("Case #%d: %lf\n",testcase,(double)dat[0].r);
		}else if(n == 2){
			printf("Case #%d: %lf\n",testcase,(double)(dat[0].r > dat[1].r ? dat[0].r : dat[1].r));
		}else if(n == 3){
			double r1,r2,r3;
			int i,j,k;
			r3 = 1e60;
			for(i=0;i<3;i++){
				for(j=i+1;j<3;j++){
					for(k=0;k<3;k++){
						if(k ==i || k== j)continue;
						r1 = (sqrt((double)((dat[i].x-dat[j].x)*(dat[i].x-dat[j].x)+(dat[i].y-dat[j].y)*(dat[i].y-dat[j].y))) + dat[i].r + dat[j].r) / 2;
						r2 = dat[k].r;
						if(r1 < r2){
							if(r3 > r2){
								r3 = r2;
							}
						}else{
							if(r3 > r1){
								r3 = r1;
							}
						}
					}
				}
			}
			printf("Case #%d: %lf\n",testcase,r3);
		}
	}
	return 0;
}
