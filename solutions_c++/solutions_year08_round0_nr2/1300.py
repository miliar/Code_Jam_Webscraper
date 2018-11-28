#include <iostream>
#include <sstream>
#include <string>
#include <list>

using namespace std;

// Time is an object created from a "HH:MM" 24-hour time string
// Internally it stores the number of minutes past midnight
class Time
{
public:
  Time(const string& t) {
    istringstream str(t);
    int h, m;
    char c;
    str >> h >> c >> m; // Parse HH:MM
    minutes = h*60 + m;
  }

  // Return the time as number of minutes past midnight
  int getTime(void) const { return minutes; }

  // Comparison, used for sorting
  bool operator<(const Time& t) const {
    return minutes < t.minutes;
  }
  bool operator>(const Time& t) const {
    return minutes > t.minutes;
  }

  // Addition
  Time& operator+=(int min) {
    minutes += min;
  }

private:
  int minutes;
};

ostream& operator<<(ostream& os, const Time& t)
{
  os << t.getTime()/60 << ":" << t.getTime()%60;
}


// Event holds a Time and a Arrival/Departure flag
class Event
{
public:
  enum EventType { ARRIVAL, DEPARTURE };
  
  Event(const Time& t, EventType et) : time(t), type(et) {}

  const Time& getTime(void) const { return time; }
  EventType   getType(void) const { return type; }

  // Comparison operator, for sorting
  // Arrivals are sorted in front of departures
  bool operator<(const Event&t) const {
    if (time < t.time) return true;
    if (time > t.time) return false;
    return (type == ARRIVAL);
  }

private:
  Time      time; // Event time
  EventType type; // Event type: arrival or departure
};

// Write Event object to output stream
ostream& operator<<(ostream& os, const Event& e)
{
  os << e.getTime() << " ";
  if (e.getType() == Event::ARRIVAL) os << "A";
  else os << "D";

  return os;
}



int main(void)
{
  int N;
  cin >> N; // N = Number of test cases

  for (int test=1; test <= N; ++test) {
    int T, NA, NB;
    cin >> T;   // T  = Turnaround time in minutes
    cin >> NA;  // NA = Number of trips from A
    cin >> NB;  // NB = Number of trips from B

    list<Event> aEvents;  // List of departures and arrivals to A
    list<Event> bEvents;  // List of departures and arrivals to B

    // Read list of trips from A
    for (int i=1; i<=NA; ++i) {
      string s;
      cin >> s;    // Read departure time
      Time td(s);
      cin >> s;    // Read arrival time
      Time ta(s);
      ta += T;     // Add turnaround time to the arrival time
      
      aEvents.push_back(Event(td, Event::DEPARTURE));
      bEvents.push_back(Event(ta, Event::ARRIVAL));
    }

    // Read list of trips from B
    for (int i=1; i<=NB; ++i) {
      string s;
      cin >> s;    // Read departure time
      Time td(s);
      cin >> s;    // Read arrival time
      Time ta(s);
      ta += T;     // Add turnaround time to the arrival time
      
      bEvents.push_back(Event(td, Event::DEPARTURE));
      aEvents.push_back(Event(ta, Event::ARRIVAL));
    }

    // Sort the event lists
    aEvents.sort();
    bEvents.sort();

    // Parse the event lists
    int aStock = 0, bStock = 0;    // Current number of ready trains at A/B
    int aStarts = 0, bStarts = 0;  // # of trains that have to start from A/B
    for (list<Event>::iterator it=aEvents.begin(); it != aEvents.end(); ++it) {
      if (it->getType() == Event::ARRIVAL) ++aStock;
      else --aStock;
      if (aStock < 0) {
	++aStarts;
	++aStock;
      }
    }

    for (list<Event>::iterator it=bEvents.begin(); it != bEvents.end(); ++it) {
      if (it->getType() == Event::ARRIVAL) ++bStock;
      else --bStock;
      if (bStock < 0) {
	++bStarts;
	++bStock;
      }
    }

    // Write the result
    cout << "Case #" << test << ": " << aStarts << " " << bStarts << endl;
  }
  
  return 0;
}
