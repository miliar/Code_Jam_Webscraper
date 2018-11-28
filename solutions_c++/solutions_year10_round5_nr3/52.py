#include <iostream>
#include <cstdlib>
#define maxn 2000001

using namespace std;

int i,n,j,ii,tt,k,x,y;
bool flag;
int a[maxn*2+1];
long long ans,p;

int main() {
	freopen("hotdog.in","r",stdin);
	freopen("hotdog.out","w",stdout);

	scanf("%d\n",&tt);
	for (ii=1;ii<=tt;++ii) {
		memset(a,0,sizeof(a));
		scanf("%d\n",&n);
		for (i=1;i<=n;++i) {
			scanf("%d%d\n",&x,&y);
			a[x+maxn]=y;
		}
		ans=0; flag=true;
		while (flag) {
			flag=false;
			for (i=0;i<2*maxn;++i)
				if (a[i]>1) {
					flag=true;
					k=a[i]/2;
					for (j=i-k;j<=i+k;++j)
						if (j!=i) a[j]++;
					if ((a[i] & 1)==0) a[i]=0;
					else a[i]=1;
					p=k;
					ans+=(2*p+1)*p*(p+1)/6;
				}
		}
		printf("Case #%d: ",ii);
		cout << ans << endl;
	}
}
