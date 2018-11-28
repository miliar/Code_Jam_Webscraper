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
    unsigned int iExistCount=0,iNewCount=0;
    cin >> iExistCount >> iNewCount;
    Dirs oDirs;

    for (unsigned int g=0;g<iExistCount;g++)
    {
      string sDir;
      cin>>sDir;
      int pos=1;
      int iLen=sDir.length();
      while (pos<=iLen)
      {
        int loc=sDir.find("/",pos);
        if (loc==-1)
          loc=sDir.length();
        string sPath=sDir.substr(0,loc);
        oDirs.insert(pair<string,int>(sPath,1));
        pos=loc+1;
      }
    }

    int iRes=0;
    for (unsigned int g=0;g<iNewCount;g++)
    {
      string sDir;
      cin>>sDir;
      int pos=1;
      int iLen=sDir.length();
      while (pos<=iLen)
      {
        int loc=sDir.find("/",pos);
        if (loc==-1)
          loc=sDir.length();
        string sPath=sDir.substr(0,loc);

        Dirs::iterator it; 
        it=oDirs.find(sPath);

        if (it==oDirs.end())
        {
           oDirs.insert(pair<string,int>(sPath,2));
           iRes++;
        }
        pos=loc+1;
      }    
    }

    cout << "Case #" << i+1 << ": " << iRes << std::endl;
  }
	return 0;
}

