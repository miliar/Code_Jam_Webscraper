using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

template <class T> string toStr(const T &x){ stringstream s; s << x; return s.str(); }
template <class T> int toInt(const T &x){ stringstream s; s << x; int r; s >> r; return r; }

#define For(i, a, b) for (int i=(a); i<(b); ++i)
#define foreach(x, v) for (typeof (v).begin() x = (v).begin(); x != (v).end(); ++x)
#define D(x) cout << #x " = " << (x) << endl

int f(vector<int> v){
  if (v.size() == 1) return 0;
  int k = 0;
  while (v[k] != 0) k++;
  int ans = k;
  v.erase(v.begin() + k);
  for (int i=0; i<v.size(); ++i){
    v[i]--;
    if (v[i] < 0) v[i] = 0;
  }
  ans += f(v);
  return ans;
}

void solve(){
  int n;
  cin >> n;
  vector<int> v;
  for (int i=0; i<n; ++i){
    string s;
    cin >> s;
    int x = s.rfind('1');
    if (x < 0) x = 0;
    v.push_back(x);
    //cout << s << endl;
  }
  printf("%d\n", f(v));
}


int main(){
  int Casos;
  cin >> Casos;
  for (int Caso=1; Caso<=Casos; ++Caso){
    printf("Case #%d: ", Caso);
    solve();
  }
  return 0;
}
