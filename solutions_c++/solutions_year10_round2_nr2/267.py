#include<cstdio>
#include<cstring>

int T,n,k,b,time,x[55],v[55];
bool ok[55];

int main(){
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		scanf("%d%d%d%d",&n,&k,&b,&time);
		for (int i=1;i<=n;++i) scanf("%d",&x[i]);
		for (int i=1;i<=n;++i) scanf("%d",&v[i]);
		memset(ok,0,sizeof(ok));
		
		for (int i=1;i<=n;++i){
			if ((b-x[i])<=(v[i]*time)) ok[i]=1;
		}
		int ans=0,pass=0;
		for (int i=n;i>=1;--i){
			if (pass>=k) break;
			if (ok[i]){
				++pass;
				for (int j=i+1;j<=n;++j) if (!ok[j]) ++ans;
			}
		}
		if (pass<k) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
