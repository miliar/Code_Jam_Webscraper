#include<iostream>
using namespace std;
#include<cmath>
int x[3],y[3],r[3];
double dis(int i,int j){
  return sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])* (y[i] - y[j]));
}
double max( double a, double b){
  return (a>b ? a:b);
}

double min(double a, double b, double c){
   if( a<=b && a<=c)
	 
	   return a;
   if(b <=a && b<=c)
	 return b;
   return c;
}

  
int main(){
  int C,kase,N,i,k;
  scanf("%d",&C);
  for(kase=1;kase<=C;kase++){
	scanf("%d",&N);
	
	for(i=0;i<N;i++)
	  scanf("%d %d %d",&x[i],&y[i],&r[i]);
	cout<<"Case #"<<kase<<": ";
	if(N==1)
	  printf("%.6lf\n",r[0]*1.0);
	else if(N==2)
	  printf("%.6lf\n",max(r[0]*1.0,r[1]*1.0));
	else
	  printf("%.6lf\n",min( max((dis(0,1)+r[0]*1.0+r[1]*1.0)/2 , 1.0*r[2]), max((dis(1,2)+r[1]*1.0+r[2]*1.0)/2 , 1.0*r[0]), max((dis(0,2)+r[0]*1.0+r[2]*1.0)/2 , 1.0*r[1])));
  }
  return 0;
}
