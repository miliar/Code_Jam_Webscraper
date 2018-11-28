/**
* @author Gareve
* @problem C
* @judge Google Code Jam
*/
#define DEBUG
#ifndef NDEBUG	
	#define DBG(a) cout<<__LINE__<<": "<<#a<<"= "<<a<<endl;
#else
	#define DBG(a) ;
#endif
#include <iostream>
#include <cassert>
#include <cstdio>
#include <vector>
#define L long long
#define MAX 1009

using namespace std;

L vc[MAX],dp[MAX],suma[MAX];
int g[MAX];
L r,k,sum;
int n;

int f(int x){
	sum=0;
	if(vc[x]>k)
		return -1;
	sum=vc[x];
	int y=x,ant=x;

	x=(x+1)%n;
	while(y!=x){
		sum+=vc[x];
		if(sum>k){
			sum-=vc[x];
			return ant;
		}
		ant=x;
		x=(x+1)%n;
	}
	return ant;
}
void resuelva(int c){
	int x,y;
	scanf("%lld %lld %d",&r,&k,&n);

	for(int i=0;i<n;i++){
		scanf("%lld",&vc[i]);
	}
	for(int i=0;i<n;i++){
		g[i]=f(i);
		suma[i]=sum;
		//printf("%d: %lld %d\n",i,suma[i],g[i]);
	}
	L res=0;
	x=0;
	y=0;
	vector<int> bs(n,-1);
	L ciclo,div,falta,long_ciclo;
	bool sw=false;

	for(int i=1;i<=r;i++){
		x=g[y];
		if(sw or bs[x]==-1){
			bs[x]=i;
			res+=suma[y];
			dp[x]=res;
		}else{
			ciclo=res-dp[x]+suma[y];
			long_ciclo=i-bs[x];
			falta=r-i+1;
			//cout<<"Ciclo = "<<ciclo<<" len= "<<long_ciclo<<" Falta="<<falta<<endl;
			res+=suma[y];
			div=falta/long_ciclo;
			res+=ciclo*div;
			i+=(div*long_ciclo);
			if(i>r)
				res-=suma[y];
			sw=true;
		}
		//cout<<x<<" "<<res<<endl;
		y=(x+1)%n;
	}
	//cout<<":"<<ciclo<<" "<<ult<<" ";
	printf("Case #%d: %lld\n",c,res);
}
int main(){
	int q;
	scanf("%d",&q);
	for(int i=1;i<=q;i++){
		resuelva(i);
	}
}

