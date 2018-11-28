#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		double mindis, mint;
		int N;
		cin >> N;
		vector<int> x0, y0, z0, vx, vy, vz;
		for(int i=0; i<N; i++)
		{
			int tx0, ty0, tz0, tvx, tvy, tvz;
			cin >> tx0 >> ty0 >> tz0 >> tvx >> tvy >> tvz;
			x0.push_back(tx0);
			y0.push_back(ty0);
			z0.push_back(tz0);
			vx.push_back(tvx);
			vy.push_back(tvy);
			vz.push_back(tvz);
		}
		double X1 = 0., X2 = 0., Y1 = 0., Y2 = 0., Z1 = 0., Z2 = 0.;
		for(int i=0; i<N; i++)
		{
			X1 += (double)x0[i];
			X2 += (double)vx[i];
			Y1 += (double)y0[i];
			Y2 += (double)vy[i];
			Z1 += (double)z0[i];
			Z2 += (double)vz[i];
		}
		if( (X1*X2 + Y1*Y2 + Z1*Z2) <= 0 )
			mint = -(X1*X2 + Y1*Y2 + Z1*Z2) / (X2*X2 + Y2*Y2 + Z2*Z2);
		else mint = 0;
		if((X2*X2 + Y2*Y2 + Z2*Z2)==0)
			mint = 0;
		mindis = (X1 + mint*X2) * (X1 + mint*X2) + (Y1 + mint*Y2) * (Y1 + mint*Y2) + (Z1 + mint*Z2) * (Z1 + mint*Z2);
		mindis /= N*N;
		mindis = sqrt(mindis);

		cout << "Case #" << t << ": " << mindis << " " << mint << endl;
	}
	return 0;
}
