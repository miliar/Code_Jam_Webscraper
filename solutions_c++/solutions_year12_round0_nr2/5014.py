#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;
int T, N, P, S;
int offsets[] = {0, -1, -2, -4};

int check(vector<int>& sums) {
  int result = 0;
  vector<pair<int, vector<pair<int, int> > > > table;
  for (int i = 0; i < sums.size(); i++) {
    vector<pair<int, int> > cur;
    int x = -10;
    int y = -10;
    int z = -10;
    if (sums[i] % 3 == 0) {
      x = sums[i] / 3;
      y = x;
      if (y >= P && sums[i] >= 0) cur.push_back(make_pair(0, y));
    }
    if ((sums[i] - 1) % 3 == 0) {
      x = (sums[i] - 1) / 3;
      y = x + 1;
      if (y >= P && sums[i] - 1 >= 0) cur.push_back(make_pair(0, y));
    } 
    if ((sums[i] - 2) % 3 == 0) {
      x = (sums[i] - 2) / 3;
      y = x + 1;
      z = x + 2;
      if (y >= P && sums[i] - 2 >= 0) cur.push_back(make_pair(0, y));
      if (z >= P && sums[i] - 2 >= 0) cur.push_back(make_pair(1, z));
    } if ((sums[i] - 4) % 3 == 0) {
      x = (sums[i] - 4) / 3;
      z = x + 2;
      if (z >= P && sums[i] - 4 >= 0) cur.push_back(make_pair(1, z));
    } if ((sums[i] - 3) % 3 == 0) {
      x = (sums[i] - 3) / 3;
      z = x + 2;
      if (z >= P && sums[i] - 3 >= 0) cur.push_back(make_pair(1, z));
    }
    table.push_back(make_pair(sums[i], cur));
  }
  int special = 0, nonspecial = 0;
  for (int i = 0; i < table.size(); i++) {
    int score = table[i].first;
    vector<pair<int, int> >& inV = table[i].second;
    if (inV.size() == 0) continue;
    if (inV[0].first == 1) special++;
    else nonspecial++;
    cout << score << "\t";
    for (int j = 0; j < inV.size(); j++) {
      cout << inV[j].first << ", " << inV[j].second << " ";
    }
    cout << endl;
  }
  return nonspecial + min(special, S);
  return 0;
}
int main(int argc, char** argv) {
  ifstream inF(argv[1]);
  string outFile = argv[1];
  outFile += ".out";
  ofstream outF(outFile.c_str());
  inF >> T;
  for (int i = 0; i < T; i++) {
    inF >> N >> S >> P;
    vector<int> cur;
    for (int j = 0; j < N; j++) {
      int tmp;
      inF >> tmp;
      cur.push_back(tmp);
    } 
    outF << "Case #" << i + 1 << ": ";
    outF << check(cur) << endl;
  }
  inF.close();
  outF.close();
  return 0;
}
