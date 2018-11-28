#include <iostream>
#include <fstream>
#include <cstring>
#include <map>
#include <string>
using namespace std;

char combine[26][26];
map<char, string> opposed;
char hasChar[26];

int main(int argc, char** argv) {
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  unsigned T = 0;
  ifs >> T;

  string list;
  for (unsigned t = 0; t < T; ++t) {
    unsigned C = 0;
    ifs >> C;
    memset(combine, 0, sizeof(combine));
    for (unsigned c = 0; c < C; ++c) {
      char e1, e2, e3;
      ifs >> e1 >> e2 >> e3;
      combine[e1 - 'A'][e2 - 'A'] = e3;
      combine[e2 - 'A'][e1 - 'A'] = e3;
    }

    unsigned D = 0;
    ifs >> D;
    opposed.clear();
    for (unsigned d = 0; d < D; ++d) {
      char e1, e2;
      ifs >> e1 >> e2;
      opposed[e1] += e2;
      opposed[e2] += e1;
    }

    unsigned N = 0;
    ifs >> N;
    list.clear();
    memset(hasChar, 0, sizeof(hasChar));
    for (unsigned n = 0; n < N; ++n) {
      char e2;
      ifs >> e2;
      if (0 == list.size()) {
        list.push_back(e2);
        hasChar[e2 - 'A'] += 1;
        continue;
      }
      
      // Combine.
      char& e1 = list.at(list.size() - 1);
      char e3 = combine[e1 - 'A'][e2 - 'A'];
      if (e3) {
        hasChar[e1 - 'A'] -= 1;
        hasChar[e3 - 'A'] += 1;
        e1 = e3; 
        continue;
      }

      // Opposed.
      const string& opStr = opposed[e2];
      for (unsigned i = 0; i < opStr.size(); ++i) {
        char e = opStr[i]; 
        if (hasChar[e - 'A']) {
          list.clear();
          memset(hasChar, 0, sizeof(hasChar));
          break;
        }
      }
      if (0 == list.size()) continue;

      // Normal.
      list.push_back(e2);
      hasChar[e2 - 'A'] += 1;
    }

    // Output.
    ofs << "Case #" << t + 1 << ": [";
    for (unsigned i = 0; i < list.size(); ++i) {
      ofs << list[i];
      if (i != list.size() - 1) ofs << ", ";
    }
    ofs << "]" << endl;
  }


return 0;
}
