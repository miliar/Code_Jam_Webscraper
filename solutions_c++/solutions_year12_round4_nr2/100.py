#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
struct ee{int r,x;}a[1010];
bool cmp(struct ee x,struct ee y){return x.r>y.r;}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int t,T,j,i,n,W,L,x,y,h,ans[1010][2];
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		x=0;
		scanf("%d%d%d",&n,&W,&L);
		y=L;
		for(i=0;i<n;i++){
			scanf("%d",&a[i].r);
			a[i].x=i;
		}
		std::sort(a,a+n,cmp);
		h=-a[0].r;
		for(i=0;i<n;i++){
			y+=a[i].r;
			if(y>L){
				x+=h+a[i].r;
				y=0;
				h=a[i].r;
			}
			ans[a[i].x][0]=x;
			ans[a[i].x][1]=y;
			y+=a[i].r;
		}
		//if(x>W)while(1);
		printf("Case #%d:",t);
		for(i=0;i<n;i++)printf(" %d.0 %d.0",ans[i][0],ans[i][1]);
		puts("");
	}
	scanf(" ");
} 
