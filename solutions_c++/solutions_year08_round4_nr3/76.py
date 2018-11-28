#include <stdlib.h>
#include <stdio.h>
#include <iostream>
using namespace std;

struct ship
{
	double x, y, z, power;
};

ship data[2000];
double minD = -1e10;
double maxD = 1e10;
int numShip;

double min(double a, double b)
{
	if (a < b) return a;
	return b;
}

double max(double a, double b)
{
	if (a < b) return b;
	return a;
}

double fabs(int a)
{
	if (a < 0) return -a;
	return a;
}


double ind(int sID, int iID)
{
	if (iID == 0)
		return  data[sID].x + data[sID].y + data[sID].z;
	if (iID == 1)
		return -data[sID].x + data[sID].y + data[sID].z;
	if (iID == 2)
		return  data[sID].x - data[sID].y + data[sID].z;
	if (iID == 3)
		return  data[sID].x + data[sID].y - data[sID].z;
	return 0.0;
}

double check(double ind1, double ind2, double ind3, double ind0L, double ind0R)
{
	double tind = ind1 + ind2 + ind3;
	if (tind > ind0L && tind < ind0R)
		return true;
	else
		return false;
}

double test(double t)
{
	double bl[4], br[4];
	int i, j;
	for (i = 0; i < 4; i++)
	{
		bl[i] = minD;
		br[i] = maxD;
	}

	for (i = 0; i < numShip; i++)
	{
		double dist = data[i].power * t;
		for (j = 0; j < 4; j++)
		{
			bl[j] = max(bl[j], ind(i, j) - dist);
			br[j] = min(br[j], ind(i, j) + dist);
		}
	}

	for (i = 0; i < 4; i++)
		if (bl[i] > br[i]) return false;



//	for (i = 0; i < 4; i++)
//	{
//		cout << bl[i] <<  " " << br[i] << endl;
//	}
//		printf("%lf %lf\n", bl[i], bl[j]);


	double lSum = bl[1] + bl[2] + bl[3];
	double rSum = br[1] + br[2] + br[3];
	if (rSum < bl[0] || lSum > br[0])
		return false;
	else
		return true;
}

int main()
{
	int numCase;
	int i, j, k;
	cin >> numCase;
	for (i = 0; i < numCase; i++)
	{
		cin >> numShip;
//		cout << numShip << endl;
		for (j = 0; j < numShip; j++)
		{
			cin >> data[j].x >> data[j].y >> data[j].z >> data[j].power;
			//scanf("%d %d %d %d", &data[j].x, &data[j].y, &data[j].z, &data[j].power);
		}

		double lb = -1.0, ub = 1e7;
		while (ub - lb > 1e-7)
		{
			double mid = (ub + lb) / 2.0;
//			cout << mid << endl;
			if (test(mid))
				ub = mid;
			else
				lb = mid;
		}
		printf("Case #%d: %.6lf\n", i+1, (ub + lb) / 2.0);
	}
	return 0;
}
