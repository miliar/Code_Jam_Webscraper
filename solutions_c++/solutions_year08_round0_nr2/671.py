#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");
void SolveCase();

int main() {
  int ncases;
  in >> ncases;
  for (int tc = 0; tc < ncases; tc++) {
    out << "Case #" << (tc+1) << ": ";
    SolveCase();
  }
  return 0;
}

int ToTime(const string &s) {
  int h = atoi(s.substr(0,2).c_str());
  int m = atoi(s.substr(3).c_str());
  return h*60+m;
}

struct Event {
  Event(int t, int l, int y): time(t), loc(l), type(y) {}
  int time;
  int loc;
  int type;
};
bool operator<(const Event &lhs, const Event &rhs) {
  if (lhs.time != rhs.time) return lhs.time < rhs.time;
  if (lhs.type != rhs.type) return lhs.type == 1;
  return false;
}

void SolveCase() {
  int tat, na, nb;
  in >> tat >> na >> nb;
  vector<Event> events;
  for (int i = 0; i < na; i++) {
    string t1, t2;
    in >> t1 >> t2;
    events.push_back(Event(ToTime(t1), 0, -1));
    events.push_back(Event(ToTime(t2) + tat, 1, 1));
  }
  for (int i = 0; i < nb; i++) {
    string t1, t2;
    in >> t1 >> t2;
    events.push_back(Event(ToTime(t1), 1, -1));
    events.push_back(Event(ToTime(t2) + tat, 0, 1));
  }
  sort(events.begin(), events.end());
  int ona = 0, onb = 0;
  na = nb = 0;
  for (int i = 0; i < (int)events.size(); i++) {
    if (events[i].loc == 0) {
      if (na == 0 && events[i].type == -1) {na++; ona++;}
      na += events[i].type;
    } else {
      if (nb == 0 && events[i].type == -1) {nb++; onb++;}
      nb += events[i].type;
    }
  }
  out << ona << " " << onb << endl;
}