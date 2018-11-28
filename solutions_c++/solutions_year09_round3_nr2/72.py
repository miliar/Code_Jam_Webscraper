#include <cstdio>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

struct vec3
{
  double x, y, z; 
  vec3(){x=y=z=0;} 
  vec3(double a, double b, double c){x=a,y=b,z=c;}
  void prn(){fprintf(stderr, "%lf %lf %lf\n", x, y, z);}
};

double dotprod(vec3 a, vec3 b) { return a.x*b.x+a.y*b.y+a.z*b.z; }
vec3 operator *(double a, vec3 b){ return vec3(a*b.x, a*b.y, a*b.z); }
vec3 operator +(vec3 a, vec3 b){ return vec3(a.x+b.x, a.y+b.y, a.z+b.z); }
vec3 operator -(vec3 a, vec3 b){ return vec3(a.x-b.x, a.y-b.y, a.z-b.z); }
double len(vec3 a) { return sqrt(a.x*a.x+a.y*a.y+a.z*a.z); }
vec3 normal(vec3 a) { return (1.0/len(a))*a; }

int main()
{
  int cases;
  scanf("%d", &cases);
  for(int cas=0; cas<cases; cas++){
    printf("Case #%d: ", cas+1);
    fprintf(stderr, "%d\n", cas);
    int N;
    scanf("%d", &N);
    
    vec3 A, V;
    
    for(int i=0; i<N; i++){
      vec3 a, v;
      scanf("%lf %lf %lf %lf %lf %lf", &a.x, &a.y, &a.z, &v.x, &v.y, &v.z);
      A=A+a;
      V=V+v;
    }
    
    A = (1.0/N)*A;
    V = (1.0/N)*V;

    //fprintf(stderr, "A="); A.prn(); fprintf(stderr, "V="); V.prn();
    
    vec3 Vcap = normal(V);
    vec3 P = A-dotprod(A, Vcap)*normal(Vcap);

    double dmin = len(P);
    double tmin;
    if(fabs(V.x)>1e-15) tmin=(P.x-A.x)/V.x;
    else if(fabs(V.y)>1e-15) tmin=(P.y-A.y)/V.y;
    else if(fabs(V.z)>1e-15) tmin=(P.z-A.z)/V.z;
    else {tmin=0; dmin=len(A);}
    
    if(tmin<1e-15) {dmin = len(A); tmin=0;}

    printf("%lf %lf\n", dmin, tmin);
    
  }
}
