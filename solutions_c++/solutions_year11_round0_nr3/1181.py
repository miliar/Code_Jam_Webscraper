#include <cstdio>
#include <map>
using namespace std;

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int Test=1;Test<=T;Test++)
	{
		int N;
		scanf("%d",&N);
		int a[1005];
		int sum=0,tot=0;
		map<int,int> d[1005];
		for(int i=1;i<=N;i++)
		{
			scanf("%d",a+i);
			sum^=a[i];
			tot+=a[i];
		}
		d[0][0]=0;
		for(int i=0;i<N;i++)
		{
			for(map<int,int>::iterator it=d[i].begin();it!=d[i].end();it++)
			{
				int j=(it->first),k=it->second+a[i+1];
				if (d[i+1][j]<k)
					d[i+1][j]=k;
				j=(it->first^a[i+1]),k=it->second;
				if (d[i+1][j]<k)
					d[i+1][j]=k;
			}
		}
		int re=0;
		for(map<int,int>::iterator it=d[N].begin();it!=d[N].end();it++)
			if ((it->first^sum)==it->first && it->second>re)
				re=it->second;
		printf("Case #%d: ",Test);
		if (re==0)
			printf("NO\n");
		else if (re!=tot)
			printf("%d\n",re);	
		else
		{
			for(int i=0;i<=N;i++)
				d[i].clear();
			d[0][0]=0;
			int ans=0;
			for(int fbd=1;fbd<=N;fbd++)
			{
				for(int i=0;i<N;i++)
				{
					for(map<int,int>::iterator it=d[i].begin();it!=d[i].end();it++)
					{
						int j=it->first,k=it->second+a[i+1];
						if ((i+1)!=fbd)
							if (d[i+1][j]<k)
								d[i+1][j]=k;
						j=(it->first^a[i+1]),k=it->second;
						if (d[i+1][j]<k)
							d[i+1][j]=k;
					}
				}
				int re=0;
				for(map<int,int>::iterator it=d[N].begin();it!=d[N].end();it++)
					if ((it->first^sum)==it->first && it->second>re)
						re=it->second;
				if (re!=0)
				{
					if (re>ans)
						ans=re;
				}
			}
			if (ans!=0) printf("%d\n",ans);
			else printf("NO\n");
		}
	}
	return 0;
}
