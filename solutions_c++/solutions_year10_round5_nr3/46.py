#include <cstdio>
#include <cstring>
#include <map>
using namespace std;

int q[10000000];
map <int,int >hash;
map <int,bool>in;
int n;

int main()
{
	freopen("C_small.in","r",stdin);
	freopen("C_small.out","w",stdout);
	
	int T,test=1;
	for (scanf("%d",&T);test<=T;++test)
	{
		hash.clear();
		in.clear();
		scanf("%d",&n);
		int h=0,tail=0;
		for (int i=0;i<n;++i)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			hash[a]=b;
			if (b>1 && !in[a])
			{
				q[tail++]=a;
				in[a]=true;
			}
		}
		int Ans=0;
		for (;h<tail;++h)
		{
			int u=q[h];
			while (hash[u]>1)
			{
				++hash[u+1];
				++hash[u-1];
				hash[u]-=2;
				if (hash[u+1]>1 && !in[u+1])
				{
					q[tail++]=u+1;
					in[u+1]=true;
				}
				
				if (hash[u-1]>1 && !in[u-1])
				{
					q[tail++]=u-1;
					in[u-1]=true;
				}
				++Ans;
			}
			in[u]=false;
		}
		
		printf("Case #%d: %d\n",test,Ans);
	}
	return 0;
}
