#include <iostream>
#include <fstream>
#include <vector>
#include <strstream>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

class CTrainTime
{
public:
	int h;
	int m;
	bool bIn; //1 for in; 0 for out
	void Normalize();
	CTrainTime(){}
	CTrainTime(int _h, int _m, bool _bIn)
	{
		h = _h;
		m = _m;
		bIn = _bIn;
	}
};

void CTrainTime::Normalize()
{
	while (m>=60)
	{
		m-=60;
		h++;
	}
}

bool LessTime(const CTrainTime &a, const CTrainTime &b)
{
	if (a.h == b.h && a.m == b.m && a.bIn == b.bIn)
	{
		return false;
	}

	if (a.h < b.h)
	{
		return true;
	}
	else if (a.h == b.h)
	{
		if (a.m < b.m)
		{
			return true;
		}
		else if (a.m == b.m)
		{
			if (a.bIn)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		else
		{
			return false;
		}
	}
	else
	{
		return false;
	}
}

void main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");

	int iTestNumber;
	ifs>>iTestNumber;
	for (int i=0; i<iTestNumber; i++)
	{
		//start big loop
		int iTurnTime;
		ifs>>iTurnTime;
		int NA, NB;
		ifs>>NA>>NB;

		vector<CTrainTime> vTimeForA, vTimeForB;
		vTimeForA.resize(NA+NB);
		vTimeForB.resize(NA+NB);

		for(int ia=0; ia<NA; ia++)
		{
			int beginh, beginm, endh, endm;
			char temp;
			ifs>>beginh>>temp>>beginm;
			ifs>>endh>>temp>>endm;
			//cout<<beginh<<" "<<beginm<<" "<<endh<<" "<<endm<<endl;
			vTimeForA[ia].h = beginh;
			vTimeForA[ia].m = beginm;
			vTimeForA[ia].bIn = false;

			vTimeForB[ia].h = endh;
			vTimeForB[ia].m = endm + iTurnTime;
			vTimeForB[ia].bIn = true;
			vTimeForB[ia].Normalize();
		}

		for(int ib=0; ib<NB; ib++)
		{
			int beginh, beginm, endh, endm;
			char temp;
			ifs>>beginh>>temp>>beginm;
			ifs>>endh>>temp>>endm;
			//cout<<beginh<<" "<<beginm<<" "<<endh<<" "<<endm<<endl;
			vTimeForB[ib+NA].h = beginh;
			vTimeForB[ib+NA].m = beginm;
			vTimeForB[ib+NA].bIn = false;

			vTimeForA[ib+NA].h = endh;
			vTimeForA[ib+NA].m = endm + iTurnTime;
			vTimeForA[ib+NA].bIn = true;
			vTimeForA[ib+NA].Normalize();
		}
		
		//use vTimeForA and vTimeForB
		sort(vTimeForA.begin(), vTimeForA.end(), LessTime);
		sort(vTimeForB.begin(), vTimeForB.end(), LessTime);

		int iNeededA = 0;
		int iHasA = 0;
		int iNeededB = 0;
		int iHasB = 0;

		for (int j=0; j<NA+NB; j++)
		{
			if (vTimeForA[j].bIn)
			{
				iHasA++;
			}
			else
			{
				if (iHasA > 0)
				{
					iHasA--;
				}
				else
				{
					iNeededA++;
				}
			}

			if (vTimeForB[j].bIn)
			{
				iHasB++;
			}
			else
			{
				if (iHasB > 0)
				{
					iHasB--;
				}
				else
				{
					iNeededB++;
				}
			}

		}
		ofs<<"Case #"<<i+1<<": "<<iNeededA<<" "<<iNeededB<<endl;
		//end big loop
	}
}