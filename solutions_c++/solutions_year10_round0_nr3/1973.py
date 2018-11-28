// ThemePark.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <map>
#include <fstream>

std::map<unsigned int, unsigned int> StartPointsMap;
std::vector<__int64> StartPoints;

__int64 GetProfit(unsigned int R, __int64 k, const std::vector<unsigned int> groups)
{
	if ( (R == 0) || (k == 0) || (groups.size() == 0) )
	{
		return 0;
	}
	
	StartPointsMap.clear();
	StartPoints.clear();

	__int64 nProfit = 0;
	unsigned int nStartIndex = 0;
	unsigned int nRidesForDay = 0;

	while (nRidesForDay < R)
	{
		std::map<unsigned int, unsigned int>::const_iterator it = StartPointsMap.find(nStartIndex);
		if ( it != StartPointsMap.end() )
		{
			unsigned int nIdx = it->second, nCountInLoop = StartPoints.size() - nIdx;
			unsigned int nFullLoops = (R - nRidesForDay) / nCountInLoop, nRem = (R - nRidesForDay) % nCountInLoop;
			__int64 nRemAmount = 0, nAmountPerLoop = 0;

			for (unsigned int i = nIdx; i < nIdx + nRem; ++i)
			{
				nRemAmount += StartPoints[i];
			}
			nAmountPerLoop = nRemAmount;
			for (unsigned int i = nIdx + nRem; i < StartPoints.size(); ++i)
			{
				nAmountPerLoop += StartPoints[i];
			}

			return nProfit + nAmountPerLoop * nFullLoops + nRemAmount;
		}
		else
		{
			__int64 nCurrentCount = 0;
			unsigned int nIdx = nStartIndex;
			do
			{
				nCurrentCount += groups[nStartIndex];
				if ( ++nStartIndex >= groups.size() )
				{
					nStartIndex = 0;
				}
			}
			while ( (nIdx != nStartIndex) && ((nCurrentCount + groups[nStartIndex]) <= k) );

			StartPoints.push_back(nCurrentCount);
			StartPointsMap[nIdx] = StartPoints.size() - 1;
			nProfit += nCurrentCount;
			++nRidesForDay;
		}
	}
	
	return nProfit;
}

int main(int argc, char * argv[])
{
	unsigned int t = 0;

	std::ifstream fIn("C-large.in");
	fIn >> t;

	std::ofstream fOut("C-large.out");

	for (unsigned int i = 0; i < t; ++i)
	{
		__int64 k = 0;
		unsigned int N = 0, R = 0;
		fIn >> R >> k >> N;

		std::vector<unsigned int> groups;
		for (unsigned int j = 0; j < N; ++j)
		{
			unsigned int g = 0;
			fIn >> g;
			groups.push_back(g);
		}

		fOut << "Case #" << i + 1 << ": " << GetProfit(R, k, groups) << std::endl;
		fOut.flush();
	}

	fOut.close();
	fIn.close();
	
	return 0;
}

