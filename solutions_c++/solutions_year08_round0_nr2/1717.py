#include <iostream>
#include <fstream>
#include <string>
#include <deque>
#include <map>
#include <list>
#include <vector>
#include <iterator>
#include <set>
#include <algorithm>
using namespace std;
typedef unsigned long long uint_64 ;
typedef long long int_64 ;
#define TRACE(X) std::cout<<X<<std::endl;
class Input;
class TrainTime;
class Input
{
    public:
    Input(std::deque<TrainTime> p_stationAtimes,std::deque<TrainTime> p_stationBtimes,uint_64 p_tat);
    void process();
    uint_64 numberofTrainsinA()
    {
        if (_noTrainsAtStationA>0)
        {
            return _noTrainsAtStationA;
        }
        return 0;
    }
    uint_64 numberofTrainsinB()
    {
        if (_noTrainsAtStationB>0)
        {
            return _noTrainsAtStationB;
        }
        return 0;
    }

 private:
    std::deque<TrainTime> stationAtimes;
    std::deque<TrainTime> stationBtimes;
    int_64 _noTrainsAtStationA;
    int_64 _noTrainsAtStationB;
    uint_64 _turnAroundTime;
};



class TrainTime
{    
    public:
    TrainTime(uint_64 p_timeForTrain,bool p_isArrived):timeForTrain(p_timeForTrain),isArrived(p_isArrived)
    {
    }

        uint_64 timeForTrain;
        bool isArrived;
};
class ReaderWriter
{
public:
    void readInputs(std::string filename)
    {
        ifstream myfile (filename.c_str(),ios::in);
        if(myfile.is_open())
        {
            string line;
                TRACE("INPUTS READ START");
            while (! myfile.eof() )
            {
                getline (myfile,line);
                cout << line << endl;
                _numberOfInputs=atol(line.c_str());
                //TRACE("number of inputs ="<<_numberOfInputs);
                for(uint_64 i=0 ; i<_numberOfInputs;i++)
                {
                    getline (myfile,line);
                    uint_64 turnAroundTime=0;
                    turnAroundTime=atol(line.c_str());
                    getline (myfile,line);
                    uint_64 trainsA2B=0,trainsB2A=0;
                    sscanf(line.c_str(),"%ld %ld",&trainsA2B,&trainsB2A);
                    //TRACE("Number of trains a2B="<<trainsA2B<< "   Number of trains B2A="<<trainsB2A);
                    std::deque<TrainTime> timesForStationA;
                    std::deque<TrainTime> timesForStationB;
                    for (uint_64 j=0;j<trainsA2B ;j++ )
                    {
                        getline (myfile,line);
                        uint_64 timeHr1=0,timeHr2=0,timeMin1=0,timeMin2=0;
                        sscanf(line.c_str(),"%ld:%ld %ld:%ld",&timeHr1,&timeMin1,&timeHr2,&timeMin2);
                        uint_64 totalTime1=timeHr1*60 + timeMin1;
                        uint_64 totalTime2=timeHr2*60 + timeMin2;
                        TrainTime x(totalTime1,false);
                        TrainTime y(totalTime2+turnAroundTime,true);
                        timesForStationA.push_back(x);
                        timesForStationB.push_back(y);
                        //TRACE("trains A2B  "<<j+1<<" departure time is ="<<totalTime1<< " and arrival time is "<<totalTime2);
                                  
                    }
                                      
                    for (uint_64 j=0;j<trainsB2A ;j++ )
                    {
                        getline (myfile,line);
                        uint_64 timeHr1=0,timeHr2=0,timeMin1=0,timeMin2=0;
                        sscanf(line.c_str(),"%ld:%ld %ld:%ld",&timeHr1,&timeMin1,&timeHr2,&timeMin2);
                        uint_64 totalTime1=timeHr1*60 + timeMin1;
                        uint_64 totalTime2=timeHr2*60 + timeMin2;
                        TrainTime x(totalTime1,false);
                        TrainTime y(totalTime2+turnAroundTime,true);
                        timesForStationA.push_back(y);
                        timesForStationB.push_back(x);
                        //TRACE("trains B2A  "<<j+1<<" departure time is ="<<totalTime1<< " and arrival time is "<<totalTime2);
                                           
                    }
                    Input inputData(timesForStationA,timesForStationB,turnAroundTime);
                    _inputs.push_back(inputData);
                }
            }
                myfile.close();
                //TRACE("INPUTS READ END");
        }
        else TRACE("unable to open the file "<<filename);
    }
    void processInputs()
    {
        for (std::deque<Input> ::iterator itr=_inputs.begin();itr!=_inputs.end();itr++)
        {
            itr->process();
        }
    }
    void writeOutput(std::string filename)
    {
        //Case #1: 2 2
//Case #2: 2 0
        ofstream myfile (filename.c_str());
        if(myfile.is_open())
        {
            uint_64 i=1;
            for (std::deque<Input> ::iterator itr=_inputs.begin();itr!=_inputs.end();itr++)
            {
                myfile<<"Case #"<<i<<": "<<itr->numberofTrainsinA()<<" "<<itr->numberofTrainsinB()<<"\n";
                i++;
            }
            myfile.close();
        }
        else TRACE("unable to open the file "<<filename);
    }
private:
    uint_64 _numberOfInputs;
    std::deque<Input> _inputs;



};


bool timeSortCriterion (const TrainTime& p1, const TrainTime& p2)
{
  if (p1.timeForTrain<p2.timeForTrain)
  {
      return true;
  }
  else if (p2.timeForTrain<p1.timeForTrain)
  {
      return false;
  }
  else
  {
      if (p1.isArrived>p2.isArrived)
      {
          return true;
      }
  }
  return false;
}


Input::Input(std::deque<TrainTime> p_stationAtimes,std::deque<TrainTime> p_stationBtimes,uint_64 p_tat)
    :stationAtimes(p_stationAtimes),stationBtimes(p_stationBtimes),_noTrainsAtStationA(0),_noTrainsAtStationB(0),_turnAroundTime(p_tat)
{
}
void Input::process()
{
    std::deque<TrainTime>::iterator itr;
//   for (itr=stationAtimes.begin() ; itr!=stationAtimes.end();++itr )
//   {
//       TRACE("time A station "<<itr->timeForTrain<<"    Is Arrived "<< itr->isArrived)
//   }
//   for ( itr=stationBtimes.begin() ; itr!=stationBtimes.end();++itr )
//   {
//       TRACE("time B station "<<itr->timeForTrain<<"    Is Arrived "<< itr->isArrived)
//   }

   //TRACE("Sorting ....."<<std::endl)   TRACE("Sorting ....."<<std::endl)   TRACE("Sorting ....."<<std::endl)   TRACE("Sorting ....."<<std::endl)
   sort(stationAtimes.begin(),stationAtimes.end(),timeSortCriterion); 
   sort(stationBtimes.begin(),stationBtimes.end(),timeSortCriterion); 
//   for ( itr=stationAtimes.begin() ; itr!=stationAtimes.end();++itr )
//   {
//       TRACE("time A station "<<itr->timeForTrain<<"    Is Arrived "<< itr->isArrived)
//   }
//   for ( itr=stationBtimes.begin() ; itr!=stationBtimes.end();++itr )
//   {
//       TRACE("time B station "<<itr->timeForTrain<<"    Is Arrived "<< itr->isArrived)
//   }

   int buffer=0;
   for (itr=stationAtimes.begin() ; itr!=stationAtimes.end();++itr )
   {

        if (itr->isArrived)
        {
            buffer++;
        }
        else
        {
            if(buffer==0)
            {
                _noTrainsAtStationA++;
            }
            else buffer--;
        }
   }
    buffer=0;
   for (itr=stationBtimes.begin() ; itr!=stationBtimes.end();++itr )
   {
        if (itr->isArrived)
        {
            buffer++;
        }
        else
        {            
            if(buffer==0)
            {
                _noTrainsAtStationB++;
            }else buffer--;
        }
   }
}






int main () {
  string line;
  //ifstream myfile ("inputfile",ios::in);
  ReaderWriter a;
  a.readInputs("B-large.in");
  a.processInputs();
  a.writeOutput("B-large.out");

  return 0;
}
