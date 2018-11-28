// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
  int iLines=0;

  cin >> iLines;
  int aSnappers[30];

  for (int i=0;i<iLines;i++)
  {
    unsigned int iSnapers=0,iTrials=0;
    cin >> iSnapers >> iTrials;

    unsigned int iPower=1<<iSnapers;

    bool bFinalPower=false;
    if ((iTrials+1)%iPower==0)
      bFinalPower=true;

/*    memset(aSnappers,0,sizeof(aSnappers));

    for (int j=0;j<iTrials;j++)
    {

      bool bHasPower=true;
      int k=0;
      for (k=0;k<iSnapers && bHasPower;k++)
      {
        bool bSnapperPowered=bHasPower;

        if (aSnappers[k]==0)
        {
          bHasPower=false;
        }

        if (bSnapperPowered)
          aSnappers[k]=1-aSnappers[k];
      }
    }

    bFinalPower=true;
    for (int k=0;k<iSnapers && bFinalPower;k++)
    {
        if (aSnappers[k]==0)
        {
          bFinalPower=false;
        }
    }
*/
    cout << "Case #" << i+1 << ": " << ((bFinalPower)?"ON":"OFF") << std::endl;
  }
	return 0;
}

