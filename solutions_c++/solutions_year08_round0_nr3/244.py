#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define LD double

const LD eps = 1e-11;
const LD pi = 2*acos(0.0);

template <class _T>

inline void swap(_T &a,_T &b)
{
	_T c;c=a;a=b;b=c;
}

struct point
{
	LD x,y;
	point(){}
	point(LD xx,LD yy)
	{
		x=xx,y=yy;
	}
};

int cases,caseno;
LD fly,R,th,r,gap,ar,area;

struct Point
{
	LD x,y;
};

bool findArea()
{
	if(fly*2+eps>gap) return true;
	ar=(gap-2*fly)*(gap-2*fly);
	return false;
}

inline LD distance(point a,point b)
{
	return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));
}

inline LD sq_dis(LD x1,LD y1,LD x2,LD y2)
{
	return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
}

inline LD findTriangle(point A,point B,point C)
{
	LD a,b,c,s;

	a=distance(B,C);
	b=distance(A,C);
	c=distance(A,B);

	s=(a+b+c)/2;
	return sqrt(s*(s-a)*(s-b)*(s-c));
}

inline LD findArea(point A,point B,point C)
{
	LD a,b,c;
	point D;

	D=point(0,0);
	a=distance(A,B);
	b=distance(B,D);
	c=distance(A,D);

	return (R-fly)*(R-fly)*acos((b*b+c*c-a*a)/(2*b*c))/2 - findTriangle(A,B,D) + findTriangle(A,B,C);
}

bool collides(LD x1,LD y1,LD x2,LD y2)
{
	if(x2*x2+y2*y2 > R*R + eps)
	{
		x1+=fly;
		x2-=fly;
		y1+=fly;
		y2-=fly;

		LD x11,y11,x22,y22,K;

		K=R-fly;
		K*=K;
		if(K<x1*x1) return true;
		if(K<y1*y1) return true;
		x11=sqrt(K-x1*x1);
		y11=sqrt(K-y1*y1);

		if(x11<y1+eps) return true;
		if(y11<x1+eps) return true;

		if(y11 > x2+eps)
		{
			if(x11 > y2+eps)
			{
				x22=sqrt(K-x2*x2);
				y22=sqrt(K-y2*y2);

				area+=findArea(point(y22,y2),point(x2,x22),point(y22,x22));
				area+=(y2-y1)*(y22-x1)+(x2-y22)*(x22-y1);
			}
			else
			{
				x22=sqrt(K-x2*x2);
				area+=(x2-x1)*(x22-y1);
				area+=findArea(point(x1,x11),point(x2,x22),point(x1,x22));
			}
		}
		else
		{
			if(x11 > y2+eps)
			{
				y22=sqrt(K-y2*y2);
				area+=(y2-y1)*(y22-x1);
				area+=findArea(point(y11,y1),point(y22,y2),point(y22,y1));
			}
			else
				area+=findArea(point(x1,x11),point(y11,y1),point(x1,y1));
		}
		return true;
	}
	area+=ar;
	return false;
}

void process()
{
	printf("Case #%d:",++caseno);
	if(findArea() || r+eps>R-th)
	{
		puts(" 1.000000");
		return;
	}
	LD x1,y1,K,A;
	bool flag;
	int cnt=0;

	K=gap+2*r;
	area=0;
	R-=th;
	for(x1=r;;x1+=K)
	{
		flag=false;
		for(y1=r;;y1+=K)
		{
			cnt++;
			collides(x1,y1,x1+gap,y1+gap);
			if(x1*x1+y1*y1 > R*R + eps) break;
			flag=true;
		}
		if(!flag) break;
	}
	R+=th;
	A=pi*R*R/4;
	area=A-area;
	area/=A;
	printf(" %lf\n",area+eps);
}

int main()
{
	//freopen("Inputs\\C-large.in","r",stdin);
	//freopen("Inputs\\C1.ans","w",stdout);

	scanf("%d",&cases);
	while(cases--)
	{
		scanf("%lf %lf %lf %lf %lf",&fly,&R,&th,&r,&gap);
		process();
	}
	return 0;
}