#include <iostream>
using namespace std;
int aa[2300];
int flag[2300];
int cc[15][2200];
int k[15];
int t,p;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("b.out","w",stdout);
	int i,j,ans;
	int kk = 1;
	for(i=0;i<11;i++)
	{
		k[i] = kk;
		kk*=2;
	}
	int cn,cs;
	while(scanf("%d",&t)!=EOF)
	{
		cs = 1;
		while(t--)
		{
			scanf("%d",&p);
			memset(aa,0,sizeof(aa));
			memset(flag,0,sizeof(flag));
			for(i=k[p];i<k[p]*2;i++){
				scanf("%d",&aa[i]);
				aa[i] = p - aa[i];
				}
			for(i=0;i<p;i++)
			{
				for(j=0;j<k[p-1-i];j++)
				{
					scanf("%d",&cc[i][j]);
				}
			}
			cn = p;
			int max1;
			while(cn != 0)
			{
				for(i=k[cn]*2-1;i>=k[cn];i-=2)
				{
					max1 = max(aa[i],aa[i-1]);
					if(max1 >= cn)
					{
						flag[i/2] = 1;
					}
					aa[i/2] = max1;
				}
				cn--;
			}
			ans = 0;
			for(i=0;i<2000;i++)
			{
				if(flag[i]==1)
					ans++;
			}
			printf("Case #%d: %d\n",cs++,ans);
		}
	}
	return 0;
}
