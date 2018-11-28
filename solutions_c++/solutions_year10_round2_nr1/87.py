// login: 001963
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <map>
#include <set>      
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstdio>
#include <numeric>
#include <limits>
#include <functional>

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define DBG(x) cout << #x << " = " << x << endl


typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ii,int> iii;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector< ii > vii;
typedef vector< vii > vvii;
typedef unsigned int uint;

#define DEBUG



int main()
{
  #ifdef DEBUG
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
  #endif

  int T;
  cin >> T;

  for (int test = 1;test <= T;++test) {
    int n,m;
    cin >> n >> m;

    vector<string> a(n);

    for (int i = 0;i < n;++i) {
      cin >> a[i];
    }

    int res = 0;
    for (int i = 0;i < m;++i) {
      string t;
      cin >> t;
      for (int j = 0;j < t.size();++j) {
        if (t[j] == '/') {
          t[j] = ' ';
        }
      }
      stringstream ss(t);
      vector<string> b;
      string tmp;
      while (ss >> tmp) {
        b.push_back(tmp);
      }
      
      string cur;
      for (int j = 0;j < b.size();++j) {
        cur += string("/") + b[j];
        if (find(ALL(a),cur) == a.end()) {
          a.push_back(cur);
          ++res;
        }
      }
    }

    cout << "Case #" << test << ": " << res << endl;
  }


  #ifdef DEBUG
    fclose(stdin);
    fclose(stdout);
  #endif
  
  return 0;
}
