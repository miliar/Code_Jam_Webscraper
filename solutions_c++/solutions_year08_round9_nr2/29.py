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

int BFS(int n, int m, int src, int *dx, int *dy) {
  queue<int> q;
  q.push(src);
  vector<int> result(n*m, -1);
  result[src] = 0;

  while (!q.empty()) {
    int pos = q.front();
    q.pop();
    int y = pos / m, x = pos % m;
    for (int i = 0; i < 2; i++) {
      int x2 = x + dx[i], y2 = y + dy[i];
      if (x2 < 0 || y2 < 0 || x2 >= m || y2 >= n) continue;
      int i2 = y2 * m + x2;
      if (result[i2] != -1) continue;
      result[i2] = result[pos] + 1;
      q.push(i2);
    }  
  }
  int cnt = 0;
  for (int i = 0; i < n*m; i++)
    if (result[i] != -1)
      cnt++;
  return cnt;
}

void SolveCase() {
  int n, m;
  int dx[2], dy[2];
  in >> m >> n;
  in >> dx[0] >> dy[0];
  in >> dx[1] >> dy[1];
  int r, c;
  in >> c >> r;
  out << BFS(n, m, r*m+c, dx, dy) << endl; 
}
