//code by Carlo Piovesan
//Google Code Jam, round 1C, problem B

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

int main (void) {
	ofstream OUT;
	OUT.open ("OUT.txt");
	ifstream FILE("IN.txt");
	
	int Num;
	FILE>>Num;
	for (int ZZZ=1; ZZZ<=Num; ZZZ++) {
		int N;
		FILE>>N;
		double X=0, Y=0, Z=0;
		double dx=0, dy=0, dz=0;
		
		double x,y,z,ddx,ddy,ddz;
		
		for (int i=0; i<N; i++) {
			FILE>>x>>y>>z>>ddx>>ddy>>ddz;
			X+=x;
			Y+=y;
			Z+=z;
			dx+=ddx;
			dy+=ddy;
			dz+=ddz;
			}
		
		double DIST,TIME;
		
		if (X*X+Y*Y+Z*Z==0 || dx*dx+dy*dy+dz*dz==0) {DIST=sqrt((double)(X*X+Y*Y+Z*Z))/(double)N; TIME=0.0;}
		else {
//			double minDist=sqrt((double)(X*X+Y*Y+Z*Z));
			double INF=0;
			double SUP=20.0*sqrt((double)(X*X+Y*Y+Z*Z))/sqrt((double)(dx*dx+dy*dy+dz*dz));
			
			while (SUP-INF>0.00000001) {
				double A=(2.0*INF+SUP)/3.0;
				double B=(2.0*SUP+INF)/3.0;
				
				double x=X+dx*A;
				double y=Y+dy*A;
				double z=Z+dz*A;
				
				double distA, distB;
				
				distA=sqrt((double)(x*x+y*y+z*z));
				x=X+dx*B;
				y=Y+dy*B;
				z=Z+dz*B;
				distB=sqrt((double)(x*x+y*y+z*z));
				
				if (distA<distB) SUP=B;
				else INF=A;
				}
			
			TIME=0.5*(INF+SUP);
			x=X+dx*TIME;
			y=Y+dy*TIME;
			z=Z+dz*TIME;
			DIST=(sqrt((double)(x*x+y*y+z*z)))/(double)N;
			}
		
		OUT<<"Case #"<<ZZZ<<": ";
		if (DIST<0.0000001) OUT<<"0.0000000";
		else {
			DIST+=0.00000005;
			long long DIM=10000000;
			DIST*=DIM;
			long long B=(long long)DIST;
			OUT<<B/DIM<<".";
			while (DIM>=10) {
				B%=DIM;
				DIM/=10;
				OUT<<B/DIM;
				}
			}
		OUT<<" ";
		if (TIME<0.0000001) OUT<<"0.0000000";
		else {
			TIME+=0.00000005;
			long long DIM=10000000;
			TIME*=DIM;
			long long B=(long long)TIME;
			OUT<<B/DIM<<".";
			while (DIM>=10) {
				B%=DIM;
				DIM/=10;
				OUT<<B/DIM;
				}
			}
		OUT<<"\n";
		}
	FILE.close();
	OUT.close();
	return 0;
	}
