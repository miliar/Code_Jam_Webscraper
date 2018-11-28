#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#define N 1000005
using namespace std;
bool isp[N];
long long p[1000000]={2}, top=1;

int main(){
	int T, time=0, ans, i, j;
	long long n, k;
	for(i=3; i*i<N; i+=2){
		if(!isp[i]){
			p[top++]=i;
			for(j=i*i; j<N; j+=i+i) isp[j]=1;
		}
	}
	for( ; i<N; i+=2)
		if(!isp[i]) p[top++]=i;
	scanf("%d", &T);
	while(T--){
		scanf("%I64d", &n);
		if(n==1){
			printf("Case #%d: 0\n", ++time);
			continue;
		}
		ans=1;
		for(i=0; p[i]*p[i]<=n; i++){
			k=n;
			while(k>=p[i]){
				ans++;
				k/=p[i];
			}
			ans--;
		}
		printf("Case #%d: %d\n", ++time, ans);
	}
    return 0;
}
