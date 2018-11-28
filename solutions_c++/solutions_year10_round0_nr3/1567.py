#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int r,k,n;
int a[1010],vis[1010],next[1010],v[1010];
long long sv[1010];

int succ(int now) {
	return (now==n)?(1):(now+1);
}

int get_next(int now,int &w) {
	w=0;
	int sum=0;
	while (1) {
		if (sum+a[now]<=k) {
			sum+=a[now];
			now=succ(now);
		} else {
			w=sum;
			return now;
		}
	}
}

int main() {
	int c=0,cc;
	for (scanf("%d",&cc);c<cc;c++) {
		scanf("%d%d%d",&r,&k,&n);
		long long sa=0;
		for (int i=1;i<=n;i++) {
			scanf("%d",&a[i]);
			sa+=a[i];
		}
//		cout<<sa<<" "<<r<<" "<<k<<endl;
		if (sa<=k) {
			cout<<"Case #"<<c+1<<": "<<sa*r<<endl;
			continue;
		}
		memset(vis,-1,sizeof(vis));
		memset(next,0,sizeof(next));
		memset(v,0,sizeof(v));
		memset(sv,0,sizeof(sv));
		int now=1,w=0,t=0,x;
		vis[now]=0;
		long long ans=0;
		while (1) {
			x=get_next(now,w);
			t++;r--;
			ans=ans+w;
			if (vis[x]!=-1) break;
			v[x]=w;
			sv[x]=sv[now]+v[x];
			vis[x]=t;
			next[now]=x;
			now=x;
			if (r==0) break;
		}
		if (r!=0) {
			int cl=t-vis[x];
			int nc=r/cl;
			r=r%cl;
			ans=ans+(long long)nc*(ans-sv[x]);
		}
		while (r-->0) {
			x=next[x];
			ans=ans+v[x];
		}
		cout<<"Case #"<<c+1<<": "<<ans<<endl;
	}
}
