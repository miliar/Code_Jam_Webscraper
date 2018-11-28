#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int g[1010];
int f[1010];
int main(){
	int i,j,k,l,time,n,r,test,t,temp,sum;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&test);
	for (t=1;t<=test;t++){
		scanf("%d%d%d",&r,&k,&n);
		memset(g,0,sizeof(g));
		for (i=0;i<n;i++){
			scanf("%d",&g[i]);
		}
		i=0;time=0;sum=0;
		while (time<r){
			temp=0;j=0;
			while (temp+g[i]<=k&&j<n){
				temp+=g[i];
				i=(i+1)%n;
				j++;
			}
			time++;
			sum+=temp;
		}
		printf("Case #%d: %d\n",t,sum);
	}
	return 0;
}
