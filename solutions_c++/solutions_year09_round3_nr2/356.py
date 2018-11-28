#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	string file = "B-large";
//	string file = "";
//	string file = "";
	ifstream ifs((file+".in").c_str());
	ofstream ofs((file+".out").c_str());
	int N;
	int num;
	string buf;
	int tx, ty, tz, tvx, tvy, tvz;
	double x, y, z, vx, vy, vz;
	double tmin, dmin; 

	getline(ifs, buf);
	N = atoi(buf.c_str());
	for(int n=0; n<N; n++)
	{
		x = y = z = vx = vy = vz = 0;
		getline(ifs, buf);
		num = atoi(buf.c_str());
		for(int i=0; i<num; i++)
		{
			getline(ifs, buf);
			sscanf(buf.c_str(), "%d %d %d %d %d %d", &tx, &ty, &tz, &tvx, &tvy, &tvz);
			x += tx; y += ty; z += tz;
			vx += tvx; vy += tvy; vz += tvz;
		}
		x /= num; y /= num; z /= num;
		vx /= num; vy /= num; vz /= num;

		tmin = - (x*vx + y*vy + z*vz) / (vx*vx + vy*vy + vz*vz);
		if(tmin <= 0) tmin = 0;
		if(sqrt(vx*vx + vy*vy + vz*vz) < 0.000005) tmin = 0;
		dmin = sqrt((x+tmin*vx)*(x+tmin*vx) + (y+tmin*vy)*(y+tmin*vy) + (z+tmin*vz)*(z+tmin*vz));
		ofs << "Case #" << n+1 << ": " << dmin << " " << tmin << endl;
		cout << n+1 << endl;
	}

	return 0;
}


