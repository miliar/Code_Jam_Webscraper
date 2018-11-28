
#include <algorithm>
#include <string>
#include <iostream>
#include <fstream>

struct TrainTime
{
	int		m_DepartureTime;
	int		m_ArrivalTime;
	bool	m_bStarted;

	TrainTime()
		: m_DepartureTime(0)
		, m_ArrivalTime(0)
		, m_bStarted(false)
	{
	}

	bool operator < (TrainTime& rhs)
	{
		return (m_DepartureTime < rhs.m_DepartureTime);
	}
};

void IsNextTime(TrainTime* pTrainTime1, int iStartIndex1, int iMaxNum1, TrainTime* pTrainTime2, int iStartIndex2, int iMaxNum2)
{
	for (int i = iStartIndex2; i < iMaxNum2; ++i)
	{
		if (pTrainTime1[iStartIndex1].m_ArrivalTime <= pTrainTime2[i].m_DepartureTime && 
			false == pTrainTime2[i].m_bStarted)
		{
			pTrainTime2[i].m_bStarted = true;
			IsNextTime(pTrainTime2, i, iMaxNum2, pTrainTime1, iStartIndex1 + 1, iMaxNum1);
			break;
		}
	}
}

int main()
{
	std::ifstream inputFile;
	inputFile.open("B-large.in");
	std::ofstream outputFile;
	outputFile.open("B-large.out");

	std::string strTemp;

	std::getline(inputFile, strTemp);
	int iCaseNum = atoi(strTemp.c_str());

	for (int i = 0; i < iCaseNum; ++i)
	{
		int iStartNum[2] = { 0, };

		std::getline(inputFile, strTemp);
		int iTurnArroundTime = atoi(strTemp.c_str());

		int iTimeNum[2];

		std::getline(inputFile, strTemp);
		int iSeperator = strTemp.find(" ");

		iTimeNum[0] = atoi(strTemp.substr(0, iSeperator).c_str());
		iTimeNum[1] = atoi(strTemp.substr(iSeperator + 1, strTemp.length() - iSeperator).c_str());

		TrainTime* pTrainTime[2];
		pTrainTime[0] = new TrainTime[iTimeNum[0]];
		pTrainTime[1] = new TrainTime[iTimeNum[1]];

		for (int j = 0; j < 2; ++j)
		{
			for (int k = 0; k < iTimeNum[j]; ++k)
			{
				std::getline(inputFile, strTemp);
				int iSeperator = strTemp.find(" ");
				
				std::string strDepartureTime = strTemp.substr(0, iSeperator);
				std::string strArrivalTime = strTemp.substr(iSeperator + 1, strTemp.length() - iSeperator);

				iSeperator = strDepartureTime.find(":");
				pTrainTime[j][k].m_DepartureTime = atoi(strDepartureTime.substr(0, iSeperator).c_str()) * 60 + 
					atoi(strDepartureTime.substr(iSeperator + 1, strDepartureTime.length() - iSeperator).c_str());
				iSeperator = strArrivalTime.find(":");
				pTrainTime[j][k].m_ArrivalTime = atoi(strArrivalTime.substr(0, iSeperator).c_str()) * 60 + 
					atoi(strArrivalTime.substr(iSeperator + 1, strArrivalTime.length() - iSeperator).c_str()) + iTurnArroundTime;
			}

			std::sort(pTrainTime[j], pTrainTime[j] + iTimeNum[j]);
		}

		int iAIndex = 0;
		int iBIndex = 0;

		while (iAIndex != iTimeNum[0] && iBIndex != iTimeNum[1])
		{
			if (true == pTrainTime[0][iAIndex].m_bStarted)
			{
				++iAIndex;
				continue;
			}
			if (true == pTrainTime[1][iBIndex].m_bStarted)
			{
				++iBIndex;
				continue;
			}

			if (pTrainTime[0][iAIndex].m_DepartureTime < pTrainTime[1][iBIndex].m_DepartureTime)
			{
				++iStartNum[0];
				pTrainTime[0][iAIndex].m_bStarted = true;
				IsNextTime(pTrainTime[0], iAIndex, iTimeNum[0], pTrainTime[1], iBIndex, iTimeNum[1]);
			}
			else
			{
				++iStartNum[1];
				pTrainTime[1][iBIndex].m_bStarted = true;
				IsNextTime(pTrainTime[1], iBIndex, iTimeNum[1], pTrainTime[0], iAIndex, iTimeNum[0]);
			}
		}

		for (int j = 0; j < 2; ++j)
		{
			for (int k = 0; k < iTimeNum[j]; ++k)
			{
				if (false == pTrainTime[j][k].m_bStarted)
				{
					++iStartNum[j];
				}
			}
		}

		outputFile << "Case #" << i + 1 << ": " << iStartNum[0] << " " << iStartNum[1] << std::endl;

		for (int j = 0; j < 2; ++j)
		{
			delete [] pTrainTime[j];
		}
	}

	outputFile.close();
	inputFile.close();

	return 0;
}

