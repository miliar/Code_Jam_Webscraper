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

vector <char> dtob(int x, int bs) {
  int bit = 1, i;
  vector <char> c;
  for (i = 0; i < bs; i++) {
    c.push_back('0');
  }
  for (i = 0; i < bs; i++) {
    if (x & bit) {
      c[i] = '1';
    }
    bit <<= 1;
  }
  return c;
}

int btod(vector <char> v) {
  int r = 0;
  int i = 0;
  int n = 1;
  for (i = 0; i < v.size(); i++) {
    if ('1' == v[i]) {
      r += n;
    }
    n *= 2;
  }
  return r;
}

bool is_no(vector < vector <char> > v) {
  bool result = true;
  int i, j = 0;
  int r = 0;
  for (i = 0; i < v[0].size(); i++) {
    int tmp = 0;
    for (j = 0; j < v.size(); j++) {
      if ('1' == v[j][i]){ r++; }
    }
    if (0 != r % 2) {
      r = 1; result = false; break;
    }
  }
  return result;
}

// BEGIN CUT HERE
int main() {
  //  Solution ___solution;
  int s_num = 0;
  int sn, h, i, j, k = 0;
  string line;
  const int BitSize = sizeof(int) * 8;

  cin >> s_num;
  getline(cin, line);

  for (sn = 0; sn < s_num; sn++) {
    int total = 0;
    int l_num = 0;
    cin >> l_num;
    string s = "";
    vector < vector <char> > vvc;
    vector <int> vi;
    for (i = 0; i < l_num; i++) {
      int num = 0;
      cin >> num;      
      vi.push_back(num);
      vector <char> vc = dtob(num, BitSize);
      vvc.push_back(vc);
    }
    
    bool is_n = is_no(vvc);
    if (is_n) {
      sort(vi.begin(), vi.end());
      for (i = 1; i < vi.size(); i++ ) {
	total += vi[i];
      }
    }
    else {
    }

    cout << "Case #" << sn + 1 << ": ";
    if (0 == total) { cout << "NO"; }
    else { cout << total; }
    cout << endl;
    
    
    /*
    int total = 0;
    int is_c = 0;
    int is_d = 0;
    int l_num = 0;
    string buf = "";
    vector <string> cs;
    vector <string> ds;
    vector <char> seqv;

    cin >> is_c;
    if (1 <= is_c) { 
      cout << "c: ";
      for (i = 0; i < is_c; i++) {
	string tmp; 
	cin >> tmp;
	cout << tmp << ",";
	cs.push_back(tmp);
      }
    }
    cout << endl;

    cin >> is_d;
    if (1 <= is_d) {
      cout << "d: ";
      for (i = 0; i < is_d; i++) {
	string tmp; 
	cin >> tmp;
	cout << tmp << ",";
	ds.push_back(tmp);
      }
    }
    cout << endl;

    cin >> l_num;
    cin >> buf;
    cout << buf << endl;

    
    for (h = 0; h < ds.size(); h++) {
      //cout << ds[h] << endl;
      for (i = 0; i < buf.size(); i++) {
	bool is_find = false;
	//cout << "i:" << i  << ":" << buf[i] << ":" << endl;
	if ((ds[h][0] == buf[i]) || (ds[h][1] == buf[i])) {
	  for (j = i+1; j <= (buf.size() - 1); j++) {
	    //cout << "j:" << j  << ":" << buf[j] << ":" << endl;
	    if ((ds[h][0] == buf[i]) && (ds[h][1] == buf[j])) {
	      for (k = i; k <= j; k++) { buf[k] = ' '; i = j;}
	      is_find = true;
	      break;
	    }
	    else if ((ds[h][1] == buf[i]) && (ds[h][0] == buf[j])) {
	      for (k = i; k <= j; k++) { buf[k] = ' '; i = j;}
	      is_find = true;
	      break;
	    }
	  }
	}
	else {}
	if (is_find) { break; }
      }
    }
    //cout << endl;
    //cout << buf << endl;
    //cout << endl;
    
    for (i = 0; i < buf.size(); i++) {
      if (' ' == buf[i]) {}
      else { seqv.push_back(buf[i]);  }
    }
    
    for (i = 0; i < seqv.size(); i++) {
      cout << seqv[i] << ":";
    }
    cout << endl;

    for (h = 0; h < cs.size(); h++) {
      //cout << cs[h] << endl;
      for (i = 0; i < seqv.size(); i++) {
	bool is_find = false;
	if ((cs[h][0] == seqv[i]) || (cs[h][1] == seqv[i])) {
	  int ti = i + 1;
	  while (' ' == cs[h][ti]) {
	    if (ti < seqv.size()) { ti++; }
	    else { break; }
	  }
	  if (ti < seqv.size()) {
	    if ((cs[h][0] == seqv[i]) && (cs[h][1] == seqv[ti])) {
	      seqv[i] = cs[h][2];
	      seqv[ti] = ' ';
	      i = ti;
	      is_find = true;
	    }
	    else if ((cs[h][1] == seqv[i]) && (cs[h][0] == seqv[ti])) {
	      seqv[i] = cs[h][2];
	      seqv[ti] = ' ';
	      i = ti;
	      is_find = true;
	    }
	    else {
	    }
	  }
	  else {
	  }
	}
	else {
	}
	if (is_find) { break; }
      }
    }
    */
    
    /*
    for (i = 0; i < seqv.size(); i++) {
      cout << seqv[i] << ":";
      }
    */
    //cout << endl;


    /*

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
    for (i = 0; i < c.size(); i++) {
      cout << c[i] << "::";
      cout << n[i] << "::";
    }
    cout << endl;
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
    */

    /*

    */

  }
}
// END CUT HERE

