#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#define MAX 999999999
int ans[2010],a[2010];
int M(int l,int r,int x){
	long long y = (long long)(ans[r]-ans[l])*(r-x)/(r-l);
	return ans[r]-(int)y-1;
}
int DO(int l,int r){
	if(l==r-1)return 0;
	if(a[l+1]>r)return -1;
	if(a[l+1]==r){
		ans[l+1]=M(l,r,l+1);
		return DO(l+1,r);
	}
	else{
		int i=l+1,j=0,re=0,XD[2010];
		while(i!=r){
			if(a[i]>r)return -1;
			XD[j++]=i;
			i=a[i];
		}
		XD[j]=r;
		ans[XD[j-1]]=M(l,r,XD[j-1]);
		re+=DO(XD[j-1],r);
		for(i=j-2;i>=0;i--){
			ans[XD[i]]=M(XD[i+1],XD[i+2],XD[i]);
			re+=DO(XD[i],XD[i+1]);
		}
		return re;
	}
}
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.txt","w",stdout);
	int t,T,n,i,F;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d",&n);
		F=0;
		for(i=1;i<n;i++){
			scanf("%d",&a[i]);
		}
		ans[1]=MAX;
		i=1;
		while(i!=n){
			ans[a[i]]=MAX;
			if(DO(i,a[i])!=0){F=1;break;}
			i=a[i];
		}
		printf("Case #%d:",t);
		if(F){
			puts(" Impossible");
		}
		else{
			for(i=1;i<=n;i++)printf(" %d",ans[i]);
			puts("");
		}
		//fflush(stdout);
	}
	scanf(" ");
} 
