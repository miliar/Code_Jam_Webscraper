#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>


using namespace std;
double dist(int x1, int y1, int x2, int y2)
{
	return sqrt( (double)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) ));
}
int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int test = 0; test < t; test++)
	{
		int n;
		in >> n;
		double x[40], y[40], r[40];
		for(int i=0; i < n; i++)
		{
			in >> x[i] >> y[i] >> r[i];
		}
		if( n==1)
		{
			out<<"Case #"<<test+1<<": " << r[0] << endl;
		}
		if( n == 2)
		{
			out<<"Case #"<<test+1<<": " << max( r[0], r[1]) << endl;
		}
		if( n==3)
		{
			double m1 = (dist(x[0],y[0], x[2], y[2])+ r[0] + r[2] )/2.0;
			double m2 = (dist(x[1], y[1], x[2], y[2] ) + r[1] + r[2])/2.0;
			double m3 = (dist(x[0], y[0], x[1], y[1]) + r[0] + r[1])/2.0;
			double m4 = min(m1, m2);
			double ma1= max(r[0],r[1]);
			double ma2 = max(ma1, (double)r[2]);
			//printf("%.6d", max( ma2, min(m4,m3)));
			out <<"Case #"<<test+1<<": "<< max( ma2, min(m4,m3)) << endl;
		}
		

	}
	return 0;
}