#include <iostream>
#include <math.h>

#define EPSILON 1E-15
using namespace std;

//estructura de un punto
typedef struct {
   double X, Y;
} point;
//estructura de una linea
typedef struct {
    double a;
    double b;
    double c;
} line;
//estructura de un circulo
typedef struct {
	point c; /* center of circle */
	double r; /* radius of circle */
} circle;
//convertir de dos puntos a una linea
void points_to_line(point p1, point p2, line &l)
{
    if (p1.X == p2.X) {
        l.a = 1;
        l.b = 0;
        l.c = -p1.X;
    } else {
        l.b = 1;
        l.a = -(p1.Y-p2.Y)/(p1.X-p2.X);
        l.c = -(l.a * p1.X) - (l.b * p1.Y);
    }
}
//convertir de un punto y una pendiente a una recta
void point_and_slope_to_line(point p, double m, line &l)
{
    l.a = -m;
    l.b = 1;
    l.c = -((l.a * p.X) + (l.b * p.Y));
}
//verificar si dos lineas son paralelas
bool parallelQ(line l1, line l2)
{
     bool band=false;
     band=((fabs(l1.a-l2.a)<=EPSILON)&&(fabs(l1.b-l2.b)<=EPSILON));
     if(band) return band;
     else{
          if((l1.b!=0)&&(l2.b!=0))
              if(fabs(l1.a/l1.b-l2.a/l2.b)<EPSILON) return true;

          if((l1.b==0)&&(l2.b==0))
              if(fabs(l1.c/l1.a-l2.c/l2.a)<EPSILON) return true;
          return band;
     }
}
//verificar si las lineas son iguales
bool same_lineQ(line l1, line l2)
{
     bool band=false;
     band=(parallelQ(l1,l2)&&(fabs(l1.c-l2.c)<=EPSILON));
     if(band) return true;
     else{
          double a1,a2;
          if((l1.b!=0)&&(l2.b!=0))
          {
              a1=(l1.a+l1.c)/l1.b;
              a2=(l2.a+l2.c)/l2.b;
              if (parallelQ(l1,l2)&&(fabs(a1-a2)<=EPSILON)) return true;
          }
          if((l1.a!=0)&&(l2.a!=0))
          {
              a1=(l1.b+l1.c)/l1.a;
              a2=(l2.b+l2.c)/l2.a;
              if (parallelQ(l1,l2)&&(fabs(a1-a2)<=EPSILON)) return true;
          }
          return false;
     }
}
//intercepcion de dos puntos
void intersection_point(line l1, line l2, point &p)
{
	if (same_lineQ(l1,l2)) {
		p.X = p.Y = -1;
		return;
	}
	if (parallelQ(l1,l2)) {
		p.X = p.Y = -1;
		return;
	}
	p.X = (l2.b*l1.c - l1.b*l2.c) / (l2.a*l1.b - l1.a*l2.b);
	if (fabs(l1.b) > EPSILON) /* test for vertical line */
		p.Y = - (l1.a * (p.X) + l1.c) / l1.b;
	else
		p.Y = - (l2.a * (p.X) + l2.c) / l2.b;
}

int main(){

    int t,n,j,k,res;
    point p1,p2,p3;
    line linea;
    line lineas[1001];
    double xi[1001];
    double xd[1001];
    double yi=0,yd=0;

    cin>>t;
    for(int i=1;i<t+1;i++){
        res=0;
        cout<<"Case #"<<i<<": ";
        cin>>n;
        for(j=0;j<n;j++){
           cin>>xi[j]>>xd[j];
           if(xi[j]>yd) yd=xi[j];
           else if(xd[j]>yd) yd=xd[j];
        }
        for(j=0;j<n;j++){
           p1.X=xi[j];   p1.Y=yi;   p2.X=xd[j];    p2.Y=yd;
           //cout<<p1.X<<" "<<p2.X<<" ";
           points_to_line(p1, p2, lineas[j]);
        }
        n--;
        for(j=0;j<n;j++){
            for(k=j+1;k<n+1;k++){
                intersection_point(lineas[j], lineas[k], p3);
                //cout<<p3.X<<" "<<p3.Y<<", ";
                if(p3.X!=-1 && p3.Y!=-1 && p3.X>=0 && p3.X<=yd && p3.Y>=0 && p3.Y<=yd) res++;
            }
        }
        cout<<res<<endl;
    }
}
