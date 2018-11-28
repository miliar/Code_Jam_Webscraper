#include<iostream>
using namespace std;
const int MAXN = 1500;
struct point
{
    int x,y;
};
struct line
{
    point a,b;
}a[MAXN];
inline int sign(int x)
{
    return x > 0 ? 1 : (x < 0 ? -1 : 0);
}

inline int xmult(point p1,point p2,point p0)
{
	return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y);
}

inline int dot_online_in(point p,line l)
{
	return !xmult(p,l.a,l.b)&&(l.a.x-p.x)*(l.b.x-p.x)<=0&&(l.a.y-p.y)*(l.b.y-p.y)<=0;
}

inline int dots_inline(point p1,point p2,point p3)
{
	return !xmult(p1,p2,p3);
}

inline int same_side(point p1,point p2,line l)
{
	return sign(xmult(l.a,p1,l.b))*xmult(l.a,p2,l.b)>0;
}

inline int intersect_in(line u,line v)
{
	if (!dots_inline(u.a,u.b,v.a)||!dots_inline(u.a,u.b,v.b))
		return !same_side(u.a,u.b,v)&&!same_side(v.a,v.b,u);
	return dot_online_in(u.a,v)||dot_online_in(u.b,v)||dot_online_in(v.a,u)||dot_online_in(v.b,u);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int cas,n;
    scanf("%d",&cas);
	for (int T = 1;T <= cas;T++)
	{
        scanf("%d",&n);
		for (int i = 0;i < n;i++)
        {
            scanf("%d%d",&a[i].a.x,&a[i].b.x);
            a[i].a.y = 1;
            a[i].b.y = 10;
        }
		int ans = 0;
		for (int i = 0;i < n;i++)
			for(int j = i + 1;j < n;j++)
				ans += intersect_in(a[i],a[j]);
		printf("Case #%d: %d\n",T,ans);
	}
}
