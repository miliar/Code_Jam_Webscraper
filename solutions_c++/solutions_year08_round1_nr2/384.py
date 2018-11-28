#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main()
{
	int C,c;
	cin>>C;
	for(c=1;c<=C;c++)
	{
		int N,M,i,j,d,T;
		vector<int> z[2000][2];
		cin>>N;
		cin>>M;
		for(i=0;i<M;i++)
		{
			cin>>T;
			for(j=0;j<T;j++)
			{
				int x,y;
				cin>>x>>y;
				z[x-1][y].push_back(i);
			}
		}
		int mini=3000,n_min=-1;
		for(i=0;i<1<<N;i++)
		{
			int was[2000]={0},k;
			int on=0;
			d=0;
			for(j=0;j<N;j++)
			{
				int r;
				if((i&(1<<j))==0)r=0;
				else r=1;
				on+=r;
				for(k=0;k<z[j][r].size();k++)
				{
					if(was[z[j][r][k]]==0)d++;
					was[z[j][r][k]]=1;
				}
			}
			if((d==M)&&(mini>on))
			{
				mini=on;
				n_min=i;
			}
		}
		if(n_min==-1)
		{
			printf("Case #%d: IMPOSSIBLE\n",c);
		}
		else
		{
			printf("Case #%d:",c);
			for(j=0;j<N;j++)
			{
				printf(" %d",(n_min&(1<<j))==0?0:1);
			}
			printf("\n");
		}
	}
	return 0;
}