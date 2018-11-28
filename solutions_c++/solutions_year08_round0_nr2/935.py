#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using std::string;
using std::cin;
using std::cout;
using std::cerr;
using std::endl;
using std::vector;

#define FOR(i,s,e) for (int i = (s); i < (e); i++)

static const int MIN_TIME = 0;
static const int MAX_TIME = 24*60;

struct trip {
  int departure;
  int arrival;
};

int main() {
  string line;
  int cases;
  cin >> cases;
  getline(cin, line);
  for (int c = 1; c <= cases; c++) {
    int turnaroundTime;
    cin >> turnaroundTime;
    getline(cin, line);

    int tripsA;
    cin >> tripsA;
    int tripsB;
    cin >> tripsB;
    getline(cin, line);

    signed int minutesA[MAX_TIME];
    signed int minutesB[MAX_TIME];
    memset(minutesA, 0, sizeof(minutesA));
    memset(minutesB, 0, sizeof(minutesB));

    FOR(i, 0, tripsA) {
      getline(cin, line);
      int d_hour,d_minute,a_hour,a_minute;
      d_hour = atoi(line.substr(0,2).c_str());
      d_minute = atoi(line.substr(3,2).c_str());
      a_hour = atoi(line.substr(6,2).c_str());
      a_minute = atoi(line.substr(9,2).c_str());
      int departure = d_hour * 60 + d_minute;
      int arrival = a_hour * 60 + a_minute;
      FOR(t, departure, MAX_TIME) {
        minutesA[t]++;
      }
      FOR(t, (arrival+turnaroundTime), MAX_TIME) {
        minutesB[t]--;
      }
    }

    FOR(i, 0, tripsB) {
      getline(cin, line);
      int d_hour,d_minute,a_hour,a_minute;
      d_hour = atoi(line.substr(0,2).c_str());
      d_minute = atoi(line.substr(3,2).c_str());
      a_hour = atoi(line.substr(6,2).c_str());
      a_minute = atoi(line.substr(9,2).c_str());
      int departure = d_hour * 60 + d_minute;
      int arrival = a_hour * 60 + a_minute;
      FOR(t, departure, MAX_TIME) {
        minutesB[t]++;
      }
      FOR(t, (arrival+turnaroundTime), MAX_TIME) {
        minutesA[t]--;
      }
    }

    int trainsA = 0;
    int trainsB = 0;

    FOR(t, MIN_TIME, MAX_TIME) {
      if (trainsA < minutesA[t])
        trainsA = minutesA[t];
    }
    FOR(t, MIN_TIME, MAX_TIME) {
      if (trainsB < minutesB[t])
        trainsB = minutesB[t];
    }

    cout << "Case #" << c << ": " << trainsA << " " << trainsB  << endl;
  }
  return 0;
}
