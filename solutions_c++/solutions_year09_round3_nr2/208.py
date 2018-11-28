#include<iostream>
using namespace std;
#include<math.h>
int X[500][3], V[500][3];
int main(){
  int kase, T, N, i, k;
  scanf("%d\n",&T);
  double Mx, My, Mz, Vx, Vy, Vz, d, t;
  for(kase=1;kase<=T;kase++){
	scanf("%d\n",&N);
	for(i=0;i<N;i++)
	  scanf("%d %d %d %d %d %d",&X[i][0],&X[i][1],&X[i][2],&V[i][0],&V[i][1],&V[i][2]);
	Mx=My=Mz=Vx=Vy=Vz=0.0;
	for(i=0;i<N;i++){
	  Mx += X[i][0];
	  My += X[i][1];
	  Mz += X[i][2];
	  Vx += V[i][0];
	  Vy += V[i][1];
	  Vz += V[i][2];
	}
	//cout<<Mx<<" "<<My<<" " <<Mz<<" "<<Vx<<" "<<Vy<<" "<<Vz<<endl;
	Mx = Mx/N;
	My = My/N;
	Mz = Mz/N;
	Vx = Vx/N;
	Vy = Vy/N;
	Vz = Vz/N;
	//cout<<Mx<<" "<<My<<" " <<Mz<<" "<<Vx<<" "<<Vy<<" "<<Vz<<endl;
	double tmp = (Vx*Vx+Vy*Vy+Vz*Vz);
	if(tmp > 0.0000000001){
	  t = -(Mx*Vx + My*Vy + Mz*Vz)/(Vx*Vx+Vy*Vy+Vz*Vz);
	}
	else
	  t= +0.0;
	if(t <= 0.0)
	  t = +0.0;
	d = sqrt((Mx+Vx*t)*(Mx+Vx*t) +(My+Vy*t)*(My+Vy*t) +(Mz+Vz*t)*(Mz+Vz*t));
	
	printf("Case #%d: %.8lf %.8lf\n",kase,d,t);
  }
  return 0;
}
