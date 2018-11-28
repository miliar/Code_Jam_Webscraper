#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<algorithm>

using namespace std;
#define INF (1<<29)
#define MAXQ 128

int v[MAXQ];
int memo[MAXQ][MAXQ];



int faz(int i,int j){
	int min1,k,resp,ck;
	
	if(memo[i][j] >= 0) return memo[i][j];
	
	
	if(i+1 == j) return memo[i][j] = 0;
	
	min1 = INF;
	
	for(k = i+1;k<j;k++){
		ck = v[k] - v[i] - 1;
		ck += v[j] - v[k] - 1;
		ck += faz(i,k) + faz(k,j);
		min1 = min(min1,ck);
	}
	
	return memo[i][j] = min1;
	
}

int main(){
	int T,i,resp,p,q;
	
	scanf("%d ",&T);
	int tot = T;
	while(T--){
		scanf("%d %d",&p,&q);
		
		for(i=0;i<q;i++)
			scanf("%d",v+i+1);
		
		v[0] = 0;
		v[q+1] = p+1;
			
		memset(memo,-1,sizeof(memo));
		resp = faz(0,q+1);
			
		printf("Case #%d: %d\n",tot-T,resp);
	}

	return 0;
}
