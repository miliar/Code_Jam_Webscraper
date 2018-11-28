#include<cstdio>
#include<iostream>
using namespace std;
typedef long long ll; 
int next[1010],seen[1010],times[1010];
ll R,K,N,G[1010],count[1010],timesum[1010],ans=0,steps=0,c=0;
void assign(int i)
{
	ll sum=G[i],ind=(i+1)%N;
	while(sum<K && ind!=i){
		if(sum+G[ind]<=K){
			sum+=G[ind];
			ind=(ind+1)%N;
		}
		else	break;
	}
	next[i]=ind;count[i]=sum;
}			
int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		scanf("%Ld %Ld %Ld",&R,&K,&N);
		for(int i=0;i<N;i++){
			scanf("%Ld",&G[i]);
			seen[i]=0;times[i]=0;timesum[i]=0;
		}	
		for(int i=0;i<N;i++)	assign(i);
		ans=0;steps=0;c=0;int ind=0;
		while(!seen[ind]){
			steps++;
			timesum[ind]=c;
			times[ind]=steps;
			seen[ind]=1;
			c+=count[ind];	
			ind=next[ind];
		}
		ll period=steps-times[ind]+1,periodsum=c-timesum[ind];
		if(steps>R)	{ind=0;}
		else		{ans+=timesum[ind];R-=times[ind]-1;ans+=(R/period)*periodsum;R%=period;}
		while(R>0){
			ans+=count[ind];
			R--;
			ind=next[ind];
		}
		printf("Case #%d: %Ld\n",test,ans);
	}
	return 0;
}					
