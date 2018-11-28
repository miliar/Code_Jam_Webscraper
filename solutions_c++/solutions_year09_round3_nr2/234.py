#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
using namespace std;

typedef long long LL ;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define sqr( x ) ((x)*(x))
template<class T> inline void checkmax( T&a ,T b ){ if(b>a) a=b;}
template<class T> inline void checkmin( T&a ,T b ){ if(b<a) a=b;}
template<class T> inline T gcd( T a , T b ){ return b?gcd(b,a%b):a;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}


const int MAXN = 505 ;
const int MAXM = 270 ;
const double eps = ( 1e-15 ) ;

int N ;
struct Point{
	double x , y , z , vx , vy , vz ;
	Point(){}
	Point( double _x , double _y , double _z ){
		x = _x , y = _y , z = _z ;
	}
};
Point P[MAXN] ;

int dcmp(double x){return x < -eps ? -1 : x > eps; } 

double dis( Point x  ){
	return sqrt( sqr(x.x) + sqr( x.y ) + sqr( x.z ) ) ;
}

double Calc( double t ){
	double x = 0 , y = 0 , z = 0 ;
	for( int i = 0 ; i < N ; i ++ ){
		x += P[i].x + P[i].vx * t ;
		y += P[i].y + P[i].vy * t ;
		z += P[i].z + P[i].vz * t ;
	}
	//cout << x << " " << y << " " << z << endl ;
	x /=  N ,  y /= N , z /= N ;
	return dis( Point( x , y  , z  ) ) ;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int cases ; scanf("%d",&cases );
	for( int k = 1 ; k <= cases ; k ++ ){
		scanf("%d",&N);
		for( int i = 0 ; i < N ; i ++ ){
			scanf("%lf%lf%lf%lf%lf%lf",&P[i].x ,&P[i].y ,&P[i].z , &P[i].vx ,&P[i].vy,&P[i].vz);
		}
		double F = 0 , T = 1e50 ;
		while( F + eps < T ){
			double m1 = F + ( T - F ) / 3.0 ;
			double m2 = F + 2.0*( T - F ) / 3.0 ;
			if( fabs( m1 - m2 ) < eps ) break;
			double d1 = Calc( m1 ) ;
			double d2 = Calc( m2 ) ;			
			//cout << m1 << " " << m2 << endl;
			//cout << d1 << " " << d2 << endl;
			if( fabs( d1 - d2 ) < 1e-20 ) break;
			if( dcmp(d1-d2) > 0 ){
				F = m1 + eps ;
			}else if( dcmp(d2-d1) > 0  ){
				T = m2 - eps ;
			}else{
				F = m1 + eps ;
				T = m2 - eps ;
			}
		}
		double t = Calc( 0.0 ) ; 
		double res = Calc( F ) ; if( res > t || F > 1e10 ) res = t , F = 0.0 ; 
		printf("Case #%d: %.8lf %.8lf\n" , k , res , F );
	}
}