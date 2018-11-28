#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <stack>
#include <cstdlib>
using namespace std;
long not_prime[1000002];
long used[1000002];
long fuc(long N){
	int i,j,k;
	int bound;
	bound = (int)sqrt(N)+1;
	long count=0;
	long ans=0;
		for(i=2;i<=bound;i++){
//		printf("i is %d not is %ld\n",i,not_prime[i]);
			if(not_prime[i]==0){
				ans ++;
				count+=(long)floor(log((double)N)/log((double)i));
			}
		}
//printf("ans %ld is N is %ld count is %ld bound is %d\n",ans,N,count,bound);
return ans+N-count-1;
}
int main(){
	int i,j,k,n,T,l,m,M;
	scanf("%d",&n);
	for(i=2;i<=1000;i++){
		if(not_prime[i]==0)
			for(j=i+i;j<=1000;j+=i){
				not_prime[j] = 1;
			}
	}

	long N;
	long large,small;
	for(T=0;T<n;T++){
		scanf("%ld",&N);
		large = N;
		small = fuc(N);
		printf("Case #%d: %ld\n",T+1,large-small);
	}
	return 0;
}

