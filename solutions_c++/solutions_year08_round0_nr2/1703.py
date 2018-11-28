#include "stdafx.h"

#include <vector>
#include <string>
#include <fstream>
 
using namespace std;

struct STrip{
	STrip(int iDeparture_, int iArrival_)
		:iDeparture(iDeparture_), iArrival(iArrival_)
	{
	}

	int iDeparture;
	int iArrival;
};

class CCase{
public:
	CCase(int iTurnAroundTime, vector<STrip> a2b, vector<STrip> b2a)
		:m_iTurnAroundTime(iTurnAroundTime), m_a2b(a2b), m_b2a(b2a)
	{
	}

	int m_iTurnAroundTime;
	vector<STrip>	m_a2b;
	vector<STrip>	m_b2a;
};

string SolveCase(const CCase& Case, vector<CCase>::size_type iCaseIndex);
int FindArrived(const vector<STrip>& Trips, int iCurTime, int iTurnAroundTime);
int FindDepartured(const vector<STrip>& Trips, int iCurTime);
void ParseInput(string sInput, vector<CCase>* pInput);
int ParseTime(string sTime);
string IntToString(int i);

string SolveTrainTimetable()
{
	string
		sOutput;
	vector<CCase>
		Input;
	ParseInput("Input.txt", &Input);

	vector<CCase>::size_type
		i;
	for (i = 0; i < Input.size(); ++i)
		sOutput += SolveCase(Input[i], i) + "\n";

	return sOutput;
}

void ParseInput(string sInputFile, vector<CCase>* pInput)
{
	ifstream
		is(sInputFile.c_str());
	int
		iCaseCount;
	is >> iCaseCount;

	for (int i = 0; i < iCaseCount; ++i){
		int
			iTurnAroundTime, ia2bCount, ib2aCount;
		is >> iTurnAroundTime;
		is >> ia2bCount;
		is >> ib2aCount;

		vector<STrip>
			a2bTrips;
		for (int j = 0; j < ia2bCount; ++j){
			string
				sDeparture;
			is >> sDeparture;
			int
				iDeparture = ParseTime(sDeparture);

			string
				sArrival;
			is >> sArrival;
			int
				iArrival = ParseTime(sArrival);

			a2bTrips.push_back(STrip(iDeparture, iArrival));
		}

		vector<STrip>
			b2aTrips;
		for (int j = 0; j < ib2aCount; ++j){
			string
				sDeparture;
			is >> sDeparture;
			int
				iDeparture = ParseTime(sDeparture);

			string
				sArrival;
			is >> sArrival;
			int
				iArrival = ParseTime(sArrival);

			b2aTrips.push_back(STrip(iDeparture, iArrival));
		}

		pInput->push_back(CCase(iTurnAroundTime, a2bTrips, b2aTrips));
	}
}

int ParseTime(string sTime)
{
	int
		iHour = (sTime[0] - '0') * 10 + (sTime[1] - '0'),
		iMinute = (sTime[3] - '0') * 10 + (sTime[4] - '0');

	return iHour * 60 + iMinute;
}

string SolveCase(const CCase& Case, vector<CCase>::size_type iCaseIndex)
{
	string
		sOutput;
	int
		iFromACount = 0,
		iFromBCount = 0;
	int
		iInA = 0,
		iInB = 0,
		iCurTime = 0;

	for (int iCurTime = 0; iCurTime < 24*60; ++iCurTime){
		vector<STrip>::const_iterator
			it;
		int
			iArrivedCount = FindArrived(Case.m_a2b, iCurTime, Case.m_iTurnAroundTime);
		iInB += iArrivedCount;

		iArrivedCount = FindArrived(Case.m_b2a, iCurTime, Case.m_iTurnAroundTime);
		iInA += iArrivedCount;

		int
			iDeparturedCount = FindDepartured(Case.m_a2b, iCurTime);
		iInA -= iDeparturedCount;

		iDeparturedCount = FindDepartured(Case.m_b2a, iCurTime);
		iInB -= iDeparturedCount;

		if (iInA < 0 && -iInA > iFromACount)
			iFromACount = -iInA;

		if (iInB < 0 && -iInB > iFromBCount)
			iFromBCount = -iInB;
	}

	sOutput = "Case #" + IntToString(iCaseIndex + 1) + ": " + IntToString(iFromACount)
		+ " " + IntToString(iFromBCount);

	return sOutput;
}

int FindArrived(const vector<STrip>& Trips, int iCurTime, int iTurnAroundTime)
{
	int
		iArrivedCount = 0;

	vector<STrip>::const_iterator
		it;
	for (it = Trips.begin(); it != Trips.end(); ++it)
	{
		if (it->iArrival + iTurnAroundTime == iCurTime)
			++iArrivedCount;
	}

	return iArrivedCount;
}

int FindDepartured(const vector<STrip>& Trips, int iCurTime)
{
	int
		iDeparturedCount = 0;

	vector<STrip>::const_iterator
		it;
	for (it = Trips.begin(); it != Trips.end(); ++it)
	{
		if (it->iDeparture == iCurTime)
			++iDeparturedCount;
	}

	return iDeparturedCount;
}

string IntToString(int i)
{
	char
		arch[64];
	string
		s	= _itoa(i, arch, 10);

    return s;
}

// #include <vector>
// #include <string>
// 
// using namespace std;
// 
// class Bishops{
// public:
// 	int count(int k, vector <string> board)
// 	{
// 		vector<char>
// 			vBoard(board.size() * board.size());
// 		for (int i = 0; i < board.size(); ++i)
// 			for (int j = 0; j < board.size(); ++j)
// 				vBoard[i + j * board.size()] = board[i][j];
// 
// 		return count(k, vBoard, board.size(), 0, 0);
// 	}
// 
// 	int count(int k, const vector<char>& vBoard, int iSize, int iMin, int jMin)
// 	{
// 		int
// 			iCount = 0;
// 
// 		if (k == 0)
// 			iCount = 1;
// 		else{
// 			for (int i = 0; i < iSize; ++i){
// 				for (int j = 0; j < iSize; ++j){
// 					if (i + j >= iMin + jMin && vBoard[i + j * iSize] == '.'){
// 						if (k == 1)
// 							iCount++;
// 						else{
// 							vector<char>
// 								vboard2 = vBoard;
// 							vboard2[i + j * iSize] = 'b';
// 
// 							int i2 = i;
// 							int j2 = j;
// 							while (++i2 < iSize && ++j2 < iSize)
// 								vboard2[i2 + j2 * iSize] = '0';
// 
// 							i2 = i;
// 							j2 = j;
// 							while (--i2 >= 0 && ++j2 < iSize)
// 								vboard2[i2 + j2 * iSize] = '0';
// 
// 							i2 = i;
// 							j2 = j;
// 							while (--i2 >= 0 && --j2 >= 0)
// 								vboard2[i2 + j2 * iSize] = '0';
// 
// 							i2 = i;
// 							j2 = j;
// 							while (++i2 < iSize && --j2 >= 0)
// 								vboard2[i2 + j2 * iSize] = '0';
// 
// 							iCount += count(k - 1, vboard2, iSize, i, j);
// 						}
// 					}
// 				}
// 			}
// 		}
// 
// 		return iCount % 10000;
// 	}
// };
// 
// class ConnectingAsteroids{
// public:
// 	double getMinimumCost(vector <int> x, vector <int> y, vector <int> z){
// 		double
// 			dbMax = 0;
// 		for (int i = 0; i < int(x.size()); ++i){
// 			for (int i2 = 0; i2 < int(x.size()); ++i2){
// 				if (i != i2){
// 					double
// 						dbCur = sqrt(double(
// 							double(x[i] - x[i2]) * (x[i] - x[i2])
// 							+ double(y[i] - y[i2]) * (y[i] - y[i2])
// 							+ double(z[i] - z[i2]) * (z[i] - z[i2])));
// 					if (dbCur > dbMax)
// 						dbMax = dbCur;
// 				}
// 			}			
// 		}
// 
// 		double
// 			dbMin = 0;
// 		bool
// 			bFirst = true;
// 		for (int i = 0; i < int(x.size()); ++i){
// 			double
// 				dbCurMax = 0;
// 			for (int i2 = 0; i2 < int(x.size()); ++i2){
// 				if (i != i2){
// 					double
// 						dbCur = sqrt(double(
// 							(x[i] - x[i2]) * (x[i] - x[i2])
// 							+ (y[i] - y[i2]) * (y[i] - y[i2])
// 							+ (z[i] - z[i2]) * (z[i] - z[i2])));
// 					if (dbCur > dbCurMax)
// 						dbCurMax = dbCur;
// 				}
// 			}			
// 
// 			if (bFirst || dbCurMax - dbMax / 2 < dbMin){
// 				dbMin = dbCurMax - dbMax / 2;
// 				bFirst = false;
// 			}
// 		}
// 
// 		return dbMin < 0 ? 0.0 : dbMin;
// 	}
// };

// class Alphabet{
// public:
// 	int choices(string decree){
// 		vector<int>
// 			viPosCounts;
// 		viPosCounts.push_back(1);
// 
// 		int
// 			iResult;
// 
// 		for (int iRule = 0; iRule < decree.length(); iRule++){
//             int
// 				iFrom, iTo, iStep;
// 
// 			if (decree[iRule] == 'B'){
// 				viPosCounts.push_back(0);
// 				iFrom	= viPosCounts.size() - 1;
// 				iTo		= 0;
// 			}
// 			else{
// 				viPosCounts.insert(viPosCounts.begin(), 0);
// 				iFrom	= 0;
// 				iTo		= viPosCounts.size() - 1;
// 			}
// 			iStep	= iFrom < iTo ? 1 : -1;
// 
// 			for (int iPos = iFrom; iPos != iTo + iStep ; iPos += iStep){
// 				int
// 					iPosCount	= 0;
// 				for (int iPos2 = iPos + iStep; iPos2 != iTo + iStep; iPos2 += iStep)
//                     iPosCount	+= viPosCounts[iPos2];
//                 viPosCounts[iPos]	= iPosCount;
// 			}
// 
// 			iResult	= 0;
// 			for (int i = 0; i < viPosCounts.size(); i++)
// 				iResult	+= viPosCounts[i];
// 			if (iResult > 1000000000){
// 				iResult	= -1;
// 				break;
// 			}
//         }
// 
// 
// 		return iResult;
// 	}
// };

//class SPlan{
//public:
//	SPlan(string sPlan){
//		iFee = atoi(sPlan.c_str());
//
//		sPlan = sPlan.substr(sPlan.find(' ') + 1);
//		iFreeMinutes = atoi(sPlan.c_str());
//
//		sPlan = sPlan.substr(sPlan.find(' ') + 1);
//		iMinuteCost = atoi(sPlan.c_str());
//
//		sPlan = sPlan.substr(sPlan.find(' ') + 1);
//        bOff	= sPlan[0] == 'T';
//	}		
//
//	double GetCost(vector<int> peakMinutes, vector<int> offMinutes){
//		double
//			iCost	= 0;
//
//		for (int i = 0; i < peakMinutes.size(); ++i){
//			int
//				iTotalPaidMinutes	= (!bOff ? offMinutes[i] : 0) + peakMinutes[i],
//				iPaidMinutes	= iTotalPaidMinutes - iFreeMinutes;
//			if (iPaidMinutes < 0)
//				iPaidMinutes	= 0;
//			iCost	+= iFee + iPaidMinutes * iMinuteCost;
//		}
//
//		return iCost;
//	}
//
//private:
//	int iFee;
//	int iFreeMinutes;
//	int iMinuteCost;
//	bool bOff;
//};
//
//class CellPlans{
//public:
//	int cheapest(vector<string> plans, vector<int> peakMinutes, vector<int> offMinutes){
//		double iMinCost = 0;
//		int iBestPlan = 0;
//
//		for (int i = 0; i < plans.size(); ++i){
//			SPlan
//				Plan(plans[i]);
//			double iCurPlanCost = Plan.GetCost(peakMinutes, offMinutes);
//
//			if (i == 0 || iMinCost > iCurPlanCost){
//				iBestPlan = i;
//				iMinCost  = iCurPlanCost;
//			}
//		}
//
//		return iBestPlan;
//	}
//};
//
//
//
