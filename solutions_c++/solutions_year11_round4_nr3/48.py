#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define maxn 1000000
#define LL long long

using namespace std;

bool f[maxn+1];
int prime[maxn];
int cnt;
int tt;

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	memset(f,false,sizeof(f));
	f[1]=true; cnt=0;
	for (int i=2;i<=maxn;++i) {
		if (!f[i]) {
			prime[++cnt]=i;
			for (int j=maxn/i;j>=2;--j)
				f[j*i]=true;
		}
	}

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		LL x;
		LL ans=0;
		cin >> x;
		for (int i=1;i<=cnt;++i) {
			int cur=0;
			LL tmp=prime[i];
			while (tmp<=x) {
				cur++;
				tmp=tmp*(LL)prime[i];
			}
			if (cur>0) ans+=(LL)(cur-1);
		}
		if (x!=1) ans++;
		printf("Case #%d: ",ii);
		cout << ans << endl;
	}
}
