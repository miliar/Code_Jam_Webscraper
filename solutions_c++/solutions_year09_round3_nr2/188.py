#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
using namespace std;

int main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("res.out");

	int T, caseNo;
	double c1, c2, c3;
	double dmin, tmin;
	ifs >> T;
	for(int caseNo = 1; caseNo <= T; ++caseNo)
	{
		int N;
		ifs >> N;
		double xx, yy, zz;
		double ox = 0, oy = 0, oz = 0;
		double tx = 0, ty = 0, tz = 0;
		for(int i = 0; i < N; ++i)
		{
			ifs >> xx >> yy >> zz;
			ox += xx; oy += yy; oz += zz;
			ifs >> xx >> yy >> zz;
			tx += xx; ty += yy; tz += zz;
		}
		ox/=(double)N;oy/=(double)N;oz/=(double)N;
		tx/=(double)N;ty/=(double)N;tz/=(double)N;

		c1 = tx*tx + ty*ty + tz*tz;
		c2 = 2*ox*tx + 2*oy*ty + 2*oz*tz;
		c3 = ox*ox + oy*oy + oz*oz;

		//c1, c2, c3;
		double delt = c2 * c2 - 4.0 * c1 * c3;
		if(delt < 0)
		{
			tmin = -(c2)/(2.0*c1);
			if(tmin >= 0)
			{
				dmin = fabs(c3 - c2*c2/(4.0*c1));
			}
			else
			{
				tmin = 0.0;
				dmin = fabs(c3);
			}
		}
		else
		{
			dmin = 0;
			delt = sqrt(delt);
			double x1 = (-c2+delt)/(2.0*c1);
			double x2 = (-c2-delt)/(2.0*c1);
			if(x2>=0)
				tmin = x2;
			else if(x1>=0)
				tmin = x1;
			else
			{
				tmin = 0.0;
				dmin = fabs(c3);
			}
		}
		ofs << "Case #" << caseNo<< ": "  << sqrt(dmin) << " " << tmin << endl;
	}

	ifs.close();
	ofs.close();
	
	return 0;
}