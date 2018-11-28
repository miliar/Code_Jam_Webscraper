#include <cstdio>
#include <cstring>
#include <cstdlib>

#define Max(a,b) (((a)>(b))?(a):(b))
#define Min(a,b) (((a)<(b))?(a):(b))

typedef double TYPE;

struct POINT
{
    TYPE x;
    TYPE y;
    TYPE z;
    POINT() : x(0), y(0), z(0) {};
    POINT(TYPE _x_, TYPE _y_, TYPE _z_ = 0) : x(_x_), y(_y_), z(_z_) {};
};

struct SEG
{
    POINT a;
    POINT b;
    SEG() {};
    SEG(POINT _a_, POINT _b_):a(_a_),b(_b_) {};
};

TYPE Cross(const POINT & a, const POINT & b, const POINT & o)
{
    return (a.x - o.x) * (b.y - o.y) - (b.x - o.x) * (a.y - o.y);
}

bool IsIntersect(const SEG & u, const SEG & v)
{
    return (Cross(v.a, u.b, u.a) * Cross(u.b, v.b, u.a) >= 0) &&
        (Cross(u.a, v.b, v.a) * Cross(v.b, u.b, v.a) >= 0) &&
        (Max(u.a.x, u.b.x) >= Min(v.a.x, v.b.x)) && 
        (Max(v.a.x, v.b.x) >= Min(u.a.x, u.b.x)) && 
        (Max(u.a.y, u.b.y) >= Min(v.a.y, v.b.y)) && 
        (Max(v.a.y, v.b.y) >= Min(u.a.y, u.b.y));
}

SEG xduan[20000];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int Cases, count, i, j, p1, p2, sum;
	scanf("%d", &Cases);

    int case1=1;
	while(Cases--)
	{
		sum=0;
		scanf("%d",&count);
		for (i=0;i<count;i++)
		{
			scanf("%d %d", &p1, &p2);
			xduan[i].a.x=0;
			xduan[i].a.y=p1;
			xduan[i].b.x=1;
			xduan[i].b.y=p2;
		}
		for (i=0;i<count;i++)
		{
			for (j=0;j<i;j++)
			{
				if (IsIntersect(xduan[i], xduan[j]))
				{
					sum++;
				}
			}
		}
		printf("Case #%d: %d\n", case1, sum);
		case1++;
	}

	return 0;
}