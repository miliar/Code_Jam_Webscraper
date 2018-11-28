#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string.h>

using namespace std;
int use[55];
char mm[55][55],lf[55];
int ans,n,op;
int dd[100],tt[100],tmp[45];

void merge(int left ,int mid ,int right){
	int i=left,j=mid+1,k=0;
	while((i<=mid)&&(j<=right)){
		if(dd[i]<=dd[j])
			tt[k++]=dd[i++];
		else{
			tt[k++]=dd[j++];
			
			ans+=mid-i+1;  //¼ÆËãÄæÐòÊý
			
		}
	}
	while(i<=mid) tt[k++]=dd[i++];
	while(j<=right) tt[k++]=dd[j++];
	for(i=0,k=left;k<=right;) dd[k++]=tt[i++];
}

void mergesort(int left,int right){
	int mid=(left+right)>>1;
	if(left<right){
		mergesort(left,mid);
		mergesort(mid+1,right);
		merge(left,mid,right);
	}
}

void dfs(int dep){
	if(dep==n){
		ans=0;	
		for(int i=1;i<=n;i++){
			dd[i]=tmp[i];
		//	printf("%d",dd[i]);
		}
	//	printf("\n");
		mergesort(1,n);
		if(ans<op){
		
			
			op=ans;
		}
		return;
	}
	int i,J;
	for(i=0;i<n;i++){
		
		if(use[i]||lf[i]>dep) continue;
		
		use[i]=1;
		tmp[dep+1]=i;		
		dfs(dep+1);
		use[i]=0;
	}
}

int main(){
	int i,J,ncase,ii;
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	
	scanf("%d",&ncase);
	for(ii=1;ii<=ncase;ii++){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",mm[i]);
			for(J=n-1;J>=0;J--)
				if(mm[i][J]!='0') break;
			lf[i]=J;
		}
		op=99999;
		memset(use,0,sizeof(use));
		dfs(0);
		printf("Case #%d: %d\n",ii,op);
	}
}
