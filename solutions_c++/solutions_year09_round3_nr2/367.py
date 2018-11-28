#include<iostream>
#include<vector>
#include<complex>

using namespace std;

struct Vector
{
	int x, y, z;
};

int main()
{
	int T;
	cin >> T;

	for(int X = 1; X <= T; ++X)
	{
		int N;
		cin >> N;

		vector<Vector> p(N), v(N);

		double sPix = 0, sPiy = 0, sPiz = 0, sVix = 0, sViy = 0, sViz = 0;

		for(int i = 0; i < N; ++i)
		{
			cin >> p[i].x >> p[i].y >> p[i].z >> v[i].x >> v[i].y >> v[i].z;

			sPix += p[i].x; sPiy += p[i].y; sPiz += p[i].z;
			sVix += v[i].x; sViy += v[i].y; sViz += v[i].z;
		}

		double dmin, tmin;

		if(sVix == 0 and sViy == 0 and sViz == 0)
		{
			tmin = 0;
			dmin = sqrt(sPix*sPix + sPiy*sPiy + sPiz*sPiz) / N;
		}
		else
		{
			tmin = -(sPix * sVix + sPiy * sViy + sPiz * sViz) / (sVix*sVix + sViy*sViy + sViz*sViz);

			if(tmin < 0)
			{
				tmin = 0;
				dmin = sqrt(sPix*sPix + sPiy*sPiy + sPiz*sPiz) / N;
			}
			else
			{
				double dx, dy, dz;

				dx = sPix + tmin * sVix;
				dy = sPiy + tmin * sViy;
				dz = sPiz + tmin * sViz;

				dmin = sqrt(dx*dx + dy*dy + dz*dz) / N;
			}
		}

		cout << "Case #" << X << ": " << dmin << " " << tmin << '\n';
	}

	return 0;
}