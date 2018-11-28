#include <algorithm>
#include <iostream>
#include <vector>

enum EventType
{
  Arrival,
  Departure
};

enum StationEnm
{
  StationA,
  StationB
};

class Event
{
  EventType type_;
  int time_;
  StationEnm station_;
public:
  Event(int time, EventType type, StationEnm station)
    :time_(time),type_(type),station_(station)
  {
  }

  StationEnm Station()const{return station_;}
  EventType Type()const{return type_;}
  int Time()const{return time_;}
};

struct sort_events
{
  bool operator()(const Event& left, const Event& right) 
  {
    if( left.Time() == right.Time() )
    {
      return left.Type() < right.Type();
    }
    else
    {
      return left.Time() < right.Time();
    }
  }
};

void TrainTimetables(int caseNumber)
{
  int turnAroundTime; std::cin >> turnAroundTime;
  int numberOfTripsFromAtoB; std::cin >> numberOfTripsFromAtoB;
  int numberOfTripsFromBtoA; std::cin >> numberOfTripsFromBtoA;

  std::vector<Event> events;
  for(int i=0; i<numberOfTripsFromAtoB; ++i)
  {
    char colon;
    int hours;
    int minutes;

    std::cin >> hours >> colon >> minutes;
    events.push_back(Event(minutes+60*hours,Departure,StationA));

    std::cin >> hours >> colon >> minutes;
    events.push_back(Event(turnAroundTime+minutes+60*hours,Arrival,StationB));
  }

  for(int i=0; i<numberOfTripsFromBtoA; ++i)
  {
    char colon;
    int hours;
    int minutes;

    std::cin >> hours >> colon >> minutes;
    events.push_back(Event(minutes+60*hours,Departure,StationB));

    std::cin >> hours >> colon >> minutes;
    events.push_back(Event(turnAroundTime+minutes+60*hours,Arrival,StationA));
  }

  std::sort(events.begin(),events.end(),sort_events());

  int totalTrainsAtA = 0;
  int totalTrainsAtB = 0;
  int trainsAtA = 0;
  int trainsAtB = 0;

  for(int i=0; i < events.size(); ++i)
  {
    if( events[i].Type() == Departure )
    {
      if( events[i].Station() == StationA )
      {
        if( trainsAtA == 0 )
        {
          ++trainsAtA;
          ++totalTrainsAtA;
        }
        --trainsAtA;
      }
      else
      {
        if( trainsAtB == 0 )
        {
          ++trainsAtB;
          ++totalTrainsAtB;
        }
        --trainsAtB;
      }
    }

    if( events[i].Type() == Arrival )
    {
      if( events[i].Station() == StationA )
      {
        ++trainsAtA;
      }
      else
      {
        ++trainsAtB;
      }
    }
  }

  std::cout << "Case #" << caseNumber << ": " << totalTrainsAtA << " " << totalTrainsAtB << std::endl;
}

int main()
{
  int numberOfTestCases; std::cin >> numberOfTestCases;
  for(int testCase = 1; testCase <= numberOfTestCases; ++testCase)
  {
    TrainTimetables(testCase);
  }
}