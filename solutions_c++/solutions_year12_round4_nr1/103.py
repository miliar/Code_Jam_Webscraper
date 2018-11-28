#include<stdio.h>
#include<stdlib.h>
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int t,T,j,i,n;
	int a[10010][2],c[10010]={};
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		for(i=0;i<=n;i++){
			if(i!=n)scanf("%d%d",&a[i][0],&a[i][1]);
			else if(i==n){scanf("%d",&a[i][0]);a[i][1]=1;}
			if(i==0)c[i]=0;
			else c[i]=a[i][0];
			for(j=0;j<i;j++){
				if(a[j][0]+a[j][0]-c[j]>=a[i][0]){
					if(a[j][0]<c[i])c[i]=a[j][0];
				}
			}
			if(c[i]<a[i][0]-a[i][1])c[i]=a[i][0]-a[i][1];
		}
		if(c[n]==a[n][0])printf("Case #%d: NO\n",t);
		else printf("Case #%d: YES\n",t);
	}
} 
