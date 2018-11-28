#include <iostream> 
#include <queue>
#include <algorithm>
#include <vector>
#include <cassert>
#include <map>
#include <cmath>
#include <set>
#include <string>
#include <cstring>
#include <cstdio>

#ifdef D 
#define D 1
#else 
#define D 0
#endif

using namespace std; // insert push_back find size begin first second

typedef unsigned long long ULL;
typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef map<int,int> MII;
typedef vector<PII> VPII;
typedef set<int> SI;
typedef pair<double,double> PDD;

typedef struct {
  double x, y, z;
} tP;
tP point(double x = 0, double y = 0, double z = 0) {  // pseude-constructor
  tP a;
  a.x = x;
  a.y = y;
  a.z = z;
  return a;
}
double abs3d(tP a) {             // euclidean norm of point a
  return sqrt( a.x*a.x + a.y*a.y + a.z*a.z );
}
double operator* (tP a, tP b) {   // scalar product
  return a.x*b.x + a.y*b.y + a.z*b.z;
}
tP operator* (double d, tP a) {   // scalar multiplication
  return point( d*a.x, d*a.y, d*a.z);
}
tP operator+ (tP a, tP b) {       // vector addition
  return point(a.x + b.x, a.y + b.y, a.z + b.z); 
}
tP operator- (tP a, tP b) {       // vector substraction
  return a + (-1.0) * b;
}

// POINT LINE DISTANCE
// point c
// line L: a + t * b
// returns distance between point c and line L
double pldist(tP c, tP a, tP b) {
  double tf = ( (c-a) * b ) / (b*b);
  return abs3d( c - (a + tf * b) );
}

double pltime(tP c, tP a, tP b) {
  double tf = ( (c-a) * b ) / (b*b);
  return tf;
}




PDD doit(){
    int n;
    cin >> n;
    int data[6][n];
    for(int i=0;i<n;i++)
        cin >> data[0][i] >> data[1][i] >> data[2][i] >> data[3][i] >> data[4][i] >> data[5][i] ;
    for(int i=0;i<n;i++)
        cerr <<" "<< data[0][i] <<" "<< data[1][i] <<" "<< data[2][i] <<" "<< data[3][i] <<" "<< data[4][i] <<" "<< data[5][i] <<" "<< endl;
    double x0,y0,z0;
    int sx,sy,sz,dx,dy,dz;
    sx=sy=sz=dx=dy=dz=0;
    for(int i=0;i<n;i++){
        sx+=data[0][i];
        sy+=data[1][i];
        sz+=data[2][i];
        dx+=data[3][i];
        dy+=data[4][i];
        dz+=data[5][i];
    }
    x0 = ((double)sx)/((double)n);
    y0 = ((double)sy)/((double)n);
    z0 = ((double)sz)/((double)n);
    fprintf(stderr,"(%lf,%lf,%lf) : (%d,%d,%d)\n",x0,y0,z0,dx,dy,dz);
    tP p0,dir,_0;
    p0 = point(x0,y0,z0);
    dir = point(dx,dy,dz);
    _0 = point(0,0,0);
    double dist = -1;
    double time = -1;
    if(abs3d(dir)>0){
       time = n*pltime(_0,p0,dir); 
       dist = pldist(_0,p0,dir) ;

    }
    if(time<0){
        dist= abs3d(p0);
	time = 0.0;
    }
    cerr << dist << " " << time << endl;
    return PDD(dist,time);
}

int main(){
    int N;
    cin >> N;
    for(int kase =1 ;kase<=N;kase++){
        PDD p = doit();
	printf("Case #%d: %.8lf %.8lf\n",kase,p.first,p.second);
    }
    return 0;
}
