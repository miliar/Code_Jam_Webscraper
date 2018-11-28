#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>
using namespace std;

void checkForCombine (vector<char>& vc, map<string, char> m)
{
  long int sz = vc.size();
  if(sz <= 1)
    return;
  string t1 (1, vc[sz-1]);
  string t2 (1, vc[sz-2]);
  string ky = t1 + t2;
  sort (ky.begin(), ky.end());
  map<string, char>::const_iterator ix = m.find(ky);
  if(ix != m.end()) {
    vc[sz-2] = ix->second;
    vc.erase(vc.begin()+sz-1);
  }
}

void checkForOppose (vector<char>& vc, map<string, char> m)
{
  long int sz = vc.size();
  if(sz <= 1)
    return;
  string t1 (1, vc[sz-1]);
  for(long int a = 0; a < sz-1; ++a) {
    string t2 (1, vc[a]);
    string ky = t1 + t2;
    sort (ky.begin(), ky.end());
    map<string, char>::const_iterator ix = m.find(ky);
    if(ix != m.end()) {
      vc.clear();
    }
  }
}

int main()
{
  ifstream f("in", ios::in);
  if(!f.is_open()) {
    cout << "SCREAM: Invalid input file 'in'\n";
    return 0;
  }
  long int T;
  f >> T;
  for(long long i = 1; i <= T; ++i) {
    long int C;
    long int D;
    long int N;
    map<string, char> combine;
    map<string, char> oppose;
    vector<char> v;
    f >> C;
    for(long int x = 0; x < C; ++x) {
      string s;
      f >> s;
      char ch = s[2];
      string sx = s.substr(0, 2);
      sort(sx.begin(), sx.end());
      combine [sx] = ch;
    }
    f >> D;
    for(long int y = 0; y < D; ++y) {
      string s;
      f >> s;
      char ch = s[2];
      string sx = s.substr(0, 2);
      sort(sx.begin(), sx.end());
      oppose [sx] = ch;
    }
    f >> N;
    // for(long int z = 0; z < N; ++z) {
      string s;
      f >> s;
      assert (s.size() == N);
      for(long int w = 0; w < s.size(); ++w) {
        v.push_back(s[w]);
        checkForCombine(v, combine);
        checkForOppose(v, oppose);
      }
    // }
    if(v.size() == 0) 
      cout << "Case #" << i << ": []" << endl;
    else { 
      cout << "Case #" << i << ": [";
      for(long int a = 0; a < v.size()-1; ++a)
        cout << v[a] << ", ";
      cout << v[v.size()-1] << "]" << endl;
    }
  }
  f.close();
}
