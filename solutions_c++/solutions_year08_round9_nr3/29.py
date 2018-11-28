#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <time.h>
#include <vector>
using namespace std;
typedef __int64 ll;
typedef unsigned __int64 ull;

///////////////////////////////////////////////////////////////////////////////////////////////////
// Parsing
vector<string> Split(const string &s, const string &delimiters = " ") {
  vector<string> result;
  string temp;
  for (int i = 0; i < (int)s.size(); i++) {
    if (delimiters.find(s[i]) == string::npos) {
      temp += s[i];
    } else {
      if ((int)temp.size() > 0)
        result.push_back(temp);
      temp = "";
    }
  }
  if ((int)temp.size() > 0)
    result.push_back(temp);
  return result;
}
vector<string> SplitDelimiters(const string &s, const string &delimiters = " ") {
  vector<string> result;
  string temp;
  for (int i = 0; i < (int)s.size(); i++) {
    if (delimiters.find(s[i]) == string::npos) {
      if ((int)temp.size() > 0 || (int)result.size() == 0)
        result.push_back(temp);
      temp = "";
    } else {
      temp += s[i];
    }
  }
  result.push_back(temp);
  return result;
}

///////////////////////////////////////////////////////////////////////////////////////////////////
// Debugging tools
int gPrecision = -1;
string ToString(bool x) {return (x? "1" : "0");}
string ToString(char ch) {string s; s += ch; return s;}
string ToString(unsigned char ch) {string s; s += ch; return s;}
string ToString(double x) {
  ostringstream out;
  if (gPrecision != -1) {out.precision(gPrecision); out << fixed;}
  out << x;
  string temp = out.str();
  if (temp[0] != '-') // Never return "-0.0000"
    return temp;
  for (int i = 1; i < (int)temp.size(); i++)
    if (temp[i] != '.' && temp[i] != '0')
      return temp;
  return temp.substr(1);
}
string ToString(float x) {return ToString(double(x));}
string ToString(int n) {ostringstream out; out << n; return out.str();}
string ToString(unsigned int n) {ostringstream out; out << n; return out.str();}
string ToString(ll n) {ostringstream out; out << n; return out.str();}
string ToString(ull n) {ostringstream out; out << n; return out.str();}
string ToString(const string &s) {return s;}
template <class S, class T> string ToString(const pair<S, T> &x) {
  return "(" + ToString(x.first) + "," + ToString(x.second) + ")";
}
template <class S, class T> string ToString(const map<S, T> &x, const string &delim = ",") {
  string s = "{";
  for (map<S, T>::const_iterator it = x.begin(); it != x.end(); ++it)
    s += (it == x.begin()? "" : delim) + ToString(it->first) + "->" + ToString(it->second);
  return s + "}";
}
template <class T> string ToString(const set<T> &x, const string &delim = ",") {
  string s = "{";
  for (set<T>::const_iterator it = x.begin(); it != x.end(); ++it)
    s += (it == x.begin()? "" : delim) + ToString(*it);
  return s + "}";
}
template <class T> string ToString(const vector<T> &x, const string &delim = ",") {
  string s = "(";
  for (int i = 0; i < (int)x.size(); i++)
    s += (i == 0? "" : delim) + ToString(x[i]);
  return s + ")";
}

///////////////////////////////////////////////////////////////////////////////////////////////////
// Other tools
///////////////////////////////////////////////////////////////////////////////////////////////////

ifstream in("in.txt");
ofstream out("out.txt");
void SolveCase();
int main() {
  int num_cases;
  in >> num_cases;
  clock_t start_time = clock();
  for (int i = 0; i < num_cases; i++) {
    out << "Case #" << (i+1) << ": ";
    cout << "Solving case #" << (i+1) << " of " << num_cases << "..." << endl;
    SolveCase();
  }
  clock_t end_time = clock();
  double duration = double(end_time - start_time) / CLOCKS_PER_SEC;
  cout << "Run-time: " << duration << " seconds" << endl;
  return 0;
}

///////////////////////////////////////////////////////////////////////////////////////////////////

vector<int> BFS(const vector<string> &grid, int src) {
  int n = (int)grid.size(), m = (int)grid[0].size();
  queue<int> q;
  q.push(src);
  vector<int> result(n*m, -1);
  result[src] = 0;

  while (!q.empty()) {
    int pos = q.front();
    q.pop();
    int y = pos / m, x = pos % m;
    for (int dx = -1; dx <= 1; dx++)
      for (int dy = -1; dy <= 1; dy++)
        if (dx * dx + dy * dy == 1) {
          int x2 = x + dx, y2 = y + dy;
          if (x2 < 0 || y2 < 0 || x2 >= m || y2 >= n) continue;
          if (grid[y2][x2] == '.') continue;
          int i2 = y2*m + x2;
          if (result[i2] != -1) continue;
          result[i2] = result[pos] + 1;
          q.push(i2);
        }
    
  }
  return result;
}

void Solve(vector<vector<int> > &is_mine, vector<vector<int> > &temp_sums, vector<vector<int> > &ngb,
           const vector<vector<int> > &sums,
           int r, int c, int value, int *best) {
  int n = (int)is_mine.size(), m = (int)is_mine[0].size();
  for (int val = 0; val < 2; val++) {
    bool is_bad = false;
    is_mine[r][c] = val;
    for (int dx = -1; dx <= 1; dx++)
      for (int dy = -1; dy <= 1; dy++) {
        int x2 = c + dx, y2 = r + dy;
        if (x2 < 0 || y2 < 0 || x2 >= m || y2 >= n) continue;
        temp_sums[y2][x2] += val;
        ngb[y2][x2]--;
        if (ngb[y2][x2] == 0 && temp_sums[y2][x2] != sums[y2][x2])
          is_bad = true;
      }

    if (!is_bad) {
      int new_value = value;
      if (2*r+1 == n) new_value += val;
      if (r == n-1 && c == m-1) {
        *best = max(*best, new_value);
      } else {
        int r2 = r, c2 = c;
        c2++;
        if (c2 >= m) {
          c2 = 0;
          r2++;
        }
        Solve(is_mine, temp_sums, ngb, sums, r2, c2, new_value, best);
      }
    }

    for (int dx = -1; dx <= 1; dx++)
      for (int dy = -1; dy <= 1; dy++) {
        int x2 = c + dx, y2 = r + dy;
        if (x2 < 0 || y2 < 0 || x2 >= m || y2 >= n) continue;
        temp_sums[y2][x2] -= val;
        ngb[y2][x2]++;
      }
    is_mine[r][c] = 0;
  }
}

void SolveCase() {
  int n, m;
  in >> n >> m;
  vector<vector<int> > sums(n, vector<int>(m, 0));
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      in >> sums[i][j];
  vector<vector<int> > ngb(n, vector<int>(m, 0));
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
      for (int dy = -1; dy <= 1; dy++)
        for (int dx = -1; dx <= 1; dx++) {
          int y2 = i + dy, x2 = j + dx;
          if (y2 < 0 || x2 < 0 || y2 >= n || x2 >= m) continue;
          ngb[y2][x2]++;
        }
  vector<vector<int> > is_mine(n, vector<int>(m, 0));
  vector<vector<int> > temp_sums(n, vector<int>(m, 0));
  int best = 0;
  Solve(is_mine, temp_sums, ngb, sums, 0, 0, 0, &best);
  out << best << endl;
}
