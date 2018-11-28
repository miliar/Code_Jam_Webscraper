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

typedef pair<int,int> Wire;

int main(int argc, char* argv[])
{
  int iCases=0;

  if (argc > 1) 
     freopen(argv[1], "rt", stdin);

  if (argc > 2) 
     freopen(argv[2], "wt", stdout);

  cin >> iCases;

  for (int k=0;k<iCases;k++)
  {
    unsigned int iWireCount=0;
    cin >> iWireCount ;
    Wire wires[1000];

    for (unsigned int g=0;g<iWireCount;g++)
    {
  
      cin>>wires[g].first;
      cin>>wires[g].second;
    }
    int iRes=0;

    for (unsigned int i=0;i<iWireCount;i++)
    {
      for (unsigned int j=i+1;j<iWireCount;j++)
      {
        Wire *A=wires+i;
        Wire *B=wires+j;

        if (A->first>B->first && A->second < B->second)
          iRes++;

        if (A->first<B->first && A->second > B->second)
          iRes++;
        
      }
    }

    cout << "Case #" << k+1 << ": " << iRes << std::endl;
  }
	return 0;
}

