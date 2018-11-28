#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;


int main(){
  int Z;
  scanf("%d",&Z);
  for(int nrz=1; nrz<=Z; nrz++){
    int N;
    scanf("%d",&N);
    int X[3],Y[3],R[3];

    for(int i=0; i<N; i++)
	scanf("%d%d%d",&X[i],&Y[i],&R[i]);

    double result;
    if(N==1)
	result=R[0];
    else if(N==2)
	result=max(R[0],R[1]);
    else{
	double res0=(sqrt( (X[1]-X[2])*(X[1]-X[2])+(Y[1]-Y[2])*(Y[1]-Y[2]) )+R[1]+R[2])/2;
	double res1=(sqrt( (X[0]-X[2])*(X[0]-X[2])+(Y[0]-Y[2])*(Y[0]-Y[2]) )+R[0]+R[2])/2;
	double res2=(sqrt( (X[1]-X[0])*(X[1]-X[0])+(Y[1]-Y[0])*(Y[1]-Y[0]) )+R[1]+R[0])/2;	
	result=min(max(res0,(double)R[0]), max(res1,(double)R[1]));
	result=min(result, max(res2,(double)R[2]));
    }

    printf("Case #%d: %lf\n",nrz,result);
  }
}
