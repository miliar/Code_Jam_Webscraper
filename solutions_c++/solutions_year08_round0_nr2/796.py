#include <iostream>
#include <algorithm>
#include <string>
#include <set>
using namespace std;

const int TO_A = 0;
const int TO_B = 1;
const int READY_A = 2;
const int READY_B = 3;
const int FROM_A = 4;
const int FROM_B = 5;

struct event
{
  int type;
  int min;
  int param;
  event(int type, int min, int param = 0) : type(type), min(min), param(param) {}
  bool operator <(const event &rhs) const {
    if (min != rhs.min) { return min < rhs.min; }
    if (type != rhs.type) { return type < rhs.type; }
    return param < rhs.param;
  }
};

int tomin(const string &t)
{
  int m = 0;
  m += (t[0]-'0')*600;
  m += (t[1]-'0')*60;
  m += (t[3]-'0')*10;
  m += (t[4]-'0')*1;
  return m;
}

int main()
{
  int N;
  cin >> N;

  for (int a = 1; a <= N; a++) {
    cout << "Case #" << a << ": ";
    int t;
    cin >> t;
    
    int na, nb;
    cin >> na >> nb;

    multiset<event> que;
    for (int i = 0; i < na; i++) {
      string s1, s2;
      cin >> s1 >> s2;
      que.insert(event(FROM_A, tomin(s1), tomin(s2)));
    }
    for (int i = 0; i < nb; i++) {
      string s1, s2;
      cin >> s1 >> s2;
      que.insert(event(FROM_B, tomin(s1), tomin(s2)));
    }

    int train_a = 0;
    int train_b = 0;
    int max_train_a = 0;
    int max_train_b = 0;
    while (!que.empty()) {
      event e = *que.begin();
      que.erase(que.begin());

      switch (e.type) {
      case READY_A:
	train_a--;
	break;
      case READY_B:
	train_b--;
	break;
      case FROM_A:
	que.insert(event(TO_B, e.param));
	max_train_a = max(++train_a, max_train_a);
	break;
      case FROM_B:
	que.insert(event(TO_A, e.param));
	max_train_b = max(++train_b, max_train_b);
	break;
      case TO_A:
	que.insert(event(READY_A, e.min + t));
	break;
      case TO_B:
	que.insert(event(READY_B, e.min + t));
	break;
      }
    }

    cout << max_train_a << " " << max_train_b << endl;
  }
    
  return 0;
}
