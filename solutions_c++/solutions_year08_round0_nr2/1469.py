//
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

#include <list>
using namespace std;

class TrainInfo
{
public:
	// Default Constructor
  TrainInfo() {};
  ~TrainInfo() {};

  int m_intOrigin;
  int m_intLocation;
  int m_intTimeAvailable;
};
typedef std::list< TrainInfo > t_listTrain;

class ScheduleInfo
{
public:
  // Default Constructor
  ScheduleInfo() {};
  ~ScheduleInfo() {};

  int m_intOrigin;
  int m_intDepartTime;
  int m_intArriveTime;
};
typedef std::list< ScheduleInfo > t_listSchedule;

bool sortSchedule(const ScheduleInfo& p1, const ScheduleInfo & p2)
{	return( const_cast< ScheduleInfo& >(p1).m_intDepartTime < const_cast< ScheduleInfo& >(p2).m_intDepartTime);
}

class CaseInfo
{
public:
  // Default Constructor
  CaseInfo() {};
  ~CaseInfo() {};

  int m_intCaseNumber;
  int m_intTurnAroundTime;
  t_listSchedule m_listSchedule;
  t_listTrain    m_listTrain;
};
typedef std::list< CaseInfo > t_listCaseInfo;


int main( int argc, char** argv )
{
  string fnIn;
	// Set Input File Name
	fnIn = argv[1];
  string line;
  ifstream myfile ( fnIn.c_str() );
  if ( ! myfile.is_open())
  {
    cout << "Unable to open file";
    return( 1);
  }

  int intNumCases;
  // Get NumCases
  getline (myfile,line);
  intNumCases = atoi( line.c_str());
//  cout << "NumCases: " << intNumCases << endl;

	int        intSplitPos;
	int        intColonPos;
	int        intNA, intNB;
	int        intOrigin;
	int        intDepartTime;
	int        intArriveTime;
	string     strTemp;
	string     strMin, strSec;
  CaseInfo       l_CaseInfo;
  ScheduleInfo   l_ScheduleInfo;
  t_listCaseInfo listCaseInfo;
  for ( int i=0; i<intNumCases; ++i)
  {
    l_CaseInfo.m_intCaseNumber = i+1;
    // Get TurnAround Time
    getline (myfile,line);
    l_CaseInfo.m_intTurnAroundTime = atoi( line.c_str());
    // Get NA, NB
    getline (myfile,line);
    intSplitPos = line.rfind(" ");
    strTemp = line.substr( 0, intSplitPos);
    intNA = atoi( strTemp.c_str());
    strTemp = line.substr( intSplitPos+1);
    intNB = atoi( strTemp.c_str());
//    cout << "Case: " << l_CaseInfo.m_intCaseNumber
//         << "\nTurnAround Time: " << l_CaseInfo.m_intTurnAroundTime
//         << "\nNumA: " << intNA << " NumB: " << intNB
//         << endl;

    intOrigin = -1;
    for ( int j=0; j<intNA; ++j)
    {
      getline (myfile,line);
      cout << "Time: " << line << endl;
      intSplitPos = line.rfind(" ");
      // Get Depart Time
      strTemp = line.substr( 0, intSplitPos);
      intColonPos = strTemp.rfind(":");
      strMin = strTemp.substr( 0, intColonPos);
      strSec = strTemp.substr( intColonPos+1);
      intDepartTime = atoi( strMin.c_str())*60 + atoi( strSec.c_str());
      // Get Arrive Time
      strTemp = line.substr( intSplitPos+1);
      intColonPos = strTemp.rfind(":");
      strMin = strTemp.substr( 0, intColonPos);
      strSec = strTemp.substr( intColonPos+1);
      intArriveTime = atoi( strMin.c_str())*60 + atoi( strSec.c_str()) + l_CaseInfo.m_intTurnAroundTime;

      l_ScheduleInfo.m_intOrigin     = intOrigin;
      l_ScheduleInfo.m_intDepartTime = intDepartTime;
      l_ScheduleInfo.m_intArriveTime = intArriveTime;
      l_CaseInfo.m_listSchedule.push_back( l_ScheduleInfo);
//      cout << "Depart: " << intDepartTime << " Arrive: " << intArriveTime << endl;
    }

    intOrigin = 1;
    for ( int j=0; j<intNB; ++j)
    {
      getline (myfile,line);
      cout << "Time: " << line << endl;
      intSplitPos = line.rfind(" ");
      // Get Depart Time
      strTemp = line.substr( 0, intSplitPos);
      intColonPos = strTemp.rfind(":");
      strMin = strTemp.substr( 0, intColonPos);
      strSec = strTemp.substr( intColonPos+1);
      intDepartTime = atoi( strMin.c_str())*60 + atoi( strSec.c_str());
      // Get Arrive Time
      strTemp = line.substr( intSplitPos+1);
      intColonPos = strTemp.rfind(":");
      strMin = strTemp.substr( 0, intColonPos);
      strSec = strTemp.substr( intColonPos+1);
      intArriveTime = atoi( strMin.c_str())*60 + atoi( strSec.c_str()) + l_CaseInfo.m_intTurnAroundTime;

      l_ScheduleInfo.m_intOrigin     = intOrigin;
      l_ScheduleInfo.m_intDepartTime = intDepartTime;
      l_ScheduleInfo.m_intArriveTime = intArriveTime;
      l_CaseInfo.m_listSchedule.push_back( l_ScheduleInfo);
//      cout << "Depart: " << intDepartTime << " Arrive: " << intArriveTime << endl;
    }
    // Sort the Schedule
    l_CaseInfo.m_listSchedule.sort( sortSchedule);
    listCaseInfo.push_back( l_CaseInfo);
    l_CaseInfo.m_listSchedule.clear();
  }
  myfile.close();

  t_listCaseInfo::iterator itCase;
  t_listSchedule::iterator itSchedule;
  t_listTrain::iterator    itTrain;
  TrainInfo l_TrainInfo;
  for (
    itCase  = listCaseInfo.begin();
    itCase != listCaseInfo.end();
    ++itCase)
  {
    for (
      itSchedule  = (*itCase).m_listSchedule.begin();
      itSchedule != (*itCase).m_listSchedule.end();
      ++itSchedule)
    {
      for (
        itTrain  = (*itCase).m_listTrain.begin();
        itTrain != (*itCase).m_listTrain.end();
        ++itTrain)
      {
        if ( ((*itTrain).m_intLocation == (*itSchedule).m_intOrigin) &&
             ((*itTrain).m_intTimeAvailable <= (*itSchedule).m_intDepartTime))
        {
          (*itTrain).m_intLocation = -1*(*itSchedule).m_intOrigin;
          (*itTrain).m_intTimeAvailable = (*itSchedule).m_intArriveTime;
          break;
        }
      }
      if ( itTrain == (*itCase).m_listTrain.end() )
      {
        l_TrainInfo.m_intOrigin = (*itSchedule).m_intOrigin;
        l_TrainInfo.m_intLocation = -1*(*itSchedule).m_intOrigin;
        l_TrainInfo.m_intTimeAvailable = (*itSchedule).m_intArriveTime;
        (*itCase).m_listTrain.push_back( l_TrainInfo);
      }
    }
  }

  cout << "\n\nFINAL OUTPUT\n\n" << endl;
  for (
    itCase  = listCaseInfo.begin();
    itCase != listCaseInfo.end();
    ++itCase)
  {
    for (
      itTrain  = (*itCase).m_listTrain.begin(), intNA=0, intNB=0;
      itTrain != (*itCase).m_listTrain.end();
      ++itTrain)
    {
      if ( (*itTrain).m_intOrigin < 0) intNA++;
      else intNB++;
    }
    cout << "Case #" << (*itCase).m_intCaseNumber
         << ": " << intNA
         << " " << intNB << endl;
  }

  return( 0);
}


