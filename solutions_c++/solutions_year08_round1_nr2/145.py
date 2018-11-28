#include <stdio.h>

int ind[2001];
int like[2001][2001];
int melt[2001];
int set[2001];

int main()
{
	int x,y,i,j,sat;
	int tmp;
	int n,m;
	int cas,asd;
	int no;
//	freopen("b.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d",&n);
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			melt[i] = -1;
			tmp=0;
			scanf("%d",&ind[i]);
			for(j=0;j<ind[i];j++)
			{
				scanf("%d %d",&x,&y);
				x--;
				if(y==0)
					like[i][tmp++] = x;
				else
					melt[i] = x;
			}
			ind[i]=tmp;
		}
		for(i=0;i<n;i++)
			set[i]=0;
		no=0;
		while(1)
		{
			for(i=0;i<m;i++)
			{
				if(melt[i]==-1)
					continue;

				sat=0;
				for(j=0;j<ind[i];j++)
				{
					if(set[like[i][j]]==0)
					{
						sat=1;
						break;
					}
				}
				if(sat==0 && set[melt[i]] == 0)
				{
					set[melt[i]]=1;
					break;
				}
			}
			if(i==m)
				break;
			for(i=0;i<m;i++)
			{
				for(j=0;j<ind[i];j++)
				{
					if(set[like[i][j]] == 0)
						break;
				}
				if(j==ind[i] && melt[i]==-1)
				{
					no=1;
					break;
				}
			}
			if(no)
				break;
		}
		printf("Case #%d:",asd+1);
		if(no)
			printf(" IMPOSSIBLE\n");
		else
		{
			for(i=0;i<n;i++)
				printf(" %d",set[i]);
			printf("\n");
		}
	}
	return 0;
}