#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#define MAXN 1010
using namespace std;

int g[MAXN],r,k,n,next[MAXN],values[MAXN],q[MAXN];
bool flag[MAXN];

int main()
{
#ifndef ONLINE_JUDGE
//	freopen("in.txt","r",stdin);
//	freopen("google_2.txt","w",stdout);
#endif

	int dataset;
	scanf("%d",&dataset);
	for(int cas=1;cas<=dataset;++cas)
	{
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;++i)
		{
			scanf("%d",g+i);
			flag[i]=false;
		}
		memset(next,-1,sizeof(next));
		int cur=0,p=0,tot=0;
		while(true)
		{
			if(next[cur]!=-1)
				break;
			tot=0;
			while(tot+g[p]<=k)
			{
				tot+=g[p];
				if(p==(cur+n-1)%n)
				{
					p=(p+1)%n;
					break;
				}
				p=(p+1)%n;
			}
			values[cur]=tot;
			next[cur]=p;
//			cout<<cur<<"\t"<<next[cur]<<"\t"<<values[cur]<<endl;
			cur=p;
		}
		printf("Case #%d: ",cas);
		int key=0,cyc=0,front=0;
		cur=0;
		while(r--)
		{
			key+=values[cur];
				q[front++]=cur;
				cur=next[cur];
//			cout<<r<<"\t"<<key<<endl;
		}
		printf("%d\n",key);
	}

	return 0;
}
