#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>

#include <pthread.h>

//#define DEBUG_TRACE(x) x
#define DEBUG_TRACE(x)


#define GETVALUE_1(VAR) std::cin >> VAR; DEBUG_TRACE( std::cout << #VAR "=" << VAR <<std::endl );

#define GETVALUE(TYPE, VAR) TYPE VAR; GETVALUE_1(VAR)

class Problem
{
public:
  pthread_t threadId;
  //std::ostringstream outPut;
  std::string outPut;

  virtual void readData()=0;
  virtual void execute()=0;
};

class TrainTable :public Problem
{
public:
  typedef std::map <int , int > TimeTable;

private:
  int _convertTime(std::string& time)
  {
    int dTime=0;
    dTime = (time[0]-'0')*10+(time[1]-'0');
    dTime *=60;
    dTime += ( (time[3]-'0')*10+(time[4]-'0') );
    return dTime;
  }

  void _getTimings(int departures, TimeTable &firstS, TimeTable& secondS)
  {
    std::string time;
    int dTime;
    for(int iii=0; iii<departures; iii++)
    {
      GETVALUE_1(time);
      dTime=_convertTime(time);
      firstS[dTime]=firstS[dTime]-1;
      DEBUG_TRACE( std::cout << firstS[dTime] );

      GETVALUE_1(time);
      dTime=_convertTime(time)+turnAroundTime;
      secondS[dTime]=secondS[dTime]+1;

      DEBUG_TRACE(std::cout << " " << secondS[dTime] << std::endl);
    }
  }

  int _getMinCount(TimeTable &station)
  {
    int minCount=0;
    int cumCount=0;
    TimeTable::iterator present = station.begin();
    if(present == station.end() )
    {
      return minCount;
    }
    cumCount = minCount = present->second;

    TimeTable::iterator prev = present;
    present++;

    while(present!=station.end())
    {
      cumCount+=present->second;
      if(cumCount < minCount)
      {
        minCount=cumCount;
      }
      present++;
      prev++;
    }

    return minCount;
  }

public:

  TimeTable stationA;
  TimeTable stationB;

  int turnAroundTime;
  int countA;
  int countB;

  void readData()
  {
    GETVALUE_1(turnAroundTime);
  
    GETVALUE(int, startA);
  
    GETVALUE(int, startB);
  
    _getTimings(startA, stationA, stationB);
    _getTimings(startB, stationB, stationA);
  }

  void execute()
  {
    countA=_getMinCount(stationA);
    countB=_getMinCount(stationB);

    std::ostringstream solu;
    solu << (countA>0?0:-countA)<<" ";
    solu << (countB>0?0:-countB)<<" ";
    outPut += solu.str();
    DEBUG_TRACE ( std::cout<< outPut << std::endl );
  }
};

void* execute(void *prob)
{
  Problem *thProb = static_cast<Problem*>(prob);
  thProb->execute();
  pthread_exit(NULL);
}

int main()
{
  int rc;
  int numProb;

  std::cin>> numProb;

  DEBUG_TRACE( std::cout << "numProb=" << numProb <<std::endl );
  
  std::vector<TrainTable> probSet(numProb);

  for(int iii=0; iii<numProb; iii++)
  {
    std::ostringstream outPut;
    outPut << "Case #" << iii+1 << ": ";
    probSet[iii].outPut = outPut.str();
    probSet[iii].readData();
    probSet[iii].execute();
/*
    rc=pthread_create(&probSet[iii].threadId, NULL, execute, (void*) &probSet[iii]) ;
    if(rc )
    {
      std::cerr<<"ERROR: return code from pthread_create("<<iii<<") is " << rc << std::endl;
      exit(-1);
    }
*/
  }

/*
  void* status;
  for(int iii=0; iii<numProb; iii++)
  {
    rc = pthread_join(probSet[iii].threadId, &status);
    if(rc )
    {
      std::cerr<<"ERROR: return code from pthread_join("<<iii<<") is " << rc << std::endl;
      exit(-1);
    }
  }
*/

  for(int iii=0; iii<numProb; iii++)
  {
    std::cout << probSet[iii].outPut << std::endl;
  }

  return 0;
}
