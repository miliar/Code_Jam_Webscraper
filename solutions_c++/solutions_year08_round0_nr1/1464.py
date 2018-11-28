#include <map>
#include <string>
#include <iostream>
using namespace std;

struct Engine {
  int last_round_seen;
};

int main() {
  int N;
  cin >> N;

  for (int case_num = 1; case_num <= N; ++case_num) {
    map<string, Engine> theEngines;

    int S;
    cin >> S;
    cin.ignore(100, '\n');

    while (S--) {
      string name;
      getline(cin, name);
      theEngines[name].last_round_seen = 0;
    }

    int Q;
    cin >> Q;
    cin.ignore(100, '\n');

    int round = 0;
    int engines_left = theEngines.size();

    while (Q--) {
      string query;
      getline(cin, query);

      if (theEngines[query].last_round_seen == round) {
        ++theEngines[query].last_round_seen;
        --engines_left;

        // can't "switch" to the engine we used last
        if (engines_left == 0) {
          ++theEngines[query].last_round_seen;
          ++round;
          engines_left = theEngines.size() - 1;
        }
      }

    }


    cout << "Case #" << case_num << ": " << round;
    cout << endl;

  }

  return 0;
}

