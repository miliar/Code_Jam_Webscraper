#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct point{
	int x,y;
}ps[1024];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%d%d",&ps[i].x,&ps[i].y);
		int ans=0;
		for(int i=0;i<n;++i){
			for(int j=i+1;j<n;++j){
				//printf("%d %d\n",i,j);
				if((ps[i].x-ps[j].x)*(ps[i].y-ps[j].y)<0){
					++ans;
				}
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}