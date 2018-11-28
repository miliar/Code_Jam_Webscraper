#include <stdio.h>
#include <math.h>
#define eps (1e-9)
#define pi (3.141592653589793238462)
double f,R,t,r,g;
int N,Case;
double AreaS,AreaC;
struct Tpoint
{
	double x,y;
}	zero;
struct Tsqure
{
	Tpoint dl,dr,ur,ul;
	inline void Up(double x)
	{
		dl.y+=x;
		dr.y+=x;
		ul.y+=x;
		ur.y+=x;
	}
	inline void Right(double x)
	{
		dl.x+=x;
		dr.x+=x;
		ul.x+=x;
		ur.x+=x;
	}
}	s;

inline double sqr(double x)
{
	return x*x;
}

inline double dist(Tpoint& A,Tpoint& B)
{
	return sqrt(sqr(A.x-B.x)+sqr(A.y-B.y));
}

inline double cpt(double x1,double y1,double x2,double y2)
{
	return x1*y2-x2*y1;
}

inline double Area(Tpoint& A,Tpoint& B,Tpoint& C)
{
	return fabs(cpt(B.x-A.x,B.y-A.y,C.x-A.x,C.y-A.y)/2);
}

inline int Sign(double x)
{
	if (fabs(x)<eps) return 0;
	return x>0?1:-1;
}

inline bool intersect(Tpoint A,Tpoint B,Tpoint& inter)
{
	if (!Sign(A.x-B.x))
	{
		if (Sign(dist(A,zero)-R)*Sign(dist(B,zero)-R)>0) return false;
		inter.x=A.x;
		inter.y=sqrt(sqr(R)-sqr(A.x));
		return true;
	}
	else{
		if (Sign(dist(A,zero)-R)*Sign(dist(B,zero)-R)>0) return false;
		inter.y=A.y;
		inter.x=sqrt(sqr(R)-sqr(A.y));
		return true;
	}
}

inline double sector(Tpoint A,Tpoint B)
{
	double res=asin(Area(A,B,zero)/dist(A,zero)/dist(B,zero)*2)/2*sqr(R);
	res-=Area(A,B,zero);
	return res;
}

inline double Get_Area(Tsqure s)
{
	if (dist(s.ur,zero)<R+eps) return g*g;
	if (dist(s.dl,zero)>R-eps) return 0;
	
	double res=0;
	int sign1,sign2;
	Tpoint point1,point2;
	if (intersect(s.dl,s.ul,point1)) sign1=1;
	else intersect(s.ul,s.ur,point1),sign1=2;
	
	if (intersect(s.ur,s.dr,point2)) sign2=3;
	else intersect(s.dr,s.dl,point2),sign2=4;
	
	res+=Area(point1,point2,s.dl);
	if (sign1==2) res+=Area(point1,s.ul,s.dl);
	if (sign2==3) res+=Area(point2,s.dr,s.dl);
	res+=sector(point1,point2);
	
	return res;
}

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	for (scanf("%d",&N);N;N--)
	{
		//readin && ready
		scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
		R-=t+f;
		r+=f;
		g-=f*2;
		AreaS=0;
		AreaC=sqr(R+t+f)*pi/4;
		
		if (g<eps)
		{
			printf("Case #%d: 1.000000\n",++Case);
			continue;
		}
		
		//do
		int x=1,cnt=0;
		s.dl.x=s.dl.y=r;
		s.dr.x=r+g,s.dr.y=r;
		s.ur.x=s.ur.y=r+g;
		s.ul.x=r,s.ul.y=r+g;
		
		Tsqure tmp=s;
		while (dist(tmp.ur,zero)<R+eps)
		{
			++x;
			tmp.Up(2*r+g);
		}
		
		
		for (int i=0;i<=x;++i)
			for (int j=0;j<=x;++j)
			{
				tmp=s;
				tmp.Up((2*r+g)*j);
				tmp.Right((2*r+g)*i);
				AreaS+=Get_Area(tmp);
			}
		
		printf("Case #%d: %.6lf\n",++Case,(AreaC-AreaS)/AreaC);
	}
	
	return 0;
}
