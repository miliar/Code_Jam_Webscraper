#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<sstream>
#include<set>
#include<cmath>

using namespace std;

double dist(double x1, double y1, double x2, double y2)
{
	double retval = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1);
	return sqrt(retval);
}

int main()
{
	int cases;
	cin >> cases;

	for(int n=1;n<=cases;n++)
	{
		int p;
		cin >> p;
		vector<int> x(p), y(p), r(p);

		double retval = 2000.0;

		for(int i=0;i<p;i++)
		{
			cin >> x[i] >> y[i] >> r[i];
		}

		if(p==1)
		{
			retval = r[0];
		}
		else if(p==2)
		{
			retval = max(r[0],r[1]);
		}
		else if(p==3)
		{
			double distAB, distAC, distBC;
			distAB = dist(x[0],y[0],x[1],y[1]) + r[0] + r[1];
			distAC = dist(x[0],y[0],x[2],y[2]) + r[0] + r[2];
			distBC = dist(x[1],y[1],x[2],y[2]) + r[1] + r[2];
			distAB/=2;
			distAC/=2;
			distBC/=2;
			retval = max(distAB, (double)r[2]);
			retval = min(retval,max(distAC, (double)r[1]));
			retval = min(retval,max(distBC, (double)r[0]));
		}
		

		cout << "Case #" << n << ": ";
		cout << retval;
		cout << endl;
	}
	return 0;
}
