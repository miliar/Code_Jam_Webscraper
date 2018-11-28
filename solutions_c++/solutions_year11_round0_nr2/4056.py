#include <iostream>
#include <map>
#include <algorithm>
#include <map>
#include <set>
#include <deque>

using namespace std;

#define hash(x, y) x+(y<<8)

int T, n, z, d, c;
char k,l,m;
map<char, char> alp;
map<char, int> cnt;
map<int, char> trans;
set<int> dest;
deque<char> result;

static bool checktrans() {
  l = result.back();
  m = k;
  if (l > m) swap(l, m);
  if (trans.find(hash(l,m)) != trans.end()) return true;
  else return false;
}

static bool checkdest2() {
  m = k;
  if (l > m) swap(l, m);
  if (dest.find(hash(l,m)) != dest.end()) return true;
  else return false;
}

static bool checkdest() {
  for (map<char, int>::iterator it = cnt.begin(); it != cnt.end(); it++) {
    if ((*it).second > 0) {
      l = (*it).first;
      if (checkdest2()) return true;
    }
  }
  return false;
}

void inc(char c) {
  if (cnt.find(c) != cnt.end())
    cnt[c]++;
  else
    cnt[c] = 1;
}

void dec(char c) {
  cnt[c]--;
}

int main() {

  cin >> T;
  for (int num = 1; num <= T; num++) {
    cout <<"Case #"<< num<< ": [";
    z = 8;
    alp['Q'] = 0;
    alp['W'] = 1;
    alp['E'] = 2;
    alp['R'] = 3;
    alp['A'] = 4;
    alp['S'] = 5;
    alp['D'] = 6;
    alp['F'] = 7;
    
    cin >> c;
    for (int i = 0; i < c; i++) {
      cin >>k>> l>>m;
      if (k > l) swap(k, l);
      trans[hash(k, l)] = m;
    }
    cin>>d;
    for (int i = 0; i < d; i++) {
      cin>>k>>l;
      if (k > l) swap(k, l);
      dest.insert(hash(k, l));
    }

    cin>>n;
    for (int i = 0; i < n; i++) {
      cin>>k;
      if (result.empty()) {
        inc(k);
        result.push_back(k);
      } else {
        if (checktrans()) {
          l = result.back();
          result.pop_back();
          dec(k);
          dec(l);
          if (k > l) swap(k, l);
          inc(trans[(hash(k, l))]);
          result.push_back(trans[hash(k, l)]);
        } else if (checkdest()) {
          result.clear();
          cnt.clear();
        } else {
          inc(k);
          result.push_back(k);
        }
      }
    }

    while (!result.empty()) {
      cout << result.front();
      result.pop_front();
      if (!result.empty()) cout <<", ";
    }

    alp.clear();
    cnt.clear();
    trans.clear();
    dest.clear();
    result.clear();
    cout <<"]\n";
  }
}
