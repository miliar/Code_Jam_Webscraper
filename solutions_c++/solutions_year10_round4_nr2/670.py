#include<iostream>
#include<vector>
using namespace std;
struct
{
	int match;
	int mincost[11];//还需要i张,,最小消耗
}tree[2500];
#define INF 1000000000
int main()
{
	freopen("C:\\Documents and Settings\\Administrator\\桌面\\gcj\\B-small-attempt0.in","r",stdin);
	freopen("C:\\Documents and Settings\\Administrator\\桌面\\gcj\\b.out","w",stdout);
	int cas;
	cin>>cas;
	for(int cs=1;cs<=cas;cs++)
	{
		int p;
		cin>>p;
		for(int i=(1<<p);i;i>>=1)
		{
			for(int j=i;j<2*i;j++)
				cin>>tree[j].match;
		}
		for(int i=(1<<p);i<2*(1<<p);i++)
		{
			int nd=p-tree[i].match;
			if(nd<0)nd=0;
			for(int k=0;k<nd;k++)tree[i].mincost[k]=INF;
			for(int k=nd;k<=p;k++)tree[i].mincost[k]=0;
		}
		for(int i=(1<<p)/2;i;i>>=1)
		{
			for(int j=i;j<2*i;j++)
			{
				int s1=j*2,s2=j*2+1;
				for(int k=0;k<=p;k++)
				{
					if(tree[s1].mincost[k]!=INF&&tree[s2].mincost[k]!=INF)
						tree[j].mincost[k]=tree[s1].mincost[k]+tree[s2].mincost[k];
					else
						tree[j].mincost[k]=INF;
				}
				
				int cost=tree[j].match;
				for(int k=1;k<=p;k++)
				{
					if(tree[j].mincost[k]!=INF)
					{
						int nc=tree[j].mincost[k]+cost;
						if(nc<tree[j].mincost[k-1])
							tree[j].mincost[k-1]=nc;
					}
				}
			}
		}
		cout<<"Case #"<<cs<<": ";
		cout<<tree[1].mincost[0]<<"\n";
	}
}