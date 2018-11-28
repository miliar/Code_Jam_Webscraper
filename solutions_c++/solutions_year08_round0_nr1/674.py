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


void SolveCase() {
  string temp;
  int S, O;
  in >> S;
  getline(in, temp);
  map<string, int> engine_map;
  vector<int> queries;
  for (int i = 0; i < S; i++) {
    getline(in, temp);
    engine_map[temp] = (int)engine_map.size();
  }
  in >> O;
  getline(in, temp);
  for (int i = 0; i < O; i++) {
    getline(in, temp);
    queries.push_back(engine_map[temp]);
  }
  /*vector<bool> seen(S, false);
  int seen_count = 0, result = 0;
  for (int i = 0; i < O; i++) {
    if (!seen[queries[i]]) {
      seen[queries[i]] = true;
      seen_count++;
      if (seen_count == S) {
        seen = vector<bool>(S, false);
        seen_count = 0;
        result++;
      }
    }
  }*/
  vector<int> answer(S, 0);
  for (int i = 0; i < O; i++) {
    answer[queries[i]] = O + 1000;
    int mv = answer[0];
    for (int j = 0; j < S; j++)
      mv = min(mv, answer[j]);
    for (int j = 0; j < S; j++)
      answer[j] = min(mv+1, answer[j]);
  }
  int mv = answer[0];
  for (int j = 0; j < S; j++)
    mv = min(mv, answer[j]);
  out << mv << endl;
}