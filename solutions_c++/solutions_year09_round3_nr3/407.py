#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
int n,m;
int r[1000];
int a[100];
bool has[1000];
int solve(int pos)
{
	int i,j;
	int res=0;
	for(i=pos+1;i<=n&&has[i];i++)
	{
		res++;
	}
	for(i=pos-1;i>=1&&has[i];i--)
		res++;
	return res;
}
int main()
{
	freopen("f.in","r",stdin);
	freopen("f.out","w",stdout);
	int i,j;
	int T;
	int case_cnt=1;
	scanf("%d",&T);
	while(T--)
	{
		memset(has,0,sizeof(has));
		//case_cnt++;
		scanf("%d%d",&n,&m);
		for(i=1;i<=m;i++)
			scanf("%d",&r[i]);
		printf("Case #%d: ",case_cnt++);
		//search(1,0);
		int res=999999999;
		do
		{
			for(i=1;i<=n;i++)
				has[i]=1;
			int temp=0;
			for(i=1;i<=m;i++)
			{
				temp+=solve(r[i]);
				has[r[i]]=0;
			}
			if(temp<res)
				res=temp;
		}
		while(std::next_permutation(r+1,r+1+m));
		printf("%d\n",res);
	}
}