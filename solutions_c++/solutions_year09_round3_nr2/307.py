#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	ifstream in("in.txt");
	//ofstream out("out.txt");
	freopen("out.txt", "w", stdout);
	int t;
	in >> t;
	for(int k=0; k<t; k++)
	{
		double n;
		in >> n;
		double mx = 0, my = 0, mz = 0 ;
		double vmx = 0, vmy = 0, vmz = 0;
		for(int i=0; i < n; i++)
		{
			double x,y,z,vx,vy,vz;
			in >> x >> y >> z >> vx >> vy >> vz;
			mx += x;
			my += y; 
			mz += z;
			vmx += vx;
			vmy += vy;
			vmz += vz;
		} 
		mx = mx / n;my = my / n;mz = mz / n;
		vmx = vmx / n; vmy = vmy / n; vmz = vmz / n;
		double time;
		double dist;
		if(  ( vmx*vmx + vmy*vmy + vmz*vmz) == 0 )
		{
			time =0;
			dist = sqrt( mx*mx + my*my + mz*mz);
		}else{
			time = - (mx*vmx + my*vmy + mz*vmz) / ( vmx*vmx + vmy*vmy + vmz*vmz);
			double _x, _y, _z;
			_x = mx + vmx*time;
			_y = my + vmy*time;
			_z = mz + vmz*time;
			dist = sqrt(_x*_x + _y*_y + _z*_z);
		}
		if( time < 0 )
		{
				time = +0;
			dist = sqrt( mx*mx + my*my + mz*mz);
		}
		if( time == 0)
			time = +0;
		cout<<"Case #" << k+1 <<": " ;
		printf("%.8lf", dist);
		cout << " ";
		printf("%.8lf", time);
		cout << endl;

	}

	return 0;
}