#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int k;
string data[250];
string datar[250];

bool cmp(const string& a, const string& b) {
  for (int i = 0; i < k; i++)
    if (a[i] != ' ' && b[i] != ' ')
      if (a[i] != b[i])
        return false;
  return true;
}

vector<int> rrr;

int foo() {
  for (int R = k / 2; R < k;  R++) {
    bool ok = true;

    for (int i = R + 1; i < k && ok; i++) {
      int _i = R - (i - R);
      ok = cmp(data[i], data[_i]);
    }

    if (ok)
      rrr.push_back(R);
  }
}

void rot() {
  for (int i = 0; i < k; i++)
    datar[i].resize(k, ' ');

  for (int i = 0; i < k; i++)
    for (int j = 0; j < k; j++)
      datar[i][j] = data[j][i];

  for (int i = 0; i < k; i++)
    data[i] = datar[i];
}

void flip() {
  for (int i = 0; i < k / 2; i++)
    swap(data[i], data[k - 1 - i]);
}

int cnt(int i) {
  int v = (i + 1) / 2;
  return v * v;
}

int res(int x, int y) {
  int cur = cnt(k);

  int size = 0;
  for (int i = 0; i < k; i++) 
    for (int j = 0; j < k; j++)
      if (data[i][j] != ' ') {
        int _x = abs(i - x), _y = abs(j - y);
        size = max(size, _x + _y);
      }

  return cnt(2 * size + 1) - cur;
}


int res() {

  rrr.clear();
  foo();
  flip();
  foo();
  flip();

  vector<int> x1 = rrr;
  rrr.clear();

  rot();
  foo();
  flip();
  foo();

  int ret = 100500;
  for (int i = 0; i < x1.size(); i++)
    for (int j = 0; j < rrr.size(); j++)
      ret = min(ret, res(x1[i], rrr[j]));

  return ret;
}

int main() {
  int _t; cin >> _t;
  for (int _tt = 1; _tt <= _t; _tt++) {
    cout << "Case #" << _tt << ": ";
    cin >> k;
    k = 2 * k - 1;

    string s;
    getline(cin, s);

    for (int i = 0; i < k; i++) {
      getline(cin, s);
      s.resize(k, ' ');
      data[i] = s;
    }
    
    cout << res() << endl;

  }

  return 0;
}
