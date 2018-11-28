#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#define MP make_pair

using namespace std;
#define EPS 1e-12

int st[1010], ed[1010];

struct Node{
	int st, ed;
	double w;
	bool operator<(const Node &t)const{
		return w < t.w;
	}
}a[1010];
bool vis[1000010];
double w[1000010];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	double x, s, t, r;
	int st, ed;
	double w;
	int n;
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		scanf("%lf%lf%lf%lf%d",&x,&s,&r,&t,&n);
		memset(vis,false,sizeof(vis));
		int top = 0;
		for(int i = 0;i < n; ++i){
			scanf("%d%d%lf",&st,&ed,&w);
			a[i].st = st;
			a[i].ed = ed;
			a[i].w = w;
			for(int j = st + 1;j <= ed; ++j){
				vis[j] = true;
			}
		}
		sort(a , a + n);
		int walk = 0;
		for(int i = 1;i <= x; ++i) if(!vis[i]) walk ++;
		double ans = 0;
		if(r*t >= (double)walk){
			ans += ((double)walk)/r;
			t -= ((double)walk)/r;
		}else{
			ans += t;
			walk -= (r*t);
			t = 0;
			ans += (double)walk/s;
		}
		for(int i = 0;i < n; ++i){
			if(t*(a[i].w + r) >= a[i].ed - a[i].st){
				t -= ((double)(a[i].ed - a[i].st))/(a[i].w + r);
				ans += ((double)(a[i].ed - a[i].st))/(a[i].w + r);
			}else if(t > 0){
				ans += t;
				ans += ((double)(a[i].ed - a[i].st - t*(a[i].w+r)))/(a[i].w + s);
				t = 0;
			}else  ans += ((double)(a[i].ed - a[i].st))/(a[i].w + s);

		}
		printf("Case #%d: ",it);	
		printf("%.12lf\n",ans);
	}
	
}
