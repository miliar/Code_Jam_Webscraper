#include <iostream>
#include <map>
using namespace std;
const int maxn = 10000;
int d[maxn],len[maxn];
int f[maxn];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	int runs;
	scanf("%d",&T);
	for (runs = 1;runs<=T;runs++)
	{
		int n;
		scanf("%d",&n);
		int i;
		for (i = 0; i<n; i++)
			scanf("%d%d",d+i,len+i);
		int D;
		scanf("%d",&D);
		f[0]=d[0];
		for (i=1;i<n;i++)
		{
			int j;
			int minj = -1;
			for (j=0;j<i;j++)
				if (f[j]+d[j]>=d[i])
				{
					minj=d[j];
					break;
				}
			if (minj ==-1)
				f[i]=0;
			else
				f[i]=d[i]-minj;
			if (f[i]>len[i])
				f[i]=len[i];
	//		cout<<f[i]<<' ';
		}
		bool yes = false;
		for (i=0;i<n;i++)
			if (f[i]+d[i]>=D)
				yes=true;
		printf("Case #%d: ",runs);
		if (yes)
			puts("YES");
		else
			puts("NO");
	}
	return 0;
}
