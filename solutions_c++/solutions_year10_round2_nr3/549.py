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

typedef map<string,int> Dirs;
typedef pair<int,int> IntPair;

int calc(int n, IntPair *arr,int order, int pos)
{
  if (pos==n)
  {
    bool bGood=true;
    int iLookPos=order;
    arr[pos].first=1;
    arr[pos].second=order;
    while (bGood && iLookPos>1)
    {
      if (arr[iLookPos].first!=1)
        bGood=false;
      iLookPos=arr[iLookPos].second;
    }
    if (bGood)
      return 1;
    else 
      return 0;
  }
  arr[pos].first=1;
  arr[pos].second=order;
  int iRes1=calc(n,arr,order+1,pos+1);
  arr[pos].first=0;
  arr[pos].second=0;
  int iRes2=calc(n,arr,order,pos+1);
  return ((iRes1+iRes2)%100003);
}

int main(int argc, char* argv[])
{
  int iCases=0;

  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  for (int i=0;i<iCases;i++)
  {
    int n;
    cin >> n;
    IntPair arr[500];
    memset(arr,0,sizeof(arr));
    int iRes=calc(n,arr,1,2);

    cout << "Case #" << i+1 << ": " << iRes << std::endl;
  }
	return 0;
}

