#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#define maxn 1001
using namespace std;
int vis[maxn];
long long g[maxn],now,cnt,r,k,n;
long long  re,tempnow,tim,a[maxn];
long long res;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	cin>>tim;
	for(int tt=1;tt<=tim;tt++)
	{
		cin>>r>>k>>n;
		for(int i=0;i<n;i++)
			cin>>g[i];
		memset(vis,0,sizeof(vis));
		now=0,res=0,cnt=0;
		while(!vis[now]&&r>0)
		{
			vis[now]=++cnt;
			a[now]=res;
			tempnow=now;
			re=0;
			while((now!=tempnow||re==0)&&re+g[now]<=k)	
				re+=g[now],now=(now+1)%n;
			res+=re;
			--r;
		}
		long long temp=res-a[now];
		cnt=cnt-vis[now]+1;
		res+=temp*(r/cnt);
		r%=cnt;
		memset(vis,0,sizeof(vis));
		while(r>0)
		{
			tempnow=now;
			re=0;
			while((now!=tempnow||re==0)&&re+g[now]<=k)	
				re+=g[now],now=(now+1)%n;
			res+=re;
			--r,cnt++;
		}
		printf("Case #%d: ",tt);
		cout<<res<<'\n';
	}
	return 0;
}

