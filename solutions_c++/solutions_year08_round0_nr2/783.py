#include <cstdio>
#include <vector>
#include <algorithm>

using std::vector;
using std::sort;

namespace {

enum EventType {DEPART, ARRIVE, SOLVED};

struct Event {
  Event(int t, EventType ty)
      :time(t), type(ty) {}

  bool operator < (const Event& other) const {
    return time < other.time ||
        (time == other.time && type == ARRIVE);
  }

  int time;
  EventType type;
};

inline int GetTime(int h, int m) {
  return h * 60 + m;
}

void ReadInput(vector<Event>* a_station,
               vector<Event>* b_station,
               int* set_up) {
  scanf("%d", set_up);
  int a_num, b_num;
  scanf("%d %d", &a_num, &b_num);
  for (int i = 0; i < a_num; i++) {
    int ha, hb, ma, mb;
    scanf("%d:%d %d:%d", &ha, &ma, &hb, &mb);
    a_station->push_back(Event(GetTime(ha, ma), DEPART));
    b_station->push_back(Event(GetTime(hb, mb) + *set_up, ARRIVE));
  }
  for (int i = 0; i < b_num; i++) {
    int ha, hb, ma, mb;
    scanf("%d:%d %d:%d", &hb, &mb, &ha, &ma);
    a_station->push_back(Event(GetTime(ha, ma) + *set_up, ARRIVE));
    b_station->push_back(Event(GetTime(hb, mb), DEPART));
  }
}

int Schedule(vector<Event>* station) {
  sort(station->begin(), station->end());

  int arr = 0;
  int dep = 0;

  while (arr < station->size() && dep < station->size()) {
    while (arr < station->size() && station->at(arr).type != ARRIVE)
      arr++;
    if (arr == station->size())
      break;
    while (dep < station->size()
           && (station->at(dep).type != DEPART
               || station->at(dep).time < station->at(arr).time)) {
      dep++;
    }

    if (dep < station->size()) {
      station->at(dep).type = SOLVED;
      dep++;
      arr++;
    }
  }
  
  int cnt = 0;
  for (int i = 0; i < station->size(); i++) {
    if (station->at(i).type == DEPART)
      cnt++;
  }
  return cnt;
}

void ProcessCase(int id) {
  vector<Event> a_station, b_station;
  int set_up_time;
  
  ReadInput(&a_station, &b_station, &set_up_time);

  printf("Case #%d: %d %d\n", id, Schedule(&a_station), Schedule(&b_station));
}
}

int main() {
  int case_num;
  scanf("%d", &case_num);
  for (int i = 1; i <= case_num; i++) {
    ProcessCase(i);
  }
  return 0;
}
