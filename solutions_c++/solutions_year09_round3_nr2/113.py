#include<iostream>
#include<cmath>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)   REP(i,0,n)

double calc(double *in,int n){
  double val=0;
  rep(i,n)val+=in[i];
  return val;
}

void solve(int n,double *x,double *y,double *z,double *vx,
	     double *vy,double *vz){
  double X=calc(x,n),Y=calc(y,n),Z=calc(z,n);
  double A=calc(vx,n),B=calc(vy,n),C=calc(vz,n);
  double t = -(A*X+B*Y+C*Z)/(A*A+B*B+C*C);
  
  
  if ( t<=1e-5)t=0;
  else if ( isnan(t))t=0;
  printf("%.8lf %.8lf\n",
	 sqrt((X*X+Y*Y+Z*Z)+2*t*(A*X+B*Y+C*Z)+t*t*(A*A+B*B+C*C)+1e-10)/n,
	 t);
}

main(){
  int te;
  int tc=1;
  cin>>te;
  while(te--){
    int n;
    cin>>n;
    double x[n],y[n],z[n],vx[n],vy[n],vz[n];
    rep(i,n)cin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
    cout << "Case #"<<tc++<<": ";
    solve(n,x,y,z,vx,vy,vz);
  }
}
