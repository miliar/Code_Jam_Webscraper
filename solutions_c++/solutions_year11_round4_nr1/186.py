#include <stdio.h>
#include <algorithm>
#define N 1010
using namespace std;
struct T { double l, v; };
bool operator <(T a, T b) { return a.v<b.v; }
T m[N];
int main()
{
	int ts, t, n, i;
	double l, s, r, h, p;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%lf%lf%lf%lf%d", &l, &s, &r, &h, &n), r-=s, i=0; i<n; scanf("%lf%lf%lf", &p, &m[i].l, &m[i].v), m[i].v+=s, m[i].l-=p, l-=m[i].l, i++);
		m[n].l=l;
		m[n].v=s;
		n++;
		sort(m, m+n);
		for(s=0, i=0; i<n; i++)
			if(m[i].l<1E-7) continue;
			else if(m[i].l/(m[i].v+r)>h) { s+=h+(m[i].l-h*(m[i].v+r))/m[i].v; h=0; }
			else { s+=m[i].l/(m[i].v+r); h-=m[i].l/(m[i].v+r); }
		printf("Case #%d: %.13lf\n", t+1, s);
	}
	return 0;
}