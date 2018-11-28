#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int T,x,s,r,n,b[1001],e[1001],i,wl;
	pair<int,int> len[1008];
	double time,t,ans,left;
	freopen("a2.in","r",stdin);
	freopen("a2.out","w",stdout);
	scanf("%d",&T);
	for (int cas=1; cas<=T; cas++)
	{
		scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
		wl = x;
		for (i=0; i<n; i++)
		{
			scanf("%d%d%d",&b[i],&e[i],&len[i].first);
			wl -= e[i]-b[i];
			len[i].second = e[i]-b[i];
			len[i].first += s;
		}
		len[n].first = s;
		len[n].second = wl;
		sort(len,len+n+1);
		r -= s;
		ans = 0.0;
		for (i=0; i<=n; i++)
		{
			time = len[i].second / (double)(r+len[i].first);
			if (time < t+1e-10) {
				t -= time;
				ans += time;
			} else {
				left = len[i].second - (r+len[i].first)*t;
				ans += t;
				ans += left/len[i].first;
				break;
			}
		}
		for (i++; i<=n; i++) ans += len[i].second / (double)len[i].first;
		printf("Case #%d: %.8lf\n",cas,ans);
	}
	return 0;
}

