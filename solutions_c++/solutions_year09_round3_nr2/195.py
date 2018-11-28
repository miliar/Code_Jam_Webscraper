#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
using namespace std;
ifstream inf;
ofstream outf;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<=_b;i++)
#define FORD(i,a,b) for(int _b=(b),i=(a);i>=_b;i--)


const double eps = 1e-10;
class dot
{
public:
	double x,y,z;
	dot(double nx, double ny, double nz)
	{
		x = nx;
		y = ny;
		z = nz;
	}
	bool iszero()
	{
		return (x*x + y*y + z*z) < eps;
	}
	double dist(dot a)
	{
		return sqrt( (x-a.x)*(x-a.x) + (y-a.y)*(y-a.y) + (z-a.z)*(z-a.z) );
	}
	dot  vect(dot a)
	{
		dot z ((y*a.z-z*a.y),z*a.x-x*a.z,x*a.y-y*a.x);
		return z;
	}
};
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	
	int tests;
	inf >> tests;
		


	for(int test = 0; test < tests; test++)
	{
		double anw = 0;
		int n;
		inf >> n;
		dot center(0,0,0);
		dot speed(0,0,0);
		dot zero(0,0,0);
		outf << "Case #"  << test+1 << ": " ;
		for (int i = 0; i < n;i++)
		{
			double x,y,z,vx,vy,vz;
			inf >> x >> y >> z >> vx >> vy >> vz;
			center.x += x;
			center.y += y;
			center.z += z;
			speed.x += vx;
			speed.y += vy;
			speed.z += vz;
		}
			center.x /= n;
			center.y /= n;
			center.z /= n;
			speed.x /= n;
			speed.y /= n;
			speed.z /= n;
			if(speed.iszero())
			{
				outf << center.dist(zero) << " " << 0 << endl;


			}
			else
			{
				//dist from line to dot
				dot e(speed.x,speed.y,speed.z);
				double len = speed.dist(zero);
				e.x /= len;
				e.y /= len;
				e.z /= len;
				// длина у e - 1 
				dot proe(0-center.x,0-center.y,0-center.z);
				//dot vp = proe.vect(e);
				double ko = (e.x * proe.x + e.y*proe.y + e.z*proe.z);
				double koef =  ko;
				dot nearest(proe.x-e.x*koef,proe.y-e.y*koef,proe.z-e.z*koef);
				double dst = nearest.dist(zero);
				dot sd(nearest.x - proe.x,nearest.y - proe.y,nearest.z - proe.z);
					if((sd.x*e.x + sd.y*e.y +sd.z* e.z) <0)
					{
						// time - ?
						double time;
						time = sd.dist(zero)/speed.dist(zero);
						outf << dst << " " << time << endl;



					}
					else
						outf << center.dist(zero) << " " << 0 << endl;

					
				
				
				
				

			}




		
		

			
			//outf <<  anw << endl;
			//if (test != tests-1) outf << endl;
		
	}
	
	outf.close();
	return 0;
}
