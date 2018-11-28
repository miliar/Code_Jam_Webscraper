#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<cmath>
using namespace std;
double eps = 1e-9 ; 
int x[502] , y[502], z[502] , vx[502], vy[502] , vz[502]; 
int main(){
	freopen("avto.in","r", stdin);
	freopen("avto.out","w", stdout);
	int T ; 
	cin >> T ;
	for( int t = 1; t <= T ; t++){
		int n , i ; 
		cin >> n; 
		double X =  0 , Y = 0 , Z = 0 , VX = 0 , VY = 0 , VZ = 0;
		for(i=0;i < n; i++){
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i] ;
			X += x[i] ; Y += y[i] ; Z += z[i] ;
			VX += vx[i] ; VY += vy[i] ; VZ += vz[i] ;
		}
		X /=  n*1.0 ; Y /=  n*1.0 ; Z /=  n*1.0 ; VX /=  n*1.0 ; VY /=  n*1.0 ;
		VZ /=  n*1.0 ;
		double dmin = 0.0 , tmin = 0.0 ; 
		if( fabs(X) < eps && fabs(Y) < eps && fabs(Z) < eps  ){
			dmin = 0.0 ; tmin = 0.0 ; 
		}
		else if( fabs(VX) < eps && fabs(VY) < eps && fabs(VZ) < eps  ){
			dmin =  sqrt(  X*X + Y*Y + Z*Z ) ; tmin = 0.0 ;
		}
		else {
			double t =   -(  VX*X + VY*Y + VZ*Z )/ ( VX*VX + VY*VY + VZ*VZ )  ;
			if ( t < 0 ) {
				dmin =  sqrt(  X*X + Y*Y + Z*Z ) ; tmin = 0.0 ;
			}
			else {
				dmin = sqrt( (X + VX*t)*(X + VX*t) + (Y + VY*t)*(Y + VY*t) + (Z + VZ*t)*(Z + VZ*t) ) ;
				tmin = t ; 
			}
		}
		printf( "Case #%d: %.6lf %.6lf\n" , t , dmin , tmin ) ;
		//cout << "Case #" << t << ": " << val << "\n" ;
	}

	return 0;

}