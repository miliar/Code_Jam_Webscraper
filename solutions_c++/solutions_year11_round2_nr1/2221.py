#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<cstdlib>
#include<cstdio>
#include<iomanip>
#include<sstream>

using namespace std;

template <class T>
bool not_0(T it) {
  return it != '0';
}

double wp(const string& str) {
  int n = 0;
  int w = 0;
  for (string::const_iterator it = str.begin(); it != str.end(); ++it) {
    if (*it != '.') ++n;
    if (*it == '1') ++w;
  }

  return static_cast<double>(w) / static_cast<double>(n);
}

void solve(vector<string>& strs) {

  vector<double> wp_list;
  vector<double> owp_list;
  vector<double> oowp_list;

  for (vector<string>::iterator it = strs.begin(); it != strs.end(); ++it) {
    int now_idx = it-strs.begin();
    wp_list.push_back(wp(*it));
  }

  for (vector<string>::iterator it = strs.begin(); it != strs.end(); ++it) {
    int now_idx = it-strs.begin();
    
    vector<int> idx_list;
    for (string::iterator jt = it->begin(); jt != it->end(); ++jt) {
      if (*jt != '.') {
        idx_list.push_back(jt - it->begin());
      }
    }

    double OWP = 0.0;
    for (vector<int>::iterator jt = idx_list.begin(); jt != idx_list.end(); ++jt) {
      string s = strs[*jt];
      s[now_idx] = '.';
      OWP += wp(s);
    }
    owp_list.push_back(OWP/static_cast<double>(idx_list.size()));
  }

  for (vector<string>::iterator it = strs.begin(); it != strs.end(); ++it) {
    int now_idx = it-strs.begin();
    vector<int> idx_list;
    for (string::iterator jt = it->begin(); jt != it->end(); ++jt) {
      if (*jt != '.') {
        idx_list.push_back(jt - it->begin());
      }
    }
    double OOWP = 0.0;
    for (vector<int>::iterator jt = idx_list.begin(); jt != idx_list.end(); ++jt) {
      OOWP += owp_list[*jt];
    }
    oowp_list.push_back(OOWP/static_cast<double>(idx_list.size()));
  }

  for (int i = 0; i < strs.size(); ++i) {
    // stringstream ss;
    // ss << setprecision(10) << wp_list[i] / 4 + owp_list[i] / 2 + oowp_list[i] / 4;
    // string s = ss.str();

    // string::reverse_iterator it;
    // for (it = s.rbegin(); it != s.rend(); ++it) {
    //   if (*it == '0') {
    //     int i = s.rend() - it;
    //     s = s.substr(0, s.length() - i + 1);
    //     break;
    //   }
    // }

    // cout << s << endl;
    cout << setprecision(6) << wp_list[i] / 4 + owp_list[i] / 2 + oowp_list[i] / 4<< endl;

  }
}

int main() {
  int test_num;
  cin >> test_num;

  for (int t = 1; t <= test_num; ++t) {
    int n;
    cin >> n;
    string s;
    getline(cin, s);

    vector<string> lines;
    for (int i = 0; i < n; ++i) {
      string s;
      getline(cin, s);
      lines.push_back(s);
    }

    cout << "Case #" << t << ":" << endl;
    solve(lines);
  }
}
