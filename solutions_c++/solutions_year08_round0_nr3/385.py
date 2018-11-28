#include <iostream>
#include <fstream>
#include <vector>
#include <strstream>
#include <string>
#include <map>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <assert.h>

using namespace std;

const double PI = 3.14159265358979323846;

class CMyBlock
{
public:
	double dl, dr, du, dd;
	double dArea;
	void SetCondition(double RR);
	void CalculateArea(double RR);
	double CalTri(double RR, double x1, double y1, double x2, double y2);
	int iCondition;
	//0 for totally out of circle
	//1 for totally in the circle
	//2 for partly in the circle
	bool bluIn;
	bool bldIn;
	bool bruIn;
	bool brdIn;

	int iType;//only care when iCondition == 2
	//iType 0: for miss ru
	//iType 1: for miss lu ru
	//iType 2: for miss ru rd
	//iType 3: for miss lu ru rd
};

double CMyBlock::CalTri(double RR, double x1, double y1, double x2, double y2)
{
	double theta1, theta2;
	double tan1, tan2;
	tan1 = y1/x1;
	tan2 = y2/x2;
	theta1 = atan(tan1);
	theta2 = atan(tan2);

	assert(theta1>theta2);
	double theta = theta1 - theta2;
	double dArc = PI * RR * RR * theta / (2 * PI);

	return dArc - 0.5 * x1 * (y1 -  y2) - 0.5 * y2 * (x2 - x1);
}

void CMyBlock::CalculateArea(double RR)
{
	if (iCondition == 0)
	{
		dArea = 0;
	}

	if (iCondition == 1)
	{
		dArea = (du - dd) * (du - dd);
	}

	if (iCondition == 2)
	{
		double x1,y1,x2,y2, dTri;
		switch (iType)
		{
		case 0:
			y1 = du;
			x1 = sqrt(RR*RR-y1*y1);
			x2 = dr;
			y2 = sqrt(RR*RR-x2*x2);
			dTri = CalTri(RR, x1, y1, x2, y2);
			dArea = dTri + (x1-dl)*(y1-dd) + (y2-dd)*(x2-x1);
			break;
		case 1:
			x1 = dl;
			y1 = sqrt(RR*RR-x1*x1);
			x2 = dr;
			y2 = sqrt(RR*RR-x2*x2);
			dTri = CalTri(RR, x1, y1, x2, y2);
			dArea = dTri + (x2-dl)*(y2-dd);
			break;
		case 2:
			y1 = du;
			y2 = dd;
			x1 = sqrt(RR*RR-y1*y1);
			x2 = sqrt(RR*RR-y2*y2);
			dTri = CalTri(RR, x1, y1, x2, y2);
			dArea = dTri + (x1-dl)*(y1-dd);
			break;
		case 3:
			x1 = dl;
			y1 = sqrt(RR*RR-x1*x1);
			y2 = dd;
			x2 = sqrt(RR*RR-y2*y2);
			dTri = CalTri(RR, x1, y1, x2, y2);
			dArea = dTri;
			break;
		}
	}
}

void CMyBlock::SetCondition(double RR)
{
	bool bLU, bLD, bRU, bRD;//if point in the radius
	//lu(dl, du)
	//ld(dl, dd)
	//ru(dr, du);
	//rd(dr, dd);

	if ((dl*dl+dd*dd) >= RR*RR)
	{
		//if left_down is out of range, iCondition = 0
		iCondition = 0;
	}
	else if ((dr*dr+du*du) <= RR*RR)
	{
		//if right_up is in of range, iCondition = 1
		iCondition = 1;
	}
	else
	{
		//else iCondition = 2
		iCondition = 2;
	}

	if (iCondition == 2)
	{
		bLD = true;
		bRU = false;
		if ((dl*dl+du*du) < RR*RR)//LU
			bLU = true;
		else
			bLU = false;
		if ((dr*dr+dd*dd) < RR*RR)//RD
			bRD = true;
		else
			bRD = false;

		if (bLU)
		{
			if (bRD)
			{
				iType = 0;
			}
			else
			{
				iType = 2;
			}
		}
		else
		{
			if (bRD)
			{
				iType = 1;
			}
			else
			{
				iType = 3;
			}
		}
	}
}

void main()
{
	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("C-small.out");

	//cout<<setiosflags(ios::fixed)<<setprecision(6)<<0.2311654987<<endl;

	int iTestNumber;
	ifs>>iTestNumber;

	double f, R, t, r, g, p;
	for (int i=0; i<iTestNumber; i++)
	{
		ifs>>f>>R>>t>>r>>g;
		int abc = 0;
		vector<CMyBlock> vBlockList;

		if (g <= 0.5 * f)//if fly can't go through gap
		{
			p = 1.0;
		}
		else
		{
			//+solve p according to f/R/t/r/g
			double RR = R - (t + f);
			double rr = r + f;
			double gg = g - 2*f;

			int iSquareRows;
			iSquareRows = ceil((RR - rr)/(rr*2 + gg));

			for (int ir = 0; ir<iSquareRows; ir++)
			{
				for (int ic = 0; ic<iSquareRows; ic++)
				{
					//calculate 4 vertex of each square
					double dl, dr, dd, du;
					dl = rr + ic * (rr*2+gg);
					dr = dl + gg;
					dd = rr + ir * (rr*2+gg);
					du = dd + gg;
					CMyBlock mb;
					mb.dd = dd;
					mb.dl = dl;
					mb.dr = dr;
					mb.du = du;
					mb.SetCondition(RR);
					mb.CalculateArea(RR);
					vBlockList.push_back(mb);
				}
			}

			double dSum = 0;
			for (int idx = 0 ;idx<(int)vBlockList.size(); idx++)
			{
				dSum += vBlockList[idx].dArea;
			}

			double dQuArea = 0.25 * PI * R * R;
			p = 1 - (dSum/dQuArea);
			//-solve p according to f/R/t/r/g
			int abc = 0;
		}
		ofs<<"Case #"<<i+1<<": "<<setiosflags(ios::fixed)<<setprecision(6)<<p<<endl;
	}
}