#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
int N,K;
int Dt[120][55];
int isLarge(int a,int b)
{				
		for (int q=0;q<K;++q)
			if (Dt[a][q]<=Dt[b][q])
					return 0;
		return 1;
}
int From[120],Outer[120],Idx[120];
int Dir[120][120],Visit[120];
int findway(int u)
{
		if (Visit[u]) return 0; 
		Visit[u]=1;
		for (int q=0;q<N;++q)
				if (Dir[u][q])
				{
						if (From[q]<0)
						{
								From[q]=u;
								return 1;
						}
						Visit[q]=1;
						int w=From[q];
						if (findway(w)) 
						{
								From[q]=u;
								return 1;
						}
				}
		return 0;
}
int main()
{
		int T;
		scanf("%d",&T);
		for (int kase=1;kase<=T;++kase)
		{
				scanf("%d %d",&N,&K);
				for (int q=0;q<N;++q) for (int w=0;w<K;++w)
						scanf("%d",&Dt[q][w]);
				for (int q=0;q<N;++q)
				{
						From[q]=-1;
						Idx[q]=q;
						Outer[q]=0;
						for (int w=0;w<N;++w)
						{
								Dir[q][w]= (isLarge(q,w));
								if (Dir[q][w]) Outer[q]++;
						}
				}
				queue<int> Q;
				for (int q=0;q<N;++q)
						if (!Outer[q])
								Q.push(q);
				int ret=0;
				while (!Q.empty())
				{
						int i=Q.front(); Q.pop();
						//release visit
						for (int q=0;q<N;++q)
								Visit[q]=0;
						//find way
						if (!findway(i)) ret++;
						//order
						for (int q=0;q<N;++q)
								if (Dir[q][i])
								{
										Outer[q]--;
										if (!Outer[q]) Q.push(q);
								}
				}
				printf("Case #%d: %d\n",kase,ret);
		}
		return 0;
}
