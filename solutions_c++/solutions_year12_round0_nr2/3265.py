#include <cstdio>
using namespace std;

int isSurprisingTriplet(int score, int iMinBest)
{
	int iSecond;
	int iThird;
	int iDiff;
	int retVal = 0;

	do
	{
		iSecond = iMinBest - 2;
		iThird = score - (iMinBest + iSecond);

		if(iThird >= 0)
		{
			iDiff = iMinBest - iThird;

			if(iDiff >= 0 && iDiff <= 2)
			{
				retVal = 1;
				break;
			}

			iMinBest++;
		}
		else
			break;

	} while(iDiff < 2 && iMinBest <= 10);

	return retVal;
}

int isNormalTriplet(int score, int minBest)
{
	int bGotoSameCheck;
	int iSecond;
	int iThird;
	int iDiff;
	int retVal = 0;

	while(minBest <= 10)
	{
		iSecond = minBest - 1;
		bGotoSameCheck = 0;
		iThird = score - (minBest + iSecond);

		if(iThird >= 0)
		{
			iDiff = minBest - iThird;

			if(iDiff >= 0 && iDiff < 2)
			{
				retVal = 1;
				break;
			}
			else if(iDiff < 0)
				bGotoSameCheck = 1;
		}

		if(bGotoSameCheck)
		{
			iSecond = minBest;
			iThird = score - (minBest + iSecond);

			if(iThird >= 0)
			{
				iDiff = minBest - iThird;

				if(iDiff >= 0 && iDiff < 2)
				{
					retVal = 1;
					break;
				}
			}
		}

		minBest++;
	}
	
	return retVal;
}

int main()
{
	int iNumTestCases;
	int iNumScores;
	int iNumSurp;
	int iAtleastBest;
	//int iScores[100];
	int isSurprising[100];
	int isNormal[100];
	int iCurScore;

	int iTestCaseIndex;
	int iScoreIndex;

	int iReqGooglers;
	int iBestPossible;
	int bFirstValid;
	int iSurpFound;
	int iDiffSurp;
	int iDiff;

	scanf("%d", &iNumTestCases);

	for(iTestCaseIndex = 0; iTestCaseIndex < iNumTestCases; iTestCaseIndex++)
	{
		iReqGooglers = 0;
		iSurpFound = 0;
		
		scanf("%d %d %d", &iNumScores, &iNumSurp, &iAtleastBest);

		for(iScoreIndex = 0; iScoreIndex < iNumScores; iScoreIndex++)
		{
			scanf("%d", &iCurScore);
			iBestPossible = iAtleastBest;
			bFirstValid = 0;
			
			while(!bFirstValid && iBestPossible <= 10)
			{
				iDiff = iCurScore - iBestPossible;

				if(iDiff < 0)
					break;

				if(iDiff - (iDiff / 2) <= iBestPossible)
				{
					bFirstValid = 1;
				}
				else
					iBestPossible++;
			}

			if(!bFirstValid)
			{
				isSurprising[iScoreIndex] = 0;
				isNormal[iScoreIndex] = 0;
				continue;
			}

			// Check for surprising triplet
			if(isSurprisingTriplet(iCurScore, iBestPossible))
				isSurprising[iScoreIndex] = 1;
			else
				isSurprising[iScoreIndex] = 0;
			
			// Check for normal triplet
			if(isNormalTriplet(iCurScore, iBestPossible))
				isNormal[iScoreIndex] = 1;
			else
				isNormal[iScoreIndex] = 0;
		}

		// Now let's find out maximum number of Googlers
		for(iScoreIndex = 0; iScoreIndex < iNumScores; iScoreIndex++)
		{
			if(isSurprising[iScoreIndex] && !isNormal[iScoreIndex])
				iSurpFound++;
		}

		iDiffSurp = iNumSurp - iSurpFound;

		if(iDiffSurp >= 0)
		{
			for(iScoreIndex = 0; iScoreIndex < iNumScores; iScoreIndex++)
			{
				if(isNormal[iScoreIndex] && isSurprising[iScoreIndex])
				{
					if(iDiffSurp)
						iDiffSurp--;
					else
						isSurprising[iScoreIndex] = 0;
				}
			}
		}
		else
		{
			iDiffSurp = -iDiffSurp;

			for(iScoreIndex = 0; iScoreIndex < iNumScores; iScoreIndex++)
			{
				if(isSurprising[iScoreIndex] && !isNormal[iScoreIndex])
				{
					if(iDiffSurp)
					{
						iDiffSurp--;
						isSurprising[iScoreIndex] = 0;
					}
				}

				if(isNormal[iScoreIndex] && isSurprising[iScoreIndex])
					isSurprising[iScoreIndex] = 0;
			}
		}

		for(iScoreIndex = 0; iScoreIndex < iNumScores; iScoreIndex++)
			if(isNormal[iScoreIndex] || isSurprising[iScoreIndex])
				iReqGooglers++;

		printf("Case #%d: %d\n", iTestCaseIndex + 1, iReqGooglers);
	}
}