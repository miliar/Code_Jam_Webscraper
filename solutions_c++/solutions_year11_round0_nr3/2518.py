#include<iostream>
using namespace std;
const int ma=1048576;
int all,ans,f[2][2000000],times,n,num[1001],tma;
void mem()
{
	all=0;
	memset(f,0,sizeof(f));
	f[0][0]=0;
	ans=0;
	tma=ma;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d",&n);
		mem();
		for (int a=1;a<=n;++a) 
		{
			
			scanf("%d",&num[a]);
			all^=num[a];
			ans+=num[a];
			tma=min(tma,num[a]);
		}
		if (all) 
		{
			printf("Case #%d: NO\n",z);
			continue;
		}
		printf("Case #%d: %d\n",z,ans-tma);
	}
}
