/*
TASK: first
LANG: C++
*/
#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <set>
#include <queue>
#include <cstring>
#include <algorithm>
#define foreach(_v,_c) for( typeof((_c).begin()) _v = (_c).begin() ; _v != (_c).end() ; ++_v )

using namespace std;


const double INF = INFINITY;

struct Point3d;
struct Vector3d;
struct LineSegment3d;

struct Point3d{
    static struct Point3d inf_point;
    double x,y,z;
    Point3d(){
        x=y=z=0;
    }
    Point3d( const Point3d& other ){
        x=other.x;
        y=other.y;
        z=other.z;
    }
    Point3d( double ax , double ay , double az ){
        x=ax;
        y=ay;
        z=az;
    }
    double dist(double ox=0,double oy=0,double oz=0){
        return sqrt( (x-ox)*(x-ox) + (y-oy)*(y-oy) + (z-oz)*(z-oz) );
    }
    double dist(const Point3d& other){
        return dist(other.x,other.y,other.z);
    }
    Point3d operator+( const Point3d& other ) const{
        return Point3d( x+other.x , y + other.y , z+other.z );
    }
    Point3d operator-( const Point3d& other ) const{
        return Point3d( x-other.x , y - other.y , z-other.z );
    }
    Point3d operator+( double coef ) const{
        return Point3d( x+coef , y+coef , z+coef );
    }
    Point3d operator-( double coef ) const{
        return operator+(-coef);
    }
    Point3d operator-()const{
        return Point3d( -x,-y,-z );
    }
    Point3d operator*( double coef ) const{
        return Point3d( x*coef , y*coef , z*coef );
    }
    Point3d& operator=(const Point3d& other){
        x=other.x;
        y=other.y;
        z=other.z;
        return (*this);
    }
    double angleZX(){
        return atan2(z,x);
    }
    double angleYX(){
        return atan2( y , x );
    }
    bool isInf()const{
        return x==INF and y == INF and z == INF;
    }
    bool operator==(const Point3d& other) const{
        return x==other.x and y==other.y and z==other.z;
    }
    operator bool() const{
        return !isInf();
    }
    friend ostream& operator<<( ostream& out , const Point3d& self ){
        out << fixed << setprecision(2) << "( " << self.x << " , " << self.y << " , " << self.z << " )";
        return out;
    }
};
Point3d Point3d::inf_point = Point3d(INF,INF,INF);

struct Vector3d{
    Point3d end;
    Vector3d( const double a , const double b , const double c ){
        end.x = a;
        end.y = b;
        end.z = c;
    }
    Vector3d( const Point3d& p ){
        end.x=p.x;
        end.y=p.y;
        end.z=p.z;
    }
    double dot( const Vector3d& other ) const{
        return end.x*other.end.x+end.y*other.end.y+end.z*other.end.z;
    }
    Vector3d cross( const Vector3d& other ) const{
        return Vector3d( 0 , 0 , end.x*other.end.y-end.y*other.end.x );
    }
    double dbl_cross( const Vector3d& other ) const{
        return end.x*other.end.y-+end.y*other.end.x;
    }
    Vector3d operator+( const Vector3d& other )const{
        Point3d new_end = end + other.end;
        return Vector3d( new_end );
    }
    Vector3d operator-()const{
        return Vector3d( -end.x , -end.y , -end.z );
    }
    Vector3d operator-( const Vector3d& other )const{
        return (*this)+( -other );
    }
    bool operator==( const Vector3d& other ) const{
        return end==other.end;
    }
    Vector3d operator*( double coef ) const{
        return Vector3d( end*coef );
    }
    double operator*( const Vector3d& other )const{
        return dot( other );
    }
    double size(){
        return end.dist();
    }
    friend ostream& operator<<( ostream& out , const Vector3d& self ){
        out << "Vector("<<self.end<<")";
        return out;
    }
};

struct LineSegment3d{
    Point3d a,b;
    LineSegment3d(){
        a.x=b.x=a.y=b.y=a.z=b.z=0;
    }
    LineSegment3d( const Point3d& _a , const Point3d& _b ){
        a = _a;
        b = _b;
    }
    LineSegment3d( double ax , double ay , double az , double bx=0 , double by=0 , double bz=0 ){
        a.x=ax;
        a.y=ay;
        a.z=az;
        b.x=bx;
        b.y=by;
        b.z=bz;
    }
    Point3d getCross( const LineSegment3d& other , bool borders = false ) const{
        Point3d c = other.a;
        Point3d d = other.b;
        if( a==c or a==d or b==c or b==d and !borders ){
            return Point3d::inf_point;
        }
        double x,y;
        double A[3]={a.x,a.y,a.z};
        double B[3]={b.x,b.y,b.z};
        double C[3]={c.x,c.y,c.z};
        double D[4]={d.x,d.y,d.z};
        int comb[][2] = { {0,1} , {1,2} , {2,0} , {1,0} , {2,1} , {2,0} };
        int i;
        for( i = 0 ; i < 6 ; i++ ){
            double& A0=A[ comb[i][0] ];
            double& A1=A[ comb[i][1] ];
            double& B0=B[ comb[i][0] ];
            double& B1=B[ comb[i][1] ];
            double& C0=C[ comb[i][0] ];
            double& C1=C[ comb[i][1] ];
            double& D0=D[ comb[i][0] ];
            double& D1=D[ comb[i][1] ];
            x=(A0-C0)*(D1-C1)-(A1-C1)*(D0-C0);
            x/=(D0-C0)*(B1-A1)-(D1-C1)*(B0-A0);
            y=(A0-C0)+(B0-A0)*x;
            y/=D0-C0;
            if( isnan(x) or isnan(y) or isinf(x) or isinf(y) ){
                continue;
            }else{
                break;
            }
        }
        double DOWN=(!borders)?(1e-11):0;
        double UP  =(!borders)?(1-(1e-11)):1;
        if( DOWN <= x and x <= UP and DOWN <= y and y <= UP ){
            Point3d crosspoint = Point3d( a.x + (b.x - a.x)*x , a.y + (b.y - a.y)*x , a.z - (b.z - a.z)*x );
            return crosspoint;
        }else{
            //cout << "{ " << x << "," << y << " } ";
            return Point3d::inf_point;
        }
    }
    double sineBetween( const Point3d& other ){
        Vector3d v1( b-a );
        Vector3d v2( other-a );
        if( v1.size() == 0 or v2.size() == 0 ){
            return 0;
        }
        return v1.dbl_cross(v2)/(v1.size()*v2.size());
    }
    Point3d midPoint(){
        return (a+b)*0.5;
    }
    double size(){
        return a.dist(b);
    }
    void amplify(double delta){
        Vector3d v(b-a);
        v=v*delta;
        b=a+v.end;
    }
    bool operator==(const LineSegment3d& other) const{
        return a==other.a and b==other.b;
    }
    friend ostream& operator<<( ostream& out , const LineSegment3d& self ){
        out << "LineSegment( "<< self.a <<" , " << self.b << " )";
        return out;
    }
};

int T;

int main(){
	freopen("first.in","r",stdin);
	freopen("first.out","w",stdout);
	
	const int Xleft = 0;
	const int Xright = 10;
	
	cin >> T;
	
	LineSegment3d ls[100000];
	
	for( int i = 0 ; i < T ; i++ ){
	    int N;
	    int count = 0;
	    
	    cin >> N;
	    
	    memset( ls , 0 , sizeof(ls) );
	    
	    for( int j = 0 ; j < N ; j++ ){
	        int ai , bi;
	        cin >> ai >> bi;
	        
	        ls[j].a = Point3d( Xleft , ai , 0 );
	        ls[j].b = Point3d( Xright , bi , 0 );
	        for( int k = 0 ; k < j ; k++ ){
	            //cout << ls[k] << " x "  << ls[j] << " -> " << ls[k].getCross(ls[j]) << endl;
                if( ls[k].getCross( ls[j] ) != Point3d::inf_point ){
                    count++;
                }
	        }
	    }
	    printf("Case #%d: %d\n", i+1 , count);
	}
	return 0;
}
