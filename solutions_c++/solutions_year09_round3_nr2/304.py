#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <vector>
#include <math.h>
using namespace std;
int main (int argc, char * const argv[]) {
	ofstream outFile;
	ifstream inFile;
	outFile.open("B-large.out");
	inFile.open("B-large.in.txt");
	string parsedString;
	int T,N;
	double x,y,z,vx,vy,vz;
	double ax,ay,az,avx,avy,avz;
	double ux,uy,uz,speed;
	double k;
	double fx,fy,fz,t;
	double dmin;
	inFile>>T;

	
	for(int c=0; c<T; c++){
		inFile>>N;
		ax=0; ay=0; az=0;
		avx=0; avy=0; avz=0;
		for(int d=0; d<N; d++){
			inFile>>x>>y>>z>>vx>>vy>>vz;
			ax+=x;
			ay+=y;
			az+=z;
			avx+=vx;
			avy+=vy;
			avz+=vz;
		}
		ax/=N;
		ay/=N;
		az/=N;
		avx/=N;
		avy/=N;
		avz/=N;
		
		
		speed=sqrt(avx*avx+avy*avy+avz*avz);
		if(speed>0){
			ux=avx/speed;
			uy=avy/speed;
			uz=avz/speed;
		
			k=-(ux*ax+uy*ay+uz*az)/(ux*ux+uy*uy+uz*uz);
			
			if(k>0){
				fx=ax+ux*k;
				fy=ay+uy*k;
				fz=az+uz*k;
				t=k/speed;
			}
			else{
				fx=ax;
				fy=ay;
				fz=az;
				t=0;
				
			}
		}
		else{
			fx=ax;
			fy=ay;
			fz=az;
			t=0;
		}
		dmin=sqrt(fx*fx+fy*fy+fz*fz);
		outFile<<"Case #"<<fixed<<setprecision(8)<<c+1<<": "<<dmin<<" "<<t<<endl;
	}
	outFile.close();
	inFile.close();
    return 0;
}
