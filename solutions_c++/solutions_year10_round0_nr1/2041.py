#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

ifstream dat ("a.in");
ofstream sol ("a.out");

int main ()
{
	int t,n,k,p,r=0;
	dat >> t;
	for (p=0;p<t;p++)
	{
		dat >> n >> k;
		sol << "Case #" << p+1 << ": ";
		r=(int)(pow(2.0,n));
		if (k<r-1)
		{
			sol << "OFF" << endl;
			continue;
		}
		if ((k-r+1)%r==0) sol << "ON" << endl;
		else sol << "OFF" << endl;		
	}
	return 0;
}
