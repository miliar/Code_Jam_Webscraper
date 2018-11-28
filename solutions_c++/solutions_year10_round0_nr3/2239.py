#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<algorithm>
using namespace std;

int T,R,k,N;
int num,Case=1;
int Q[1010],p;
queue<int> q;

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("aaa.txt","w",stdout);
	int i;
	scanf("%d",&T);
	for(;T>0;T--)
	{
		while(!q.empty()) q.pop();
		scanf("%d%d%d",&R,&k,&N);	
		for(i=0;i<N;i++)
		{
			scanf("%d",&num);
			q.push(num);
		}
		int Count,ans=0;
		for(i=0;i<R;i++)
		{
			Count=0,p=0;
			while(q.size() && Count+q.front()<=k)
			{
				int v=q.front();
				q.pop();
				Q[p++]=v;
				Count+=v;
			}
			ans+=Count;
			for(int j=0;j<p;j++) q.push(Q[j]);
		}
		printf("Case #%d: %d\n",Case++,ans);
	}
	return 0;
}	
