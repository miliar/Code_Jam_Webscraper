
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

typedef long long ll;

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int r,k,n;scanf("%d%d%d",&r,&k,&n);
		int v[2*n];
		for(int i=0;i<n;i++)scanf("%d",v+i);
		for(int i=0;i<n;i++)v[n+i]=v[i];

		int to[n];
		ll cnt[n];
		int sum=0;
		int topos=0;
		for(int i=0;i<n;i++){
			while(topos<i+n && sum+v[topos]<=k)sum+=v[topos++];
			to[i]=topos%n;
			cnt[i]=sum;
			//cout<<"to["<<i<<"]="<<to[i]<<" cnt"<<cnt[i]<<endl;
			sum-=v[i];
		}

		ll ans=0;
		int pos=0;
		while(r){
			if(r&1){
				ans+=cnt[pos];
				pos=to[pos];
			}
			int nxtto[n];
			ll nxtcnt[n];
			for(int i=0;i<n;i++){
				nxtto[i]=to[ to[i] ];
				nxtcnt[i]=cnt[i]+cnt[ to[i] ];
			}
			memcpy(to,nxtto,sizeof(nxtto));
			memcpy(cnt,nxtcnt,sizeof(nxtcnt));
			r/=2;
		}

		static int npr=1;
		printf("Case #%d: %lld\n",npr++,ans);
	}
	return 0;
}
