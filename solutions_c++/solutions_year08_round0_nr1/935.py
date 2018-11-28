#include <iostream>
#include <sstream>
#include <string>
#include <map>

using std::string;
using std::cin;
using std::cout;
using std::cerr;
using std::endl;
using std::map;

#define FOR(i,s,e) for (int i = (s); i < (e); i++)

static int min;
static int m[1000][100];
static int v[100];

static void switcher(int snum, int qnum, unsigned char queries[]) {
  int sw = 0;
  int qi = 0;
  while (qi < qnum) {
    int best = 0;
    FOR(si, 0, snum) {
      if (m[qi][si] > m[qi][best])
        best = si;
    }
//    FOR(si, 0, snum) {
//      cerr << m[qi][si] << " ";
//    }
//    cerr << endl;
    qi += m[qi][best];
//    cerr << "qi="<<qi  <<  ", m["<<qi<<"]["<<best<<"]=" <<  m[qi][best] << "sw="<<sw << endl;
    if (qi < qnum)
      sw++;
  }
  min = sw;
}

static void init(int snum, int qnum, unsigned char queries[]) {
  memset(m, 0, sizeof(m));
  memset(v, 0, sizeof(v));
  min = 1024;
  FOR(qi, 0, qnum) {
    int s = queries[qi];
    FOR(si, 0, snum)
      v[si]++;
    v[s] = 0;
    FOR(si, 0, snum)
      m[qnum - (qi + 1)][si] = v[si];
  }
//  FOR(qi, 0, qnum) {
//    FOR(si, 0, snum) {
//      cerr << m[qi][si] << " ";
//    }
//    cerr << endl;
//  }
}

int main() {
  string line;
  int cases;
  cin >> cases;
  getline(cin, line);
  for (int c = 1; c <= cases; c++) {
    min = 1024;

    int searchEngineNumber;
    cin >> searchEngineNumber;
    getline(cin, line);
    map<string, unsigned char> searchEngines;
    for (unsigned char i = 0; i < searchEngineNumber; i++) {
      getline(cin, line);
      searchEngines[line] = i;
    }

    int queryNumber;
    cin >> queryNumber;
    getline(cin, line);
    if (queryNumber != 0) {
      unsigned char queries[1024];
      FOR(i, 0, queryNumber) {
        getline(cin, line);
        queries[i] = searchEngines[line];
      }
      init(searchEngineNumber, queryNumber, queries);
      switcher(searchEngineNumber, queryNumber, queries);
    } else {
      min = 0;
    }
    cout << "Case #" << c << ": " << min << endl;
  }
  return 0;
}
