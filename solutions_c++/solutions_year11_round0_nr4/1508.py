// prob1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <map>
#include <string>


using namespace std;



int main(int argc, char* argv[])
{
  int iCases=0;

  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;


  cout.precision(6); 

  for (int i=0;i<iCases;i++)
  {
    vector<int> vInput;
    vector<int> vSorted;
    int iElementCnt;
    cin >> iElementCnt;
    vInput.resize(iElementCnt);
    vSorted.resize(iElementCnt);

    for (int j=0;j<iElementCnt;j++)
    {
      int iElem;
      cin >> iElem;
      vInput[j]=iElem;
      vSorted[j]=iElem;
    }

    sort(vSorted.begin(), vSorted.end());
     
    int iOutOfPlace=0;
      
    for (int k=0;k<iElementCnt;k++)
    {
      if (vInput[k]!=vSorted[k])
      {
        iOutOfPlace++;
      }
    }
    double dTries=iOutOfPlace;
    cout << "Case #" << i+1 << ": " << fixed      << dTries << std::endl;
  }
	return 0;
}

