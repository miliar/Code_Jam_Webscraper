#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct op {
  int sign, time;

  op(int sign, int time) : sign(sign), time(time) { }

  bool operator<(const op &other) const {
    if (time == other.time) {
      return sign > other.sign;
    } else {
      return time < other.time;
    }
  }
};

int tominutes(string stamp) {
  int hour = (stamp[0]-'0')*10 + (stamp[1]-'0');
  int minute = (stamp[3]-'0')*10 + (stamp[4]-'0');
  return hour*60 + minute;
}

int main() {
  int N;
  cin >> N;
  for (int casenum=1; casenum <= N; casenum++) {
    
    int T, NA, NB;
    cin >> T >> NA >> NB;

    vector<op> Aops;
    vector<op> Bops;

    for (int i=0; i<NA; i++) {
      string depart, arrive;
      cin >> depart >> arrive;
      int td = tominutes(depart);
      int ta = tominutes(arrive) + T;
      Aops.push_back(op(-1, td));
      Bops.push_back(op(+1, ta));
    }

    for (int i=0; i<NB; i++) {
      string depart, arrive;
      cin >> depart >> arrive;
      int td = tominutes(depart);
      int ta = tominutes(arrive) + T;
      Aops.push_back(op(+1, ta));
      Bops.push_back(op(-1, td));
    }

    sort(Aops.begin(), Aops.end());
    sort(Bops.begin(), Bops.end());

    int x = 0;
    int X = 0;
    for (int i=0; i<(int)Aops.size(); i++) {
      x += Aops[i].sign;
      X = min(X, x);
    }

    int y = 0;
    int Y = 0;
    for (int i=0; i<(int)Bops.size(); i++) {
      y += Bops[i].sign;
      Y = min(Y, y);
    }

    X = -X;
    Y = -Y;

    cout << "Case #" << casenum << ": " << X << " " << Y << endl;
  }

  return 0;
}
