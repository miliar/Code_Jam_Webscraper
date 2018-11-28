#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int d[100005],l[100005],R[100005];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,cas=0;scanf("%d",&T);
	while(T--)
	{
		int n,D,ok=0;scanf("%d",&n);
		for(int i = 0; i < n; i++)
			scanf("%d%d",&d[i],&l[i]),R[i]=-1;
		scanf("%d",&D);
		R[0] = 2*d[0];
		for(int i = 0; i < n; i++)
		{
			for(int j = i+1; j < n; j++)
			{
				if(d[j]>R[i])break;
				R[j] = max(R[j],d[j]+min(d[j]-d[i],l[j]));
			}
			if(R[i] >= D)ok = 1;
		}


		printf("Case #%d: ",++cas);
		puts(ok?"YES":"NO");
	}

	return 0;
}
