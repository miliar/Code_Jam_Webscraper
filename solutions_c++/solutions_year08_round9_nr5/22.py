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

int GetBit(ll n, int k) {
  if (k == -1) return 0; 
  ll one = ll(1);
  if ((n & (one << k)) > 0)
    return 1;
  else
    return 0;
}

string Encode(ll bm) {
  string s;
  for (int i = 0; i < 8; i++)
    if (GetBit(bm, 7-i) == 1)
      s += '#';
    else
      s += '.';
  return s;
}

void Solve(ll old_code, ll new_code, const string &s, int pos, int score_so_far, vector<int> &result, int *best_score) {
  bool can_be_0 = true, can_be_1 = true;
  int top_bit = GetBit(old_code, int(s.size()) - 1 - pos);
  int left_bit = (new_code & 1);
  if (pos >= (int)s.size()) {
    can_be_1 = false;
  } else {
    if (s[pos] == '.')
      can_be_1 = false;
    else if (s[pos] == '#')
      can_be_0 = false;
    else {
      if (left_bit == top_bit) {
        if (left_bit == 1)
          can_be_1 = false;
        else
          can_be_0 = false;
      }
    }
  }
  for (int b = 0; b < 2; b++) {
    if (b == 0 && !can_be_0) continue;
    if (b == 1 && !can_be_1) continue;
    int new_score = score_so_far;
    if (b != left_bit)
      new_score++;
    if (b != top_bit)
      new_score++;
    if (pos >= (int)s.size()) {
      result[int(new_code)] = max(result[int(new_code)], new_score);
      *best_score = max(*best_score, new_score);
      return;
    } else {
      Solve(old_code, 2*new_code + b, s, pos+1, new_score, result, best_score);
    }
  }
}

void SolveCase() {
  int n, m, best_score = -1;
  in >> n >> m;
  vector<string> grid(n);
  for (int i = 0; i < n; i++)
    in >> grid[i];

  vector<pair<ll, int> > old_options;
  old_options.push_back(make_pair(0, 0));
  for (int i = 0; i <= n; i++) {
    string s;
    if (i < n)
      s = grid[i];
    else for (int j = 0; j < m; j++)
      s += '.';

    vector<int> temp(1<<16, -1);
    for (int j = 0; j < (int)old_options.size(); j++) {
      ll old_code = old_options[j].first;
      int score = old_options[j].second;
      Solve(old_code, 0, s, 0, score, temp, &best_score);
    }

    old_options.clear();
    for (int i = 0; i < (int)temp.size(); i++)
    if (temp[i] >= 0)
      old_options.push_back(make_pair(ll(i), temp[i]));
  }

  out << best_score << endl;
}
