#include<cstdio>
#include<cstring>
#include<string>

#include<map>
#include<algorithm>

using namespace std;

#define inf 9999999LL
typedef long long LL;

LL x[9999], v[9999];
LL a[9999],w[9999];

int main(){
	int tt,n,k;
	LL b,t;
	scanf("%d", &tt);
	for(int ii=0;ii<tt;ii++){
		scanf("%d%d%I64d%I64d", &n, &k, &b, &t);
		for(int i=0;i<n;i++)scanf("%I64d", &x[n-1-i]);
		for(int i=0;i<n;i++)scanf("%I64d", &v[n-1-i]);
		
		for(int i=0;i<n;i++){
			int ti = x[i]+v[i]*t;
			if(ti >=b){
				int kl=0;
				for(;kl<i && w[kl]<b;kl++);
				a[i]=kl;
			}else a[i]=inf;
			w[i]=ti;
			sort(w,w+(i+1));
		}
		
		sort(a, a+n);
		LL ans=0;
		for(int i=0; i<k; i++)ans+=a[i];
		
		if(ans >=inf)
			printf("Case #%d: IMPOSSIBLE\n", ii+1);
		else
			printf("Case #%d: %I64d\n", ii+1, ans);
	}
	
	return 0;
}

