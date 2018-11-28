#include <stdio.h>
#define MAX 108

int bact[2][MAX][MAX];
void solve(){
	bool left=1;
	int time=0, cur=0;
	int minx = MAX, miny=MAX, maxx=0, maxy=0;
	int i,j,R,x1,x2,y1,y2;
	scanf("%d", &R);
	for(i=0;i<MAX;i++){
		for(j=0;j<MAX;j++){
			bact[0][i][j]=0;
			bact[1][i][j]=0;
		}
	}
	for(;R>0;R--){
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		if(x1<minx)	minx=x1;
		if(y1<miny) miny=y1;
		if(x2>maxx) maxx=x2;
		if(y2>maxy)	maxy=y2;
		for(i=y1;i<=y2;i++){
			for(j=x1;j<=x2;j++){
				bact[0][i][j] = 1;
				left=true;
			}
		}
	}
	while(left){
		left=false;
		for(i=miny;i<=maxy;i++){
			for(j=minx;j<=maxx;j++){
				if(bact[cur][i-1][j] && bact[cur][i][j-1]){
					bact[cur^1][i][j] = 1;
					left=true;
				}
				else if(!bact[cur][i-1][j] && !bact[cur][i][j-1])
					bact[cur^1][i][j] = 0;
				else {
					bact[cur^1][i][j] = bact[cur][i][j];
					if(bact[cur][i][j])
						left=true;
				}
			}
		}
		cur^=1;
		time++;
	}
	printf("%d\n", time);
}
int main(){
	int T, i;
	scanf("%d", &T);
	for(i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}
