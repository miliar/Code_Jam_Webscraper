#include <cstdio>
using namespace std;

int a[200],b[200],m;

bool isp(int t) {
	for (int i=2;i*i<=t;++i) if (t%i==0) return 0;
	return 1;
}

void ini() {
	for (int i=2;i<=1000;++i) if (isp(i)) a[++m]=i;
}

int main() {
//	freopen("c.in","r",stdin);
//	freopen("c.out","w",stdout);
	ini();
	int T,n;
	scanf("%d",&T);
	for (int c0=1;c0<=T;++c0) {
		int ans=1;
		scanf("%d",&n);
		for (int i=1;i<=m;++i) b[i]=0;
		for (int i=2;i<=n;++i) {
			int t=i,d=0;
			for (int j=1;j<=m;++j) if (t%a[j]==0) {
				int cnt=0;
				while (t%a[j]==0) t/=a[j], ++cnt;
				if (cnt>b[j]) d=1, b[j]=cnt;
				if (t==1) break;
			}
			ans+=d;
		}
		for (int i=1;i<=m;++i) if (a[i]>n) break; else --ans;
		if (n==1) ans=0;
		printf("Case #%d: %d\n",c0,ans);
	}
}
