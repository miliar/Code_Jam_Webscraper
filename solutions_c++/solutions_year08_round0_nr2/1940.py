#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <strstream> 

using namespace std;

int TrainsNeedforStation(string departureTime[], int departureTrips, string arriveTime[], int arriveTrips, int turnoverTime);
void TransformTime(string Time[], int* TransformedTime, int TimeNums);
void TurnOver(int* TransformedTime, int TimeNums, int turnovertime);
void SortTime(int* TransformedTime, int TimeNums);

int main(int argc, char *argv[])
{
  ifstream filein("B-large.in.txt");
  ofstream oFile( "b.out" );
  string casesin, TurnOverTimes, TripsA, TripsB;
  int cases, TurnoverTime, TripsANum, TripsBNum;
  getline(filein, casesin);
  cases = atoi(casesin.c_str());
//  cout << cases << endl;
  for (int i = 0; i < cases; i++)
  {
    //string departureTime, arriveTime;
    //getline(filein, TurnOverTimes);
    filein >> TurnOverTimes;
    TurnoverTime = atoi(TurnOverTimes.c_str());
    cout << TurnoverTime << endl;
    filein >> TripsA;
    filein >> TripsB;
    TripsANum = atoi(TripsA.c_str());
    TripsBNum = atoi(TripsB.c_str());
    string* departureTimeA = new string[TripsANum];
    string* arriveTimeA = new string[TripsANum];
    cout << TripsANum << endl;
    cout << TripsBNum << endl;
    for(int i = 0; i<  TripsANum; i++)
    {
        filein >> departureTimeA[i];
        filein >> arriveTimeA[i];
        cout << departureTimeA[i] << " ";
        cout << arriveTimeA[i] << endl;
//        cout << (departureTimeA[i]> arriveTimeA[i])<< endl;
    }
    string* departureTimeB = new string[TripsBNum];
    string* arriveTimeB = new string[TripsBNum];
    for(int i = 0; i<  TripsBNum; i++)
    {
        filein >> departureTimeB[i];
        filein >> arriveTimeB[i];
        cout << departureTimeB[i] << " ";
        cout << arriveTimeB[i] << endl;
    }
    int TrainsStationA = TrainsNeedforStation(departureTimeA, TripsANum, arriveTimeB, TripsBNum, TurnoverTime);
    int TrainsStationB = TrainsNeedforStation(departureTimeB, TripsBNum, arriveTimeA, TripsANum, TurnoverTime);
    cout << "Case #"<< i + 1 << ": "<< TrainsStationA << " ";
    cout << TrainsStationB << endl;
    oFile << "Case #"<< i + 1 << ": "<< TrainsStationA << " ";
    oFile << TrainsStationB << endl;
//    oFile << "Case #"<< i + 1 << ": "<<times << endl;
  }
  filein.close();
  system("PAUSE");	
  return 0;
}

int TrainsNeedforStation(string departureTime[], int departureTrips, string arriveTime[], int arriveTrips, int turnoverTime)
{
    int trains = 0;
    int departureTimeTransformed[departureTrips];
    int arriveTimeTransformed[arriveTrips];
    for(int i = 0; i< departureTrips;i++)
        departureTimeTransformed[i] = 0;
    for(int i = 0; i< arriveTrips;i++)
        arriveTimeTransformed[i] = 0;
    TransformTime(departureTime, departureTimeTransformed, departureTrips);
    TransformTime(arriveTime, arriveTimeTransformed, arriveTrips);
    TurnOver(arriveTimeTransformed, arriveTrips, turnoverTime);
    
    SortTime(departureTimeTransformed, departureTrips);
    SortTime(arriveTimeTransformed, arriveTrips);
    
    int departureTripsDone = 0, arriveTripsDone = 0;
    while ((departureTripsDone < departureTrips))
    {
        if(departureTimeTransformed[departureTripsDone] < arriveTimeTransformed[arriveTripsDone]
        ||arriveTripsDone == arriveTrips)
        {
            trains++;
            
        }   
        else 
        {           
            arriveTripsDone++;
        }    
        departureTripsDone++; 
    }
    if(arriveTrips == 0)
       trains = departureTrips;
            if(trains < 0)
                trains = 0;       
    return trains;
}

void TransformTime(string Time[], int* TransformedTime, int TimeNums)
{
    for (int i = 0; i< TimeNums;i++)
    {
       TransformedTime[i] = 0;
       const char* t = Time[i].c_str();
       TransformedTime[i]+=(t[0]-'0')*600;
       TransformedTime[i]+=(t[1]-'0')*60;
       TransformedTime[i]+=(t[3]-'0')*10;
       TransformedTime[i]+=(t[4]-'0');
//       cout<< Time[i]<< " "<<TransformedTime[i]<< endl;
    }
}
void TurnOver(int* TransformedTime, int TimeNums, int turnovertime)
{
    for (int i = 0; i< TimeNums;i++)
    {
       TransformedTime[i]+=turnovertime;
//       cout<< Time[i]<< " "<<TransformedTime[i]<< endl;
    }
}

void SortTime(int* TransformedTime, int TimeNums)
{
    for(int i = 0; i < TimeNums; i++)
        for (int j = i+1; j<TimeNums; j++)
           if(TransformedTime[j]< TransformedTime[i])
           {
              int t = TransformedTime[j];
              TransformedTime[j] = TransformedTime[i];
              TransformedTime[i] = t;
           }
}

