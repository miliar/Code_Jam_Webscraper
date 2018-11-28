#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<deque>
#include<vector>

using namespace std;

#define MAXN (64)
#define EPS (0.000000001)

double times[MAXN];
int v[MAXN];
long long int pi[MAXN];
bool foi[MAXN];

int main(){
	int nT,T;
	int tt,n,k,i,j;
	long long int barn,delta;
		
	scanf("%d",&nT);
	for(T=1;T<=nT;T++){
		printf("Case #%d: ",T);
		scanf("%d %d %lld %d",&n,&k,&barn,&tt);
		
		for(i=0;i<n;i++){
			scanf("%lld",pi + i);			
		}
		
		for(i=0;i<n;i++){
			scanf("%d",v + i);
			foi[i] = false;	
		}
		
		for(i=0;i<n;i++){
			delta = barn - pi[i];
			times[i] = (double)delta/v[i];			
		}
		
		j=0;
		for(i = n-1;i>=0;i--){
			if(times[i] - EPS<= (double) tt){
				j++;
				foi[i] = true;
			}
			if(j == k) break;
		}
		
		if(i < 0){
			printf("IMPOSSIBLE\n");
			continue;
		}
		
		int resp = 0;
		for(;i<n;i++){
			if(foi[i]){
				for(j=i+1;j<n;j++) if(!foi[j]) resp++;
			}
		}
		
		printf("%d\n",resp);
	}
}
