#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

const int dy[] = { -1, 0, 1, 0 };
const int dx[] = { 0, 1, 0, -1 };

char arr[16][16];
bool isGoal[16][16];

set<long long> all;

inline long long getKey(const vector <pair<int, int> >& boxes) {
  long long res = 0;
  for (int i = 0; i < boxes.size(); i++) {
    res = res * 12 + boxes[i].first;
    res = res * 12 + boxes[i].second;
  }
  return res;
}

int fillArr(vector< pair<int, int> >& boxes, long long key) {
  int hits = 0;
  for (int i = boxes.size()-1; i >= 0; i--) {
    boxes[i].second = key % 12; key /= 12;
    boxes[i].first = key % 12; key /= 12;
    if (isGoal[boxes[i].first][boxes[i].second]) hits++;
  }
  return hits;
}

bool isDangerous(vector<pair<int, int> >& boxes) {
  if (boxes.size() == 1) return false;
  static int ctr = 0;
  static int step[12][12];
  ctr++;
  for (int i = 0; i < boxes.size(); i++) {
    int r = boxes[i].first, c = boxes[i].second;
    step[r][c] = ctr;
  }
  for (int i = 0; i < boxes.size(); i++) {
    int r = boxes[i].first, c = boxes[i].second;
    bool isDangerous = true;
    for (int d = 0; d < 4; d++) {
      int rr = r + dy[d], cc = c + dx[d];
      if (rr < 0 || rr >= 12 || cc < 0 || cc >= 12) continue;
      if (step[rr][cc] == ctr) { isDangerous = false; break; }
    }
    if (isDangerous) return true;
  }
  return false;
}

void trace(long long key, int rows, int cols, vector<pair<int, int> >& boxes, map<long long, long long>& mm) {
  if (key < 0) return;
  for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) if (arr[i][j] == 'w' || arr[i][j] == 'x' || arr[i][j] == 'o') arr[i][j] = '.';

  fillArr(boxes, key);
  for (int i = 0; i < boxes.size(); i++) arr[boxes[i].first][boxes[i].second] = 'o';
  for (int i = 0; i < rows; i++) cout << arr[i] << endl;
  cout << endl;
  trace(mm[key], rows, cols, boxes, mm);
}

int process() {
  memset(arr, 0, sizeof(arr));
  memset(isGoal, 0, sizeof(isGoal));
  all.clear();
  int rows, cols; cin >> rows >> cols;
  vector< pair<int, int> > boxes;
  for (int i = 0; i < rows; i++) cin >> arr[i];
  for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) if (arr[i][j] == 'w' || arr[i][j] == 'x') isGoal[i][j] = true;
  int hits = 0;
  for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) if (arr[i][j] == 'w' || arr[i][j] == 'o') {
    if (arr[i][j] == 'w') hits++;
    boxes.push_back(make_pair(i, j));
  }

  if (hits == boxes.size()) return 0;

  vector<long long> q[2];

  long long key = getKey(boxes);
  all.insert(key);
  map<long long, long long> mm; mm[key] = -1;

  int curr = 0, next = 1;
  q[curr].push_back(key);
  int steps = 0;
  while (q[curr].size() > 0) {
    q[next].clear();
    steps++;
    for (int i = 0; i < q[curr].size(); i++) {
      if (fillArr(boxes, q[curr][i]) == boxes.size()) {
        //trace(q[curr][i], rows, cols, boxes, mm);
        return steps-1;
      }
      bool dangerous = isDangerous(boxes);
      for (int b = 0; b < boxes.size(); b++) {
        int r = boxes[b].first, c = boxes[b].second;
        for (int d = 0; d < 4; d++) {
          int rr = r + dy[d], cc = c + dx[d];
          if (rr < 0 || rr >= rows || cc < 0 || cc >= cols) continue;
          if (arr[rr][cc] == '#') continue;
          int fr = r - dy[d], fc = c - dx[d];
          if (fr < 0 || fr >= rows || fc < 0 || fc >= cols) continue;
          if (arr[fr][fc] == '#') continue;
          bool found = false;
          for (int k = 0; k < boxes.size(); k++) if (rr == boxes[k].first && cc ==boxes[k].second) { found = true; break; }
          if (found) continue;
          for (int k = 0; k < boxes.size(); k++) if (fr == boxes[k].first && fc ==boxes[k].second) { found = true; break; }
          if (found) continue;

          boxes[b].first = rr; boxes[b].second = cc;
          key = getKey(boxes);
          bool nextDangerous = isDangerous(boxes);
          boxes[b].first = r; boxes[b].second = c;
          if (dangerous && nextDangerous) continue;
          if (all.find(key) != all.end()) continue;
          all.insert(key); mm[key] = q[curr][i];
          q[next].push_back(key);
        }
      }
    }
    curr = 1 - curr; next = 1 - next;
  }

  return -1;
}

void init() {
}

int main() {
  int cases; cin >> cases;
  for (int caseNo = 1; caseNo <= cases; caseNo++) {
    cout << "Case #" << caseNo << ": " << process() << endl;
  }
  return 0;
}

