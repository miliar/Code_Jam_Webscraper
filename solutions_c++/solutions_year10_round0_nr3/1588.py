// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef queue<int>   IntQueue;

typedef vector<pair<IntQueue,int>> StateVec;

__int64 calcEarnings(int iRuns, int iCapacity, IntQueue &oGroups)
{
  __int64  iRes=0;
  IntQueue TempQueue;

  StateVec sVec;

  for (int i=0;i<iRuns;i++)
  {
    IntQueue TmpQueue(oGroups);

    int iProfitThisRun=0;
    int iLeft=iCapacity;
    while (iLeft>0)
    {
      if (oGroups.size()==0)
        break;

      int iNextGroup=oGroups.front();
      if (iLeft>=iNextGroup)
      {
        oGroups.pop();
        TempQueue.push(iNextGroup);
        iLeft-=iNextGroup;
        iProfitThisRun+=iNextGroup;
      }
      else
        break;
    }

    while (!TempQueue.empty())
    {
      oGroups.push(TempQueue.front());
      TempQueue.pop();
    }

    
    for (unsigned int j=0;j<sVec.size();j++)
    {
      if (sVec[j].first==TmpQueue)
      {
        __int64 iFullCycleProfit=0;
        unsigned int iCyclePeriod=sVec.size()-j;

        for (unsigned int k=j;k<sVec.size();k++)
          iFullCycleProfit+=sVec[k].second;

        int iRunsLeft=(iRuns-i);
        __int64  iCompleteCyclesMod=iRunsLeft%iCyclePeriod;
        __int64  iCompleteCyclesDiv=iRunsLeft/iCyclePeriod;
        iRes+=(iFullCycleProfit*iCompleteCyclesDiv);

        for (unsigned int l=j;l<(j+iCompleteCyclesMod);l++)
          iRes+=sVec[l].second;

        return iRes;
      }
    }

    sVec.push_back(std::make_pair(TmpQueue,iProfitThisRun));
    

    /*cout << "Run: " << i << " Profit:" << iProfitThisRun;
    {
      IntQueue PrintQueue(oGroups);
      cout << " Queue: ";
      while (!PrintQueue.empty())
      {
        cout << PrintQueue.front();
        cout << " ";
        PrintQueue.pop();
      }
      cout << std::endl;
    }*/

    iRes+=iProfitThisRun;
  }

  return iRes;
}

int _tmain(int argc, _TCHAR* argv[])
{
  int iCases=0;

  cin >> iCases;

  for (int i=0;i<iCases;i++)
  {
    unsigned int iRuns=0,iCapacity=0,iGroups=0;
    cin >> iRuns >> iCapacity >> iGroups;
    IntQueue oGroups;

    for (unsigned int g=0;g<iGroups;g++)
    {
      int iCount;
      cin>>iCount;
      oGroups.push(iCount);
    }

    __int64 iEuros=calcEarnings(iRuns, iCapacity, oGroups);
    cout << "Case #" << i+1 << ": " << iEuros << std::endl;
  }
	return 0;
}

