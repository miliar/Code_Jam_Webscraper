#include<stdio.h>

struct point{
	int x,y;
};

point p[1001];

int main(){
	freopen("A-large (1).in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j,t,f=1,n;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d %d",&p[i].x,&p[i].y);
		}
		int count=0;
		for(i=0;i<n-1;i++){
			for(j=i+1;j<n;j++){
				if((p[i].x<p[j].x&&p[i].y>p[j].y)||(p[i].x>p[j].x&&p[i].y<p[j].y))
				    count++;
			}
		}
		printf("Case #%d: %d\n",f++,count);
	}
	return 0;
}
