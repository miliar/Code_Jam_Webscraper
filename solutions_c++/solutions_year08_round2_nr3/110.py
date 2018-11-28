#include<iostream>
#include<vector>
using namespace std;
int b[10000],ans[10000];
vector<int>v;
int main()
{
//	freopen("C-small-attempt0.in","r",stdin);
//	freopen("C-small.out","w",stdout);
	int cas,test=1,A,B,n,i,j,k,t,sum,id;
	scanf("%d",&cas);
	while(cas--)
	{
		memset(b,0,sizeof(b));
		scanf("%d%d",&k,&n);
		id=1;
		for(i=1;i<=k;i++)
		{
			int num=i;
			while(num)
			{
				if(b[id]==0)
				{
					num--;
				}
				if(num==0)
				{
					b[id]=1;
					 ans[id]=i;
				}
				id=(id+1);
				if(id==k+1) id=1;
			}
		}
		printf("Case #%d:",test++);
		for(i=0;i<n;i++)
		{
			scanf("%d",&t);
			printf(" %d",ans[t]);
		}
		printf("\n");
	}
	return 0;
}