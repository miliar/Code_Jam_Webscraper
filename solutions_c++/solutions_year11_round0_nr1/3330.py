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


struct pushStruct
{
  int iOrder;
  int iButton;
};

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
    char cRobType;
    int nPushes;
    vector<pushStruct> vPushOrange;
    vector<pushStruct> vPushBlue;

    cin >> nPushes;

    int iOrangeCnt=0;
    int iBlueCnt=0;

    for (int j=0;j<nPushes;j++)
    {
      char cRob;
      int iButton;
      cin >> cRob;
      cin >> iButton;
      
      if (cRob=='O')
      {
        vPushOrange.resize(iOrangeCnt+1);
        vPushOrange[iOrangeCnt].iButton=iButton;
        vPushOrange[iOrangeCnt].iOrder=j;
        iOrangeCnt++;
      }

      if (cRob=='B')
      {
        vPushBlue.resize(iBlueCnt+1);
        vPushBlue[iBlueCnt].iButton=iButton;
        vPushBlue[iBlueCnt].iOrder=j;
        iBlueCnt++;
      }

    }

    int iOrangeLoc=1;
    int iBlueLoc=1;
    int iTotalTime=0;

    int iBlueIdx=0;
    int iOrangeIdx=0;

    while (true)
    {
      int iNextBlue=-1; 
      int iNextOrange=-1; 
      
      if (iBlueIdx<iBlueCnt)
      {
        iNextBlue=vPushBlue[iBlueIdx].iButton;
      }

      if (iOrangeIdx<iOrangeCnt)
      {
        iNextOrange=vPushOrange[iOrangeIdx].iButton;
      }

      if (iNextBlue==-1 && iNextOrange==-1)
        break;

      int iOrangeCur=iOrangeIdx;
      int iBlueCur=iBlueIdx;

      if (iNextOrange!=-1)
      {
        if (iOrangeLoc<iNextOrange)
        {
          iOrangeLoc++;
        }
        else
        if (iOrangeLoc>iNextOrange)
        {
          iOrangeLoc--;
        }
        else
        {
          if (iNextBlue==-1)
          {
            iOrangeIdx++;
          }
          else if (vPushOrange[iOrangeCur].iOrder<vPushBlue[iBlueCur].iOrder)
          {
            iOrangeIdx++;
          }
        }
      }

      if (iNextBlue!=-1)
      {
        if (iBlueLoc<iNextBlue)
        {
          iBlueLoc++;
        }
        else
        if (iBlueLoc>iNextBlue)
        {
          iBlueLoc--;
        }
        else
        {
          if (iNextOrange==-1)
          {
            iBlueIdx++;
          }
          else if (vPushOrange[iOrangeCur].iOrder>vPushBlue[iBlueCur].iOrder)
          {
            iBlueIdx++;
          }
        }
      }

      iTotalTime++;
    }
    /*while (iBlueIdx<iBlueCnt && iOrangeIdx<iOrangeCnt)
    {
      int iNextBlue=vPushBlue[iBlueIdx].iButton;
      int iNextOrange=vPushOrange[iOrangeIdx].iButton;

      int iDiffBlue=abs(iBlueLoc-iNextBlue);
      int iDiffOrange=abs(iOrangeLoc-iNextOrange);

      if ((iDiffBlue>iDiffOrange && vPushBlue[iBlueIdx].iOrder>vPushOrange[iOrangeIdx].iOrder) || vPushBlue[iBlueIdx].iOrder<vPushOrange[iOrangeIdx].iOrder)
      {
        int iFreeTime=iDiffBlue+1;
        iTotalTime+=iFreeTime;
        iBlueLoc=iNextBlue;

        for (int i=iOrangeIdx;i<iOrangeCnt && iFreeTime>0  ;i++)
        {
          int iNextOrange=vPushOrange[i].iButton;
          int iDiffOrange=abs(iOrangeLoc-iNextOrange);
          if (iFreeTime>(iDiffOrange+1) && vPushOrange[iOrangeIdx].iOrder<vPushBlue[iBlueIdx].iOrder)
          {
            iOrangeIdx++;
            iFreeTime-=(iDiffOrange+1);
            iOrangeLoc=iNextOrange;
          }
          else
          {
            if (iOrangeLoc<iNextOrange)
            {
              iOrangeLoc+=min(iFreeTime,iDiffOrange);
            }
            else
            {
              iOrangeLoc-=min(iFreeTime,iDiffOrange);
            }
            iFreeTime=0;
          }
        }
        iBlueIdx++;
      }
      else
      if ( (iDiffOrange>iDiffBlue && vPushOrange[iOrangeIdx].iOrder>vPushBlue[iBlueIdx].iOrder )  || vPushOrange[iOrangeIdx].iOrder<vPushBlue[iBlueIdx].iOrder)
      {
        int iFreeTime=iDiffOrange+1;
        iTotalTime+=iFreeTime;
        iOrangeLoc=iNextOrange;
        for (int i=iBlueIdx;i<iBlueCnt && iFreeTime>0  ;i++)
        {
          int iNextBlue=vPushBlue[i].iButton;
          int iDiffBlue=abs(iBlueLoc-iNextBlue);
          if (iFreeTime>(iDiffBlue+1) && vPushBlue[iBlueIdx].iOrder<vPushOrange[iOrangeIdx].iOrder)
          {
            iBlueIdx++;
            iFreeTime-=(iDiffBlue+1);
            iBlueLoc=iNextBlue;
          }
          else
          {
            if (iBlueLoc<iNextBlue)
            {
              iBlueLoc+=min(iFreeTime,iDiffBlue);
            }
            else
            {
              iBlueLoc-=min(iFreeTime,iDiffBlue);
            }
            iFreeTime=0;
          }
        }
        iOrangeIdx++;
        
      }
    }

    while (iBlueIdx<iBlueCnt)
    {
      int iNextBlue=vPushBlue[iBlueIdx].iButton;
      int iDiffBlue=abs(iBlueLoc-iNextBlue);
      iBlueLoc=iNextBlue;
      iTotalTime+=iDiffBlue+1;
      iBlueIdx++;
    }

    while (iOrangeIdx<iOrangeCnt)
    {
      int iNextOrange=vPushOrange[iOrangeIdx].iButton;
      int iDiffOrange=abs(iOrangeLoc-iNextOrange);
      iOrangeLoc=iNextOrange;
      iTotalTime+=iDiffOrange+1;
      iOrangeIdx++;
    }*/

    cout << "Case #" << i+1 << ": " << iTotalTime << std::endl;
  }
	return 0;
}

