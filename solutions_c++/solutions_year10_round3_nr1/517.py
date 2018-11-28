#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int check(pair<int, int> &p, vector< pair <int, int> > &v) {
  int cnt = 0;
  for (int i=0; i<v.size(); i++) {
    pair <int, int> q;
    q = v[i];
    //cout << p.first << ", " << p.second << "  " << q.first << ", " << q.second << endl;
    int cross = (p.first - q.first) * (p.second - q.second);
    if (cross <0) cnt++;
    else {
      
    }
  }
  return cnt;
}

int problem(void) {
  int n;
  cin >> n;
  vector<pair<int, int> > v;
  for (int i=0; i<n; i++) {
    int aa, bb;
    cin >> aa >> bb;
    v.push_back(pair<int, int>(aa, bb));
  }
  
  vector<pair <int, int> > vv;
  vv.push_back(v[0]);
  
  int sum = 0;
  for (int i=1; i<n; i++) {
    pair<int, int> p;
    p = v[i];
    
    int cross_cnt = check(p, vv);
    if (cross_cnt >= 1) {
      vv.push_back(p);
      sum += cross_cnt;
    }
    
  }
  return sum;
}

int main(void) {
  int n;
  cin >> n;
  
  for (int i=0; i<n; i++) {
    //int m;
    //cin >> m;
    int r = problem();
    cout << "Case #" << (i+1) << ": " << r << endl;
  }
  return 0;
}