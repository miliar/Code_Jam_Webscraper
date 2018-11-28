#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
	freopen("A.in","rt",stdin);
	freopen("out.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d",&n);
		vector<pair<int,int>> p(n);
		queue<int> O;
		queue<int> B;
		for(int j=0;j<n;j++)
		{
			int b;
			char a;
			scanf("%c",&a);
			scanf("%c%d",&a,&b);
			if(a=='O')
			{
				a=1;
				O.push(j);
			}
			else
			{
				a=2;
				B.push(j);
			}
			p[j]=make_pair(a,b);
		}
		int res=0;
		int g[]={0,1,1};
		for(int j=0;j<n;j++)
		{
			while(g[p[j].first]!=p[j].second)
			{
				if(!O.empty())
				if(g[1]>p[O.front()].second)
					g[1]--;
				else
					if(g[1]<p[O.front()].second)
						g[1]++;
				if(!B.empty())
				if(g[2]>p[B.front()].second)
					g[2]--;
				else
					if(g[2]<p[B.front()].second)
						g[2]++;
				res++;
			}
			res++;
			if(p[j].first==1)
			{
				if(!B.empty())
				if(g[2]>p[B.front()].second)
					g[2]--;
				else
					if(g[2]<p[B.front()].second)
						g[2]++;
				O.pop();
			}
			else
			{
				if(!O.empty())
				if(g[1]>p[O.front()].second)
					g[1]--;
				else
					if(g[1]<p[O.front()].second)
						g[1]++;
				B.pop();
			}
		}
		printf("Case #%d: %d\n",i,res);
	}
	fclose(stdout);
}