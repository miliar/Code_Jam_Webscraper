#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#define maxn 1010

using namespace std;

int f[maxn];
int tt,n;
int a[maxn],b[maxn];
int ans;
int len[maxn];

int check() {
	memset(len,0,sizeof(len));
	int cnt=0;
	for (int i=1;i<=n;++i) {
		int j=0;
		for (int k=1;k<=cnt;++k)
			if (b[k]+1==a[i] && (j==0 || len[k]<len[j])) j=k;
		if (j==0) j=++cnt;
		b[j]=a[i];
		len[j]++;
	}
	int ans=1000000;
	for (int i=1;i<=cnt;++i)
		ans=min(ans,len[i]);
	return ans;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		for (int i=1;i<=n;++i) scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		memset(f,0,sizeof(f));
		ans=check();
		if (ans==1000000) ans=0;
		printf("Case #%d: %d\n",ii,ans);
	}
}
