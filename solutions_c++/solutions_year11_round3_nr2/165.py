#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

long long num[1000010];
long long a[1000010];
long long sum[1000010];
long long tx[1000010];

long long cmp(long long c,long long d){
	return c >d;
}
int main(){
	freopen("D://B-large.in","r",stdin);
    freopen("D://B-large.out","w",stdout);
	int ts ; 
	scanf("%d",&ts);
	for(int cases = 1 ; cases<=ts;++cases){
		int L , C,N; 
		long long t ; 
		scanf("%d%lld%d%d",&L,&t,&N,&C);
		for(int i = 0; i<C;++i)scanf("%lld",&a[i]);
		int cnt = 0 ; 
		for(int k = 0 ;cnt<N ;++k){
			for(int i = 0 ; i<C;++i){
				int pr = k * C + i ;
				if( pr < N ){
					num[pr] = a[i];
					cnt++;
				}
				int en = k * C + i + 1 ;
				if( en > N ) break;
			}
		}
		long long res = -1; 
		long long tsum = 0 ; 
		for(int i = 0 ; i<N ;++i){
			tsum+= num[i] ;
			if( i == 0 ) sum[i] = 0; 
			else sum[i] =sum[i-1] + num[i-1];
		}
		int id = 0 ; 
		tsum *= 2 ;
		sum[N] = sum[N-1] + num[N-1];
		for(;id<N;++id){
			if( sum[id] * 2 <= t && sum[id+1] * 2 >= t ){
				break;
			}
		}
		cnt = 1 ; 
		tx[0] = num[id] - ( t/2 - sum[id] ); 
		for(int i = id + 1 ; i<N;++i)
			tx[cnt++] = num[i] ; 
		sort(tx,tx+cnt,cmp);
		for(int i = 0 ; i<L&&i<cnt;++i){
			tsum -= tx[i] ;
		}
		printf("Case #%d: %lld\n",cases,tsum);
	}
	return 0;
}