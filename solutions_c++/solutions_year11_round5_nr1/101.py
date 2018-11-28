#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

const double eps = 1e-10;

struct tdot
{
	double x,y;
}u[110],l[110],b[110];

int T,test,n,W,U,L,G,A,B;
double s;
double ans[110];

double get(tdot a[], int n, double l, double r)
{
	//printf("a: "); for (int i=1;i<=n;i++) printf("(%.2lf,%.2lf), ",a[i].x,a[i].y); printf("\n");
	//printf("l=%lf r=%lf\n",l,r);
	int p,q;
	for (p=2;p<=n;p++) if (a[p].x > l - eps) break;
	for (q=n-1;q>=1;q--) if (a[q].x < r + eps) break;
	//debug(p); debug(q);
	b[1].x = l;
	b[1].y = a[p-1].y + (a[p].y-a[p-1].y)/(a[p].x-a[p-1].x)*(l-a[p-1].x);
	B=1;
	for (int i=p;i<=q;i++) b[++B] = a[i];
	B++;
	b[B].x = r;
	b[B].y = a[q].y + (a[q+1].y-a[q].y)/(a[q+1].x-a[q].x)*(r-a[q].x);
	double ret = 0;
	//printf("b: "); for (int i=1;i<=B;i++) printf("(%.2lf,%.2lf), ",b[i].x,b[i].y); printf("\n");
	for (int i=2;i<=B;i++)
		ret += (b[i-1].y+b[i].y)/2.0*(b[i].x-b[i-1].x);
	//debug(ret);
	return ret;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> W >> L >> U >> G;
		for (int i=1;i<=L;i++) cin >> l[i].x >> l[i].y;
		for (int i=1;i<=U;i++) cin >> u[i].x >> u[i].y;
		s = 0;
		for (int i=2;i<=L;i++) s -= (l[i-1].y+l[i].y)/2.0*(l[i].x-l[i-1].x);
		for (int i=2;i<=U;i++) s += (u[i-1].y+u[i].y)/2.0*(u[i].x-u[i-1].x);
		s /= double(G);
		//debug(s);
		ans[0] = 0;
		for (int i=1;i<=G;i++)
		{
			double left = ans[i-1], right = W, mid;
			while (left + 1e-10 < right)
			{
				mid = (left + right) / 2.0;
				//debug(mid);
				double now = get(u,U,ans[i-1],mid) - get(l,L,ans[i-1],mid);
				//debug(now);
				//break;
				if (now>s) right = mid;
				else left = mid;
			}
			ans[i] = left;
		}
		printf("Case #%d:\n",test);
		for (int i=1;i<G;i++) printf("%.6lf\n",ans[i]);
	}
	
	return 0;
}
