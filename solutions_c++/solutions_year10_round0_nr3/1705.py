/*
Author  :kabir.iut06
Compiler: GNU C++ Code Blocks
problem : C
Contest : 2010 Google CodeJam qualification Round*/

#include<stdio.h>
#include<string.h>
typedef long long LL;
LL n,num,b,t,k,txt,r;
#define S 1005
LL val[S],go[S],in[S],sum,tot[S],hoise[S];
int nisi[S];
int main(){
	//freopen("1.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%lld",&t);
	while(t--){
		int i,j,jj;
		scanf("%lld%lld%lld",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%lld",&in[i]);
		for(i=0;i<n;i++)go[i]=i;

		for(i=0;i<n;i++){
			sum=0;
			for(j=i,jj=0;jj<n&&(sum+in[j]<=k);j=(j+1)%n,jj++){
				sum+=in[j];
			}
			val[i]=sum;
			go[i]=j;
		}
		//for(i=0;i<n;i++)printf("%d %lld next= %lld tot=%lld\n",i,in[i],go[i],val[i]);
		bool paisi=false;
		memset(nisi,0,sizeof(nisi));
		sum=0;
		j=0;
		memset(tot,0,sizeof(tot));
		for(i=0;;){
			if(j==r)break;
			nisi[i]++;
			if(nisi[i]>=2&&paisi==false){
				paisi=true;
				r=r-hoise[i];
				sum=tot[i]+(sum-tot[i])*(r/(j-hoise[i]));
				r=r%(j-hoise[i]);
				j=0;
				memset(nisi,0,sizeof(nisi));
				memset(tot,0,sizeof(tot));
				if(j==r)break;
			}
			tot[i]=sum;
			hoise[i]=j;
			sum=sum+val[i];
			i=go[i];
			j++;
		}
		printf("Case #%lld: %lld\n",++txt,sum);
	}
	return 0;
}