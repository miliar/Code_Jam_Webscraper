#include <cstdio>
#include <cstring>

int g[1024];
__int64 e[1024];
int flag[1024];

void work()
{
	int T,R,K,N;
	int cas,p,i,j,k,boa;
	__int64 earn;
	
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&R,&K,&N);
		for (i=0;i<N;i++)
			scanf("%d",&g[i]);
		earn=0;
		
		memset(e,0,sizeof(e));
		memset(flag,0,sizeof(flag));
		p=0;
		for (i=1;i<=R && flag[p]==0;i++)
		{
			flag[p]=i;
			j=p;
			boa=0;
			k=0;
			while (boa<=K && k<N)
			{
				if (boa+g[j]>K)
					break;
				boa+=g[j];
				j=(j+1)%N;
				k++;
			}
			p=j;	
			earn+=boa;
			e[i]=earn;
		}
		
		if (i<=R)
		{
			__int64 CR,YS;
			CR=(R+1-flag[p])/(i-flag[p]);
			YS=(R+1-flag[p])%(i-flag[p]);
			earn=e[flag[p]-1]+ (e[i-1]-e[flag[p]-1])*CR + (e[flag[p]+YS-1]-e[flag[p]-1]);
		}	
		printf("Case #%d: %I64d\n",cas,earn);
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	work();

	
	return 0;
}
