#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
int main()
{
	int num[10];
	int t;
	freopen("G:\\C-small-attempt0.in","r",stdin);
	freopen("G:\\C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	bool fl[110];
	for(int cas=1;cas<=t;++cas)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<m;++i)
			scanf("%d",&num[i]);
		sort(num,num+m);
		int Min=INT_MAX;
		do 
		{
			memset(fl,0,sizeof(fl));
			int res=0;
			for(int i=0;i<m;++i)
			{
				int t=num[i];
				for(int j=t+1;j<=n;++j)
				{
					if(fl[j]==1)
						break;
					res++;
				}
				for(int j=t-1;j>=1;--j)
				{
					if(fl[j]==1)
						break;
					res++;
				}
				fl[t]=1;
				
			}
			if(res<Min)
				Min=res;
		}while (next_permutation(num,num+m));
		printf("Case #%d: %d\n",cas,Min);

	}
}