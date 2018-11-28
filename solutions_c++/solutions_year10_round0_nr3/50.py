#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
inline bool prime(int n)
{
	if(n<=1)	return false;
	if(n==2||n==3)	return true;
	int k=sqrt(double(n));
	for(int i=2;i<=k;++i)
		if(n%i==0)	return false;
	return true;
}
*/
int main()
{
//	freopen("input.txt","r",stdin);
	int T,t;
	long long r,k,n;
	long long g[1000];
	long long s[1000];
	int last[1000];
	scanf("%d",&T);
	for(t=1;t<=T;++t){
		scanf("%lld%lld%lld",&r,&k,&n);
		for(int i=0;i<n;++i)
			scanf("%lld",&g[i]);
		long long tot=0;
		for(int i=0;i<n;++i){
			s[i] = g[i];
			last[i] = i;
			for(int j = (i+1)%n;j!=i&&s[i]+g[j]<=k;j = (j+1)%n){
				s[i] += g[j];
				last[i] = j;
			}
//			printf("%lld ",s[i]);
		}
		int now = 0;
		while(r--){
			tot += s[now];
			now = (last[now] + 1)%n;
		}
		printf("Case #%d: %lld\n",t,tot);
	}
	return 0;
}