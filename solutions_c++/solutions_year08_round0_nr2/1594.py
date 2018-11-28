#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <queue>

typedef unsigned long uint32;

uint32 readTime(std::istream &is) {
  uint32 hour = 0, min = 0;
  char dummy;
  is >> hour >> dummy >> min;
  return ((hour * 60) + min);
}

class Trip {
  private :
    uint32 departure;
    uint32 arrival;

  public :
    bool operator<(const Trip &trip) const {
      return (this->departure < trip.departure);
    }
    
    friend std::istream &operator>>(std::istream &is, Trip &t);
    friend class TrainSchedule;
};

std::istream &operator>>(std::istream &is, Trip &t) {
  std::string line;
  if (!getline(is, line)) {
    exit(1);
  }
  {
    std::stringstream ss(line);
    t.departure = readTime(ss);
    t.arrival = readTime(ss);
    if (!ss) exit(1);
  }
  return is;
}

void readTimeTable(std::istream &is, std::vector<Trip> &tt, uint32 n) {
  std::string line;
  for (int i = 0; i < n; ++i) {
    if (!getline(is, line)) {
      exit(1);
    }
    Trip trip;
    {
      std::stringstream ss(line);
      ss >> trip;
      if (!ss) exit(1);
    }
    tt.push_back(trip);
  }
}

class TrainEvent {
  private :
    typedef enum TEType { TET_arrival = 0, TET_departure = 1 } TEType;
    TEType type;
    uint32 when;
    Trip *trip;

  public :
    TrainEvent(TEType typ, uint32 w, Trip *tr = 0) : type(typ), when(w), trip(tr) { }

    bool operator<(const TrainEvent &event) const {
      return ((this->when > event.when) || ((this->when == event.when) && (this->type > event.type)));
    }

    friend class TrainSchedule;
};

class TrainSchedule {
  private :
    typedef std::vector<Trip> Trips;

    uint32 t;
    Trips ttA;
    Trips ttB;
    
  public :
    uint32 calcAmount(std::priority_queue<TrainEvent> &q);
    void calcAmounts(uint32 &a, uint32 &b);
    friend std::istream &operator>>(std::istream &is, TrainSchedule &ts);
};

std::istream &operator>>(std::istream &is, TrainSchedule &ts) {
  std::string line;
  if (!getline(is, line)) {
    exit(1);
  }
  {
    std::stringstream ss(line);
    ss >> ts.t;
    if (!ss) exit(1);
  }
  uint32 na = 0, nb = 0;
  if (!getline(is, line)) {
    exit(1);
  }
  {
    std::stringstream ss(line);
    ss >> na >> nb;
    if (!ss) exit(1);
  }
  readTimeTable(is, ts.ttA, na);
  readTimeTable(is, ts.ttB, nb);
  return is;
}

uint32 TrainSchedule::calcAmount(std::priority_queue<TrainEvent> &q) {
  uint32 amount = 0;
  uint32 curAmount = 0;
  while (!(q.empty())) {
    const TrainEvent &event = q.top();
    switch (event.type) {
      case TrainEvent::TET_departure :
        if (curAmount) {
          --curAmount;
        }
        else {
          ++amount;
        }
        break;
      case TrainEvent::TET_arrival :
        ++curAmount;
        break;
    }
    q.pop();
  }
  return amount;
}

void TrainSchedule::calcAmounts(uint32 &a, uint32 &b) {
  a = 0;
  b = 0;

  std::priority_queue<TrainEvent> qA;
  std::priority_queue<TrainEvent> qB;

  Trips::iterator trip_it;
  for (trip_it = ttA.begin(); trip_it != ttA.end(); ++trip_it) {
    Trip &trip = *trip_it;
    qA.push(TrainEvent(TrainEvent::TET_departure, trip.departure, &trip));
    qB.push(TrainEvent(TrainEvent::TET_arrival, trip.arrival + this->t, &trip));
  }
  for (trip_it = ttB.begin(); trip_it != ttB.end(); ++trip_it) {
    Trip &trip = *trip_it;
    qB.push(TrainEvent(TrainEvent::TET_departure, trip.departure, &trip));
    qA.push(TrainEvent(TrainEvent::TET_arrival, trip.arrival + this->t, &trip));
  }
  
  a = calcAmount(qA);
  b = calcAmount(qB);
}

int main(int argc, char *argv[]) {
  if (argc < 3) exit(1);

  std::ifstream infile(argv[1]);
  std::ofstream outfile(argv[2]);
  
  std::string line;
  if (!getline(infile, line)) {
    exit(1);
  }
  uint32 n = 0;
  {
    std::stringstream ss(line);
    ss >> n;
    if (!ss) exit(1);
  }
  for (int i = 0; i < n; ++i) {
    TrainSchedule ts;
    infile >> ts;
    uint32 a = 0, b = 0;
    ts.calcAmounts(a, b);
    outfile << "Case #" << (i + 1) << ": " << a << " "<< b << std::endl;
  }
  
  infile.close();
  outfile.close();

  return 0;
}
