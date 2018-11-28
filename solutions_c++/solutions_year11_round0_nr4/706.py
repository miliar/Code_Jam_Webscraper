#include<iostream>
using namespace std;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int cases,n,V[1024];
	int CP[12];
	CP[1] = 0,CP[2] = 1;
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		scanf("%d",&n);
		bool mark[1024];
		int ans[1024];
		int cnt = 0;
		memset(mark,false,sizeof(mark));
		for(int i=1;i<=n;i++)
			scanf("%d",&V[i]);
		for(int i=1;i<=n;i++)if(!mark[i])
		{
			mark[i] = true;
			int tmp = 1;
			int t = V[i];
			while(!mark[t])
			{
				mark[t] = true;
				tmp++;
				t = V[t];
			}
			if(tmp != 1)
				ans[cnt++] = tmp;
		}
		int sum = 0;
		for(int i=0;i<cnt;i++)
			sum += ans[i];
		printf("Case #%d: %d.000000\n",cas,sum);
	}
}
