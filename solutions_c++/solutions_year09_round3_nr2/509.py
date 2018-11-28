#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	int numCase;
	cin >> numCase;
	int i;
	for (i = 0; i < numCase; i++)
	{
		int n;
		cin >> n;
		int j;

		int x=0, y=0, z=0;
		int vx=0, vy=0, vz=0;
		int value;
		for (j=0;j<n;j++){
			cin >> value;
			x=x+value;
			cin >> value;
			y=y+value;
			cin >> value;
			z=z+value;
			cin >> value;
			vx=vx+value;
			cin >> value;
			vy=vy+value;
			cin >> value;
			vz=vz+value;
		}

		double a = (vx*vx+vy*vy+vz*vz)*1.0;
		double b = (2*vx*x + 2*vy*y + 2*vz*z)*1.0;
		double c = (x*x + y*y + z*z)*1.0;


		double dmin, tmin;

		if (a==0){
			if (b==0){
				dmin=sqrt(c)/n;
				tmin=0;
			}else{
				tmin=-c/b;
				if (tmin<0)
				{
					tmin =0;
					dmin = sqrt(c)/n;
				}else
				{
					dmin=0;
				}

			}

		}else if (b*b>=4*a*c){
			dmin=0;
			tmin = (-b-sqrt(b*b-4*a*c))/(2*a);
			if (tmin<0)
			{
				tmin = (-b+sqrt(b*b-4*a*c))/(2*a);
				if (tmin<0){
					dmin=sqrt(c)/n;
					tmin=0;
				}
			}
		}else
		{
			dmin=sqrt(c-b*b/(4*a))/n;
			tmin=-b/(2*a);
			if(tmin<0){
				dmin=sqrt(c)/n;
				tmin=0;
			}
		}
		cout.precision(8);
		cout.setf(ios::fixed,ios::floatfield);

		cout << "Case #" << (i+1) << ": " << dmin << ' '<<tmin << endl;
	}
	return 0;
}



