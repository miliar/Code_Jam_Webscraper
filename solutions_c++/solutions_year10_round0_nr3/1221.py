#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
#define MAXN 1010
#define ONLINE

int F[MAXN][2];
int Seq[MAXN];

void PreprocessGroups(int iGroupsNum, int K)
{
	for(int i = 0; i < iGroupsNum; i++)
	{
		int iCurSum = Seq[i];
		int j;
		for(j = (i + 1) % iGroupsNum; j != i; j = (j + 1) % iGroupsNum)
		{
			if(iCurSum + Seq[j] > K) 
			{
				//F[i][0] = iCurSum; F[i][1] = j;
				break;
			}
			iCurSum += Seq[j];
		}
		//if(j == i) { F[i][0] = iCurSum; F[i][1] = j;}
		F[i][0] = iCurSum; F[i][1] = j;
		//cout << F[i][0] << "*****" << F[i][1] << endl;
	}
}

int FindKStep(int start, int count)
{
	int iRet(0);

	while(count--)
	{
		iRet += F[start][0];
		start = F[start][1];
	}
	return iRet;
}
int FindResult(int N, int R)
{
	int iCurStart = 0;

	char flag[MAXN];

	int CycleSum = 0, CycleLen = 0, CycleStart, iTotalLen = 0, iTotalSum(0);
	memset(flag, 0, sizeof(flag));

	while(1)
	{
		if(flag[iCurStart]) {CycleStart = iCurStart;break;}
		flag[iCurStart] = 1;

		//cout << "----->" << iCurStart;
		//CycleSum += F[iCurStart][0];
		//CycleLen++;
		iTotalSum += F[iCurStart][0];
		iCurStart = F[iCurStart][1];
		iTotalLen++;
	}
	
	int iHeadLen(0), iHeadSum(0);
	iCurStart = 0;
	while(1)
	{
		if(iCurStart == CycleStart) break;
		iHeadLen++;
		iHeadSum += F[iCurStart][0];
		iCurStart = F[iCurStart][1];
	}

	CycleLen = iTotalLen - iHeadLen;
	CycleSum = iTotalSum - iHeadSum;

	int iRet = 0;
	iRet = FindKStep(0, min(R, iHeadLen));
	
	if(R > iHeadLen)
	{
		R -= iHeadLen;

		iRet += (R / CycleLen) * CycleSum;
		if(R % CycleLen != 0)
		{
			iRet += FindKStep(CycleStart, R % CycleLen);
		}
		//cout << endl;
		//cout << CycleLen << "******" << CycleSum << endl;
	}
	return iRet;
}

int main()
{
#ifdef ONLINE
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
#endif

	int iCaseTimes, i, j;
	int R, K, N;
	int iResult;
	
	
	scanf("%d", &iCaseTimes);
	
	for(int k = 0; k < iCaseTimes; k++)
	{
		scanf("%d%d%d", &R, &K, &N);
		for(int i = 0; i < N; i++)
		{
			scanf("%d", &Seq[i]);
		}

		PreprocessGroups(N, K);

		
		iResult = FindResult(N, R);
		printf("Case #%d: %d\n", k + 1, iResult);
	}
	return 0;
}