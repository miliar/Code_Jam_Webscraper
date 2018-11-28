#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define maxn 2005

int g[maxn],n,vis[maxn],R,Limit;
long long S[maxn],Ans[maxn],Key[maxn];

int main()
{
	freopen("C_large.in","r",stdin);
	freopen("C_large.out","w",stdout);
	
	int test=1,T;
	for (scanf("%d",&T);test<=T;++test)
	{
		scanf("%d%d%d",&R,&Limit,&n);
		for (int i=1;i<=n;++i)
		{
			scanf("%d",&g[i]);
			g[i+n]=g[i];
		}
		for (int i=1;i<=2*n;++i)
			S[i]=S[i-1]+g[i];
		
		int cur=1,N=0;
		memset(vis,0,sizeof(vis));
		while (!vis[cur])
		{
			++N;
			vis[cur]=N;
			int j=cur;
			while (j-cur<n && S[j]-S[cur-1]<=Limit)
				++j;
			Key[N]=S[j-1]-S[cur-1];
			Ans[N]=Ans[N-1]+Key[N];
			cur=j;
			if (cur>n) cur-=n;
		}
		int r=vis[cur]-1;
		long long out=0;
		if (r>R)
		{
			out=Ans[R];
		}else
		{
			out=Ans[r];
			int len=N-r;
			out+=(Ans[N]-Ans[r])*((R-r)/len);
			int t=(R-r)%len;
			for (int i=0;i<t;++i)
				out+=Key[r+1+i];
		}
		
		printf("Case #%d: %I64d\n",test,out);
	}
	
	return 0;
}
