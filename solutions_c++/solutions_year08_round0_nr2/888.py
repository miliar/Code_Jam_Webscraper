#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;


struct timestr {
  int hour;
  int minutes;
  timestr (int hour=0,int minutes = 0) 
    :hour (hour), minutes (minutes) {}
  timestr (const timestr& rhs) {
    hour = rhs.hour;
    minutes = rhs.minutes;
  }
  
  bool operator<(const timestr& rhs)  const {
    return hour < rhs.hour || (hour==rhs.hour&&minutes<rhs.minutes);
  }
  bool operator==(const timestr& rhs)  const {
    return hour==rhs.hour && minutes == rhs.minutes;
  }
  
};

struct trevent {
  timestr ev_time;
  int change_a;
  int change_b;
  bool operator<(const trevent& rhs) const {
    return ev_time < rhs.ev_time ||
      (ev_time == rhs.ev_time &&
       (change_a>0||change_b>0));
  }
  trevent (timestr ev_time, int change_a, int change_b) 
    : ev_time (ev_time), change_a (change_a), change_b (change_b) {}
  
    
};

void conv_time (string&  in, timestr& ret) {
  ret.hour = (in[0]-'0')*10 + (in[1]-'0');
  ret.minutes = (in[3]-'0')*10 + (in[4]-'0');
}

  
int main() {
  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases;++case_num) {
    int turnaround;
    cin >> turnaround;
    int na,nb;
    cin >> na >> nb;

    vector<trevent> events;
    
    // a to b trips
    for (int i = 0 ; i < na; ++i) {
      string dep,arr;
      cin >> dep >> arr;

      timestr dept,arrt;
      conv_time (dep,dept);
      conv_time (arr,arrt);
      arrt.minutes +=turnaround;
      arrt.hour+=arrt.minutes/60;
      arrt.minutes%=60;
      events.push_back (trevent (dept, -1,0));
      events.push_back (trevent (arrt, 0,1));
    }
    // b to a trips
    for (int i = 0 ; i < nb; ++i) {
      string dep,arr;
      cin >> dep >> arr;
      timestr dept,arrt;
      conv_time (dep,dept);
      conv_time (arr,arrt);
      arrt.minutes +=turnaround;
      arrt.hour+=arrt.minutes/60;
      arrt.minutes%=60;
      events.push_back (trevent (dept, 0,-1));
      events.push_back (trevent (arrt, 1,0));
    }
    sort (events.begin(),events.end());
    int min_a=0;
    int min_b=0;
    int ca = 0;
    int cb = 0;
    for (int i = 0; i < (int)events.size(); ++i) {
      ca += events[i].change_a;
      cb += events[i].change_b;
      min_a = min (min_a, ca);
      min_b = min (min_b, cb);
    }
    cout << "Case #" << case_num << ": " << -min_a << " " << -min_b << "\n";
  }
      

}
