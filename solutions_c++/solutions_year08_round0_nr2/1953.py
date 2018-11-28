#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>


using namespace std;

struct Trip
{
  int depTime;
  int arrTime;
  bool AtoB;
  bool done;
  bool operator()(const Trip& s1, const Trip& s2) const
  {
    return s1.depTime<s2.depTime;
  }
};

bool comparex(Trip& x, Trip& y)
{
  return x.depTime < y.depTime;
}

typedef vector<Trip> TripVec;


int calculateTrains(int turnTime,TripVec &Trips, int &trainsA,int &trainsB)
{
  //int trainsA=0,trainsB=0;
  vector<int> StationA;
  vector<int> StationB;
  for (unsigned int i=0;i<Trips.size();i++)
  {
    Trip &cur=Trips[i];
    if (cur.AtoB)
    {
      bool gotTrain=false;
      for (unsigned int j=0;j<StationA.size();j++)
      {
        if (StationA[j]!=-1 && StationA[j]<=cur.depTime)
        {
          // train waiting at station A
          gotTrain=true;
          StationA[j]=-1; // reserve train
          break;
        }
      }
      if (!gotTrain)
      {
        trainsA++;
      }

      gotTrain=false;
      for (unsigned int j=0;j<StationB.size();j++)
      {
        if (StationB[j]==-1)
        {
          StationB[j]=cur.arrTime+turnTime;
          gotTrain=true;
          break;
        }
      }
      if (!gotTrain)
      {
        StationB.push_back(cur.arrTime+turnTime);
      }
    }
    else
    {
      bool gotTrain=false;
      for (unsigned int j=0;j<StationB.size();j++)
      {
        if (StationB[j]!=-1 && StationB[j]<=cur.depTime)
        {
          // train waiting at station B
          gotTrain=true;
          StationB[j]=-1; // reserve train
          break;
        }
      }
      if (!gotTrain)
      {
        trainsB++;
      }

      gotTrain=false;
      for (unsigned int j=0;j<StationA.size();j++)
      {
        if (StationA[j]==-1)
        {
          StationA[j]=cur.arrTime+turnTime;
          gotTrain=true;
          break;
        }
      }
      if (!gotTrain)
      {
        StationA.push_back(cur.arrTime+turnTime);
      }
    }
  }
  return trainsB+trainsA;
}

void main(int argc, char * argv[])
{
  int caseCount=0;
  TripVec Trips;
  scanf("%d",&caseCount);

  for (int caseId=1;caseId<=caseCount;caseId++)
  {
    int turnaroundTime=0;
    int ABTripCnt=0;
    int BATripCnt=0;

    Trips.clear();
    //BAtrips.clear();

    scanf("%d",&turnaroundTime);
    scanf("%d",&ABTripCnt);
    scanf("%d",&BATripCnt);
    Trips.resize(ABTripCnt+BATripCnt);
    //BAtrips.resize(BATripCnt);
    int depH,depM,arrH,arrM;

    for (int tripId=0;tripId<ABTripCnt;tripId++)
    {
      scanf("%d:%d %d:%d",&depH,&depM,&arrH,&arrM);
      Trips[tripId].depTime=depH*60+depM;
      Trips[tripId].arrTime=arrH*60+arrM;
      Trips[tripId].AtoB=true;
      Trips[tripId].done=false;
    }
    
    //sort(ABtrips.begin(), ABtrips.end(),comparex);

    for (int tripId=ABTripCnt;tripId<(BATripCnt+ABTripCnt);tripId++)
    {
      scanf("%d:%d %d:%d",&depH,&depM,&arrH,&arrM);
      Trips[tripId].depTime=depH*60+depM;
      Trips[tripId].arrTime=arrH*60+arrM;
      Trips[tripId].AtoB=false;
      Trips[tripId].done=false;
    }
    sort(Trips.begin(), Trips.end(),comparex);

    int trainsA=0, trainsB=0;
    int result=calculateTrains(turnaroundTime,Trips,trainsA,trainsB);
    printf("Case #%d: %d %d\n",caseId,trainsA,trainsB);
  }
  //fclose(f);
}
