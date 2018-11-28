
#include "stdafx.h"
#include <iostream.h>
#include <string.h>
#include <math.h>
#define M_N 500

int main(int argc, char* argv[])
{
	long T,N;
	cin>>T;
	long data[M_N][6];
	double a[3],b[3],A,B,time,distance;
	for(int t=0;t<T;t++){
		cin>>N;
		memset(a,0,sizeof(double)*3);
		memset(b,0,sizeof(double)*3);
		A=B=0;
		for(int n=0;n<N;n++){
			cin>>data[n][0]>>data[n][1]>>data[n][2]>>data[n][3]>>data[n][4]>>data[n][5];
			for(int i=0;i<3;i++){
				b[i]+=data[n][i];
				a[i]+=data[n][i+3];
			}
		}
		
		for(int i=0;i<3;i++){
			a[i]/=N;
			b[i]/=N;
			A+=a[i]*a[i];
			B+=a[i]*b[i];
		}
		if(A==0)time=0;
		else time=-B/A;
		if(time<0)time=0;
		distance=0;
		for(i=0;i<3;i++){
			distance += (a[i]*time+b[i])*(a[i]*time+b[i]);
		}
		distance=sqrt(distance);
		printf("Case #%d: %0.8f %0.8f \n",t+1,distance,time);
	}
	return 0;
}

