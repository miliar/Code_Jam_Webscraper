#include<stdio.h>
#include<stdlib.h>
int a[1010],v[1010],Z[1010]={};
int main(){
	freopen("D-large.in","r",stdin);
	freopen("D2.out","w",stdout);
	int T,t,n,i,ans,j,z;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		ans=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)Z[i]=0;
		for(i=0;i<n;i++){
			scanf("%d",&a[i]);
			a[i]--;
			//if(Z[a[i]]==1)return 0;
			//Z[a[i]]=1;
			v[i]=0;
		}
		for(i=0;i<n;i++){
			if(a[i]==i)continue;
			j=i;
			z=0;
			while(v[j]==0){
				v[j]=1;
				j=a[j];
				z++;
			}
			ans+=z;
		}
		printf("Case #%d: %d.000000\n",t,ans);
	}
} 
