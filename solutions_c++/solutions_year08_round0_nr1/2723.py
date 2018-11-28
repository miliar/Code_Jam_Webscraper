#include "StdAfx.h"
#include "QueryPool.h"

QueryPool::QueryPool(void)
:i_SearchEngineCount(0), i_MaxSeq(0), i_MaxPosition(0)
{
	for (int i=0; i<=MAX_SE_COUNT; i++)
		for (int j=0; j<MAX_QUERY_COUNT+3; j++)
		{
			if (j == (MAX_QUERY_COUNT + 1))
			{
				a_Data[i][j] = 1;			
			}
			else if (j == 0)
			{
				a_Data[i][j] = -1;
			}
			else
			{
				a_Data[i][j] = 10000;	// large number
			}
		}
}

QueryPool::~QueryPool(void)
{
}


void QueryPool::AddSearchEngine(int iSearchEngineKey)
{
	i_SearchEngineCount++;
}

//	iQuery will alway be one of the search engine key
void QueryPool::AddQuery(int iKey, int iSequenceNo)
{
	i_MaxSeq++;

	int iNextPosition = a_Data[iKey][MAX_QUERY_COUNT+1];	//	get next position for key - iKey
	a_Data[iKey][MAX_QUERY_COUNT+1]++;

	a_Data[iKey][iNextPosition] = iSequenceNo;
	a_Data[iKey][MAX_QUERY_COUNT+2] = iSequenceNo;	//	write max

	i_MaxPosition = iNextPosition;		// position of last inserted query
 
	//	reset previous values of next seq
	for (int i=0; i<i_SearchEngineCount; i++)
	{
		if (a_Data[i][iNextPosition + 1] != 10000)
		{
			a_Data[i][iNextPosition] = a_Data[i][MAX_QUERY_COUNT+2];
			for (int k=(iNextPosition+1); k<(MAX_QUERY_COUNT+1); k++)
				a_Data[i][k] = 10000;	// set to large number

			if ((a_Data[i][MAX_QUERY_COUNT + 1]) > iNextPosition)
				a_Data[i][MAX_QUERY_COUNT + 1] = iNextPosition + 1;
		}
	}
}

int	QueryPool::GetNumberOfSwitchesRequired()
{
	int iNumberOfSwitches = 0;

	for (int i=1; i<=(i_MaxPosition+1); i++)	//	Position index
	{
		//	find max
		int iMaxKey = -1;
		int iMaxPosition = 0;
		for (int j=0; j<i_SearchEngineCount; j++)	// key
		{
			int iData = a_Data[j][i-1];
			if (iData == -1)
				iData = a_Data[j][i];

			if (iMaxPosition < iData)
			{
				iMaxKey = j;
				iMaxPosition = iData;
			}
		}

		//	market covered values as -1
		for (int j=0; j<i_SearchEngineCount; j++)	// key
		{
			if (j == iMaxKey)
				continue;

			if (a_Data[j][i-1] != -1)
				a_Data[j][i-1] = -1;

			if (a_Data[j][i] != -1 && a_Data[j][i] < iMaxPosition)
				a_Data[j][i] = -1;

/*			if (a_Data[j][i-1] != -1)
				a_Data[j][i-1] = -1;
			else
				a_Data[j][i] = -1;*/
		}

		iNumberOfSwitches++;
		if (iMaxPosition == 10000)
			break;

		if (a_Data[iMaxKey][i-1] != -1)
			--i;
	}

	return --iNumberOfSwitches;	// don't count first select for the switch count
}

/*int	QueryPool::GetNumberOfSwitchesRequired()
{	
	int iNumberOfSwitches = 0;

	int iPreviousMaxKey = -1;
	int iPreviousMaxPosition = -1;

	int iPreviousAbsMaxPosition = 0;
	int iPreviousAbsMaxKey = -1;

	for (int i=0; i<=i_MaxPosition; i++)	//	Position index
	{
		//	find max
		int iMaxPosition = 0;
		int iMaxKey = -1;
		int bBlackFound = false;

		int iAbsMaxPosition = 0;
		int iAbsMaxKey = -1;

		for (int j=0; j<i_SearchEngineCount; j++)	// Key index
		{
			int iData = a_Data[j][i];

			if (iData == 0)
			{
				bBlackFound = true;
				break;
			}

			if (iPreviousMaxPosition < iData)	// found a key with max position within position index (i) excluding iPreviousMaxKey
			{
				if (iMaxPosition < iData && iPreviousMaxKey != j && iPreviousAbsMaxKey != j)
				{
					iMaxPosition = iData;
					iMaxKey = j;
				}

				if (iAbsMaxPosition < iData)
				{
					iAbsMaxPosition = iData;
					iAbsMaxKey = j;
				}
			}
		}

		iNumberOfSwitches++;

		if (bBlackFound == true)
			break;

		//	this can only happen if two search key scenario
		if (iMaxKey == -1)
		{
			i--;	// stick to same raw
			// do something
		}
		else
		{
			iPreviousMaxKey = iMaxKey;
			iPreviousMaxPosition = iMaxPosition;

			iPreviousAbsMaxKey = iAbsMaxKey;
			iPreviousAbsMaxPosition = iAbsMaxPosition;
		}
	}

	return --iNumberOfSwitches;	// remove first switch
}*/