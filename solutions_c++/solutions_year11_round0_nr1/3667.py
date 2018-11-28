#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

class Solution {
public:
  int solve(int a, int b) {
    int result = -1;
    return result;
  }
};

int stoi(string s) {
  int r;
  stringstream ss;
  ss << s;
  ss >> r;
  return r;
}

// BEGIN CUT HERE
int main() {
  //  Solution ___solution;
  int s_num = 0;
  int sn, i, j = 0;
  string line;
    
  //stringstream ss;
  //static const string empty_string;
  //ss << str; ss >> num;
  //ss.str(empty_string);ss.clear();
  cin >> s_num;
  getline(cin, line);
  for (sn = 0; sn < s_num; sn++) {
    int total = 0;
    vector <char> c;
    vector <int> n;
    int f = 1;
    int l_num = 0;
    cin >> l_num;
    getline(cin, line);
    //cout << line << endl;
    line = line + " ";
    for (i = 1; i <= line.size(); i++) {
      if (' ' == line[i]) {
	//cout << i << "-" << f << "-" << i-f << endl;
	string buf = line.substr(f, i-f);
	f = i+1;
	if ('O' == buf[0]) {
	  c.push_back('O');
	}
	else if('B' == buf[0]) {
	  c.push_back('B');
	}
	else {
	  int t = stoi(buf);
	  n.push_back(t);
	}
      }
    }
    int tb = 0;
    int to = 0;
    int pb = 1;
    int po = 1;
    /*    for (i = 0; i < c.size(); i++) {
      cout << c[i] << "::";
      cout << n[i] << "::";
    }
    cout << endl;*/
    for (i = 0; i < c.size(); i++) {
      if ('O' == c[i]) {
	int o = 0;
	o = n[i] - po;	
	//cout << "ni" << n[i] << ":";
	//cout << "po" << po << ":";
	po = n[i];
	//cout << "o" << o << ":";
	if (o < 0) { o *= -1; }
	o -= tb; tb = 0;
	if (o < 0) { o = 0; }
	o++;//push
	//cout << "o" << o << ":";
	total += o;
	to += o;
      }
      else if ('B' == c[i]) {
	int b = 0;
	b = n[i] - pb;
	//cout << "b" << b << ":";
	pb = n[i];
	if (b < 0) { b *= -1; }
	b -= to; to = 0;
	if (b < 0) { b = 0; }
	b++;//push
	//cout << "b" << b << ":";
	total += b;
	tb += b;
      }
    }
    cout << "Case #" << sn + 1 << ": " << total << endl;
  }
}
// END CUT HERE

