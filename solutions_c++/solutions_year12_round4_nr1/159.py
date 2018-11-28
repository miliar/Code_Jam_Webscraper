#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int Maxn=10100;

int f[Maxn];
int d[Maxn],l[Maxn];
int n,N,Test;

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	scanf("%d",&Test);
	for (int ii=1;ii<=Test;++ii)
	{
		printf("Case #%d: ",ii);
		scanf("%d",&n);
		for (int i=1;i<=n;++i) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&N);
		memset(f,0,sizeof(f));
		f[1]=d[1];
		for (int i=1;i<=n;++i)
			for (int j=i+1;d[j]-d[i]<=f[i];++j)
					f[j]=max(f[j],min(l[j],d[j]-d[i]));
		bool flag=false;
		for (int i=1;i<=n;++i)
			if (f[i]+d[i]>=N) flag=true;
		if (flag) printf("YES\n");
		else printf("NO\n");
	}
	
	return 0;
}