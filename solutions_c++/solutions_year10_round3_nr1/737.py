#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;
double eps=1e-7;
//### STRUCT PUNTO Y OPERADORES  #######################################################
struct Point
{
	double x, y;
	Point()
	{
	}
	Point(double a, double b)
	{
		x = a;
		y = b;
	}
	void show()
	{
		printf("P = (x, y) = (%.2lf, %.2lf)\n", x, y);
	}
};

Point operator +(Point a, Point b)
{
	return Point(a.x + b.x, a.y + b.y);
}
Point operator /(Point a, double n)
{
	return Point(a.x/n, a.y/n);
}
Point operator *(Point a, double n)
{
	return Point(a.x*n, a.y*n);
}
bool operator ==(Point a, Point b)
{
	return fabs(a.x-b.x)<eps && fabs(a.y-b.y)<eps;
}
bool operator !=(Point a, Point b)
{
	return !(a==b);
}
bool operator <(Point a, Point b)
{
	if(a.x != b.x) return a.x < b.x;
	return a.y < b.y;
}

//### STRUCT VECTOR Y OPERADORES  ######################################################
struct Vector
{
	double m, n;
	Vector()
	{
	}
	Vector(double a, double b)
	{
		m = a;
		n = b;
	}
	double mod()
	{
		return sqrt(m*m + n*n);
	}
	Vector ort()
	{
		return Vector(-n, m);
	}
	void show()
	{
		printf("V = (m, n) = (%.2lf, %.2lf)\n", m, n);
	}
};

Vector operator +(Vector a, Vector b)
{
	return Vector(a.m + b.m, a.n + b.n);
}
Vector operator -(Vector a, Vector b)
{
	return Vector(a.m - b.m, a.n - b.n);
}
Vector operator /(Vector a, double n)
{
	return Vector(a.m/n, a.n/n);
}
Vector operator *(Vector a, double n)
{
	return Vector(a.m*n, a.n*n);
}
Vector operator -(Point a, Point b)
{
	return Vector(a.x - b.x, a.y - b.y);
}    
Point operator +(Point P, Vector V)
{
	return Point(P.x + V.m, P.y + V.n);
}
Point operator -(Point P, Vector V)
{
	return Point(P.x - V.m, P.y - V.n);
}

//############## STRUCT SEGMENT  #######################################################
struct Segment
{
	Point P1, P2;
	Segment()
	{
	}
	Segment(double a, double b, double c, double d)
	{
		P1 = Point(a, b);
		P2 = Point(c, d);
	}
	Segment(Point a, Point b)
	{
		P1 = a;
		P2 = b;
	}
	double mod()
	{
		return sqrt((P1.x - P2.x)*(P1.x - P2.x) + (P1.y - P2.y)*(P1.y - P2.y));
	}
	void show()
	{
		printf("A = (%.2lf, %.2lf) , B = (%.2lf, %.2lf)", P1.x, P1. y, P2.x, P2.y);
	}
};

//############## STRUCT CIRCLE  ########################################################
struct Circle
{
	Point C;
	double R;
	Circle()
	{
	}
	Circle(double a, double b, double c)
	{
		C = Point(a, b);
		R = c;
	}
	void show()
	{
		printf("C = (%.2lf, %.2lf) , R = %.2lf\n", C.x, C.y, R);
	}
};

//### AREA DE UN TRIANGULO #############################################################
double area(Point P1, Point P2, Point P3)
{
	double x1 = P1.x, y1 = P1.y;
	double x2 = P2.x, y2 = P2.y;
	double x3 = P3.x, y3 = P3.y;
	
	return x2*y3 + x1*y2 + y1*x3 - x2*y1 - x3*y2 - y3*x1;
}

//### PUNTO MAS LEJOS DE P #############################################################
Point maslejos(Point P, Point A, Point B)
{
	double d1=(P.x-A.x)*(P.x-A.x) + (P.y-A.y)*(P.y-A.y);
	double d2=(P.x-B.x)*(P.x-B.x) + (P.y-B.y)*(P.y-B.y);
	
	if(d1>d2) return A;
	else return B;
}

//### PUNTO MAS CERCA A P ##############################################################
Point mascerca(Point P, Point A, Point B)
{
	double d1=(P.x-A.x)*(P.x-A.x) + (P.y-A.y)*(P.y-A.y);
	double d2=(P.x-B.x)*(P.x-B.x) + (P.y-B.y)*(P.y-B.y);
	
	if(d1<d2) return A;
	else return B;
}

//### DETERMINA SI P PERTENECE AL SEGMENTO S ###########################################
bool inSegment(Segment S, Point P)
{
	return (area(S.P1, S.P2, P)==0 &&
			P.x >= min(S.P1.x, S.P2.x) && P.x <= max(S.P1.x, S.P2.x) &&
			P.y >= min(S.P1.y, S.P2.y) && P.y <= max(S.P1.y, S.P2.y));
}

//### DETERMINA SI EL SEGMENTO S1 SE INTERSECTA CON EL SEGMENTO S2 #####################
bool intersecta(Segment S1, Segment S2)
{
	if(S1.mod()==0) return inSegment(S2, S1.P1);
	if(S2.mod()==0) return inSegment(S1, S2.P1);
	
	if(area(S1.P1, S1.P2, S2.P1)==0 && area(S1.P1, S1.P2, S2.P2)==0)
		return (inSegment(S1, S2.P1) || inSegment(S1, S2.P2) ||
				inSegment(S2, S1.P1) || inSegment(S2, S1.P2));
	
	return (area(S1.P1, S1.P2, S2.P1)*area(S1.P1, S1.P2, S2.P2)<=0 &&
			area(S2.P1, S2.P2, S1.P1)*area(S2.P1, S2.P2, S1.P2)<=0);
}

//### DETERMINA SI P ESTA EN EL INTERIOR DEL POLIGONO CONVEXO A ########################
bool isInConvex(vector <Point> A, Point P)
{
	for(int i=0; i<A.size(); i++)
		if(area(A[i], A[(i+1)%A.size()], P)<0) return false;
	return true;
}

//### DETERMINA SI A, B, M, N PERTENECEN A LA MISMA RECTA ##############################
bool sameLine(Point A, Point B, Point M, Point N)
{
	return (area(A, B, M)==0 && area(A, B, N)==0);
}

//### SI DOS SEGMENTOS SON PARALELOS ###################################################
bool paralelas(Point A, Point B, Point M, Point N)
{
	Point O = Point(0, 0);
	
	A.x -= B.x;
	A.y -= B.y;
	
	M.x -= N.x;
	M.y -= N.y;
	
	return sameLine(A, O, M, O);
}

//### PUNTO DE INTERSECCION DE DOS RECTAS NO PARALELAS #################################
Point interPoint(Segment S1, Segment S2)
{
	double a1 = S1.P1.x, a2 = S1.P1.y, b1 = S1.P2.x, b2 = S1.P2.y;
	double m1 = S2.P1.x, m2 = S2.P1.y, n1 = S2.P2.x, n2 = S2.P2.y;
	
	double m = ((m1-a1)*(n2-m2)-(m2-a2)*(n1-m1))/((b1-a1)*(n2-m2)-(b2-a2)*(n1-m1));
	
	return S1.P1 + (S1.P2 - S1.P1) * m;
}


int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int caso;
    cin>>caso;
    
    for(int casos=0;casos<caso;casos++){
        int dev=0;
        int t;
        cin>>t;
        vector<int>a(t),b(t);
        for(int i=0;i<t;i++){
            cin>>a[i]>>b[i];    
        }
        for(int i=0;i<t;i++)
            for(int j=i+1;j<t;j++){
                if(intersecta(Segment(0,a[i],1,b[i]),Segment(0,a[j],1,b[j]) ))
                    dev++;
            }
        
        cout<<"Case #"<<casos+1<<": "<<dev<<endl;
    }
    
    //system("pause");
    return 0;
}
