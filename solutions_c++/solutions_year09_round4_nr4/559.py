#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <utility>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <cmath>
#include <queue>
#include <stack>
#include <set>

#define all(v) v.begin(),v.end()
#define INFINITO (1LL<<62)
#define eps 1e-07
#define PI  acos(-1.0)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define SGN(x) ((x)<-eps?-1:(x)>eps?1:0)
#define ABS(x) ((x)>0?(x):(-1*(x)))
 
typedef double LL;
template<class T> inline int size(const T&c) { return c.size(); }
template<class T> inline T sqr(const T&c) {return c*c;} 
typedef double coord;

using namespace std;


/************************** ESTRUCTURA DE PUNTO (Y VECTOR) **************************/

struct Point {
  coord x,y;
  Point() {}
  Point(coord x,coord y):x(x),y(y) {}
  double modulo(){return sqrt( sqr(x) + sqr(y) );}
};

Point operator+(const Point &A,const Point&B) { return Point(A.x+B.x,A.y+B.y); }
Point operator-(const Point &A,const Point&B) { return Point(A.x-B.x,A.y-B.y); }
Point operator*(coord c, const Point &A) { return Point(c*A.x,c*A.y); }
coord operator^(const Point&A,const Point&B) { return A.x*B.y-A.y*B.x; }
coord operator*(const Point&A,const Point&B) { return A.x*B.x+A.y*B.y; }
coord len2(const Point&A) { return A*A; }
 
bool operator<(const Point&a, const Point&b) {
  if(fabs(a.x - b.x)>eps) return a.x+eps<b.x;
  return a.y+eps<b.y;
}
bool operator ==(const Point&a, const Point&b){
  return fabs(a.x - b.x)<eps && fabs(a.y - b.y)<eps; 
}
/**********************************************************************************/



/***************** ESTRUCTURA DE CIRCULO ******************/

struct circle{

  Point center;
  coord radius;  
  circle() {}
  circle(Point c,coord r) {center=c;radius=r;}
  double area() {return PI*radius*radius;}
  double perimeter() {return 2*PI*radius;}              
};
/**********************************************************/



/****** DISTANCIA Y DISTANCIA MANHATTAN ENTRE DOS PUNTOS ******/

double distancia(Point A,Point B){
 return  sqrt( sqr(A.x-B.x)+sqr(A.y-B.y) );       
}

double manhattanDist(Point A,Point B){
 return abs(A.x-B.x)+abs(A.y-B.y);
}
/**************************************************************/



/******************** ANGULO ENTRE DOS VECTORES *********************/

double anguloEntreVectores(Point A,Point B){     
  return acos( (A*B)/fabs(A.modulo()* B.modulo()) );        
}
/********************************************************************/



/********************************** DISTANCIA DE LINEA AB a C **********************************/

double linePoinDist(Point A,Point B, Point C, bool esSegmento ){

 Point AB = Point(B-A), BA = Point(A-B), AC = Point(C-A), 
        CA = Point(A-C), BC = Point(C-B), CB = Point(B-C);  

 if( A == B) return distancia(A,C); // el caso en que AB es un punto

double dist = ( AB^AC ) / sqrt( AB * AB );
        
        if(esSegmento){
            double dot1 = BC * AB;
            if(dot1 > 0) return sqrt( CB * CB);
            double dot2 = AC * BA;
            if(dot2 > 0) return sqrt( CA * CA);
        }

 return fabs(dist);      
}
/************************************************************************************************/



/******************* VERIFICA SI EL PUNTO C SE ENCUENTRA DENTRO DEL SEGMENTO AB *******************/  

bool onSegment(Point A,Point B,Point C){

coord minX = min(A.x,B.x), maxX = max(A.x,B.x); 
coord minY = min(A.y,B.y), maxY = max(A.y,B.y);

  return ( minX+eps<C.x || fabs(minX-C.x)<eps ) && ( C.x+eps<maxX || fabs(maxX-C.x)<eps ) &&
	     ( minY+eps<C.y || fabs(minY-C.y)<eps ) && ( C.y+eps<maxY || fabs(maxY-C.y)<eps ); 
}
/**************************************************************************************************/



/********************************** INTERSECCION DE DOS LINEAS **********************************/
 
 /*  Obs:  La intersección de dos segmentos de recta, por lo general saldrá de tipo double, 
           así que se debe tener cuidado con el tipo de dato "coord" */ 
           
Point lineLineIntersec(Point A,Point B,Point C,Point D){

 coord A1 = B.y - A.y, B1 = A.x - B.x, C1 = A1*A.x + B1*A.y ;
 coord A2 = D.y - C.y, B2 = C.x - D.x, C2 = A2*C.x + B2*C.y ;  
 coord det = A1*B2 - A2*B1;
 Point ans;
    if( fabs(det) < eps) return Point(INFINITO,INFINITO); //o sea si es 0, es paralelo   
    else{
        coord x = (B2*C1 - B1*C2)/det;
        coord y = (A1*C2 - A2*C1)/det;
		ans = Point(x,y);
	}
  if( onSegment(A,B,ans) && onSegment(C,D,ans) ) return ans;
  return Point(INFINITO,INFINITO);
}


/* Esta funcion nos dara la interseccion de dos rectas infinitas cuya ecuacion
   general es Ax + By = C */

Point rectaRectaIntersec(coord A1, coord B1, coord C1, coord A2, coord B2, coord C2){

 coord det = A1*B2 - A2*B1;
 Point ans;
    if( fabs(det) < eps) return Point(INFINITO,INFINITO); //o sea si es 0, es paralelo   
    
        coord x = (B2*C1 - B1*C2)/det;
        coord y = (A1*C2 - A2*C1)/det;
       
        ans = Point(x,y);
	
   return ans;
}
/************************************************************************************************/



/******************************** CIRCUNFERENCIA DE TRES PUNTOS ********************************/

 circle getCircum(Point P,Point Q,Point R){
   
    Point M1 = 0.5*(P + Q), M2 = 0.5*(Q + R);
    coord A1 = Q.y - P.y, B1 = P.x - Q.x;
    coord A2 = R.y - Q.y, B2 = Q.x - R.x;
    
    coord D1 = -B1*M1.x + A1*M1.y;
    coord D2 = -B2*M2.x + A2*M2.y;
    
    Point centro = rectaRectaIntersec(-B1,A1,D1,-B2,A2,D2);
    coord radio = distancia(centro,P);
    
    return circle(centro,radio);
 }
/***********************************************************************************************/



/******************************* REFLEJO DE UN PUNTO *******************************/

/* El resultado es el punto C' que es simetrico a C respecto a la recta AB */
  
   Point reflectPoint(Point A,Point B, Point C){
  
    coord A1 = B.y - A.y, B1 = A.x - B.x, C1 = A1*A.x + B1*A.y;
    coord D = -B1*C.x + A1*C.y;
    Point inter = rectaRectaIntersec(A1,B1,C1,-B1,A1,D); 
    
    return inter - (C - inter);
  }
/***********************************************************************************/



/************************* DISTANCIA DE LINEA AB a LINEA BC ************************************/

double lineLineDist(Point A,Point B,Point C,Point D){
  
	return  !(lineLineIntersec(A,B,C,D) == Point(INFINITO,INFINITO) )? 0:     
		       min( min(linePoinDist(A,B,C,true),linePoinDist(A,B,D,true)),
		          min(linePoinDist(C,D,A,true),linePoinDist(C,D,B,true)) );
}
/***********************************************************************************************/



/****************************** DIRECCION ********************************/

/* Obs: Pi ---> Pj ---> Pk 
        Retorna 1 si es horario, -1 si es antihorario ó 0 si es colineal  */

int direction(Point Pi, Point Pj, Point Pk) { 
  return SGN( (Pk-Pi)^(Pj-Pi) ) ; 
} 
/*************************************************************************/



/******************* PUNTO DENTRO DE POLIGONO CONVEXO ********************/

/*  Esto incluye a los puntos que estan dentro del poligono, asi como en 
    los bordes. Cabe resaltar que los puntos deben estar en sentido horario
    o antihorario */
    
int insidePoly(Point p,vector<Point> a) { 
  int left = 0; 
  int right = 0;
  int n = a.size();
  for (int i = 0; i < n; i++) 
    switch (  direction(p, a[i], a[(i + 1) % n])  ) { 
    case  1: left  = 1; break; 
    case -1: right = 1; break; 
    } 
  return !(left & right); 
}
/*************************************************************************/



/***************************** CONVEX HULL **********************************/

/* Obs: Este convex hull nos da los puntos de tal manera que en una arista
        no haya puntos colineales. Si se desea incluirlos, se cambia el >= 0 
        por un > 0 */

vector<Point> cHull(vector<Point> points) {
  
 vector<Point> hull;
  sort(points.begin(),points.end());
  int npoints = size(points);
  int start = 0;
  hull.push_back(points[0]);
  int nh = 1;
  FOR(i,1,npoints-1) {
    Point p = points[i];
    while(nh-start >= 2 && SGN((p-hull[nh-2])^(p-hull[nh-1])) >= 0) {
      --nh; hull.pop_back();
    }
    hull.push_back(p); ++nh;
  }
  start = nh-1;
  FORD(i,npoints-2,0) {
    Point p = points[i];
    while(nh-start >= 2 && SGN((p-hull[nh-2])^(p-hull[nh-1])) >= 0) {
      --nh; hull.pop_back();
    }
    hull.push_back(p); ++nh;
  }
  hull.pop_back();
return hull;
}
/***************************************************************************/



/******************** AREA DE UN POLIGONO **********************/

/* Los puntos deben estar en sentido horario o antihorario */

double getArea(vector<Point> points ){
  if( points.size()==0) return 0;
  int sz=size(points);
  Point A=points[0];
  double area=0;
  for(int i=1;i<sz-1;i++){
    Point B=points[i],C=points[i+1];
    area+=(B-A)^(C-A);
  }
  area/=2;
  area=fabs(area);
  return area;
}
/**************************************************************/



/************************ INTERSECCION DE DOS POLIGONOS CONVEXOS ************************/

vector<Point> getPolyIntersec(vector<Point> A,vector<Point> B){

 vector<Point> ans,aux;
 int m = A.size(), n = B.size(); 
  for(int i=0;i<m;i++)
   if( insidePoly(A[i],B))
	 aux.push_back(A[i]);

   for(int i=0;i<n;i++)
   if( insidePoly(B[i],A)) 
	 aux.push_back(B[i]);

	 for(int i=0;i<m;i++){
		 for(int j=0;j<n;j++){
		    Point luchin = lineLineIntersec(A[i],A[(i+1)%m],B[j],B[(j+1)%n]);
			if( luchin.x + eps < INFINITO && luchin.y + eps < INFINITO )
			 aux.push_back(luchin);
		 }
	 }
 if( aux.size()==0) return aux;
 ans = cHull(aux);
 return ans;
}
/****************************************************************************************/



/******** PUNTOS ENTEROS COMPRENDIDOS ENTRE DOS PUNTOS EN UN SEGMENTO ********/

/* Obs: el tipo de dato "coord" debe ser entero (o long long) para 
        que esta funcion tenga sentido */ 
        
long long howMany(Point A, Point B){

  long long xx = A.x - B.x, x , y, yy = A.y - B.y;  
  if( xx == 0 && yy == 0) return 0;
  
  long long mcd = __gcd(ABS(xx),ABS(yy));
   x = xx/mcd; y= yy/mcd;
   
   if( xx ) return xx/x - 1;  
   return  yy/y - 1;
}
/*****************************************************************************/




int N,T;
double ans,aux;

int main(){
 
  scanf("%d",&T);
  
   for(int caso=1;caso<=T;caso++){
    
     cin>>N;
     vector<Point> v(N);
     vector<double> R(N);
     
     
      for(int i=0;i<N;i++) cin>>v[i].x>>v[i].y>>R[i];
      
      if( N == 1) ans = R[0]; 
      else if( N==2) ans = max(R[0],R[1]);
      else{
        
         ans =   INFINITO; //max(max ( R[0],R[1]), R[2]);
         
         for(int i=0;i<2;i++)
          for(int j=i+1;j<3;j++){
          
            aux = max( (distancia(v[i],v[j]) + R[i]+ R[j])/2, R[3-i-j]  );
            ans = min(ans,aux);
          }
           
          
      }
      
       
     printf("Case #%d: %lf\n",caso,ans);  
   }
 
}

