#include<iostream>
using namespace std;
typedef long long ll;
struct group{
  ll next;
  ll sum;
  ll val;
  int flag;
}gp[1001];
int main(){
  ll kase,i,j,m,T,R,N,K,cost,ctr,cycleLen, cycleSum;
  scanf("%lld",&T);
  for(kase=1;kase<=T;kase++){
	scanf("%lld %lld %lld",&R,&K,&N);
	for(i=0;i<N;i++)
	  scanf("%lld",&gp[i].val);
	
	for(i=0;i<N;i++){
	  gp[i].sum=gp[i].val;
	  gp[i].next=(i+1)%N;
	  j=(i+1)%N;
	  gp[i].flag=0;
	  for(;j!=i;j = (j+1)%N){
		if(gp[i].sum + gp[j].val <= K){
		  gp[i].sum += gp[j].val;
		  gp[i].next = (j+1)%N;
		}
		else
		  break;
	  }
	  
	}
	
	gp[0].flag=1;
	cost = gp[0].sum;
	ctr=1;
	i = gp[0].next;
	
	while((gp[i].flag != 1) && (ctr<R)){
	  
	  cost += gp[i].sum;
	  ctr++;
	  gp[i].flag=1;
	  i=gp[i].next;
	  
	}
	if(ctr != R){
	  cycleLen=1;
	  cycleSum = gp[i].sum;
	  m=i;
	  while(gp[m].next != i){
		m = gp[m].next;
		cycleSum += gp[m].sum;
		cycleLen++;
		
	  }
	  
	  cost = cost + cycleSum*((R-ctr)/cycleLen);
	  ctr += cycleLen*((R-ctr)/cycleLen);
	  while(ctr < R){
		
		cost += gp[i].sum;
		ctr++;
		i=gp[i].next;
	  }
	}
	
	printf("Case #%lld: %lld\n",kase,cost);
  }
  return 0;
}

	 
	  
	
	
	  
  