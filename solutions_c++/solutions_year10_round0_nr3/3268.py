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

ll ride(vector< ii >& a, int k)
{
  ll s = 0;
  int i = 0;
  while (i < a.size() && (s + a[i].first) <= k) {
    s += a[i++].first;
  }

  reverse(a.begin(),a.begin() + i);
  if (i < a.size()) {
    reverse(a.begin() + i, a.end());
  }
  reverse(a.begin(),a.end());

  return s;
}

ll dummy(vector< ii >& a,ll r,int k)
{
  ll res = 0;
  while (r--) {
    res += ride(a,k);
  }
  return res;
}

int main()
{
  #ifdef DEBUG
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
  #endif

  int T;
  cin >> T;

  for (int test = 1;test <= T;++test) {
    int r,k,n;
    ll res = 0;
    cin >> r >> k >> n;
    vector< ii > a(n);
    for (int i = 0;i < n;++i) {
      cin >> a[i].first;
      a[i].second = i;
    }

    map<int, pair<int, long> > m;
    m[0] = make_pair(0, 0);
    pair<int, long> pred;
    pair<int, long> period;
    int j = 1;
    vii b;
    do {
      res += ride(a,k); 
      if (m.find(a[0].second) != m.end()) {
        map<int, pair<int, long> >::iterator it = m.find(a[0].second);
        period = make_pair(j - it->second.first,res - it->second.second); 
        pred = it->second;
        b = a;
        break;
      } else {
        m[a[0].second].first = j++; 
        m[a[0].second].second = res;
      }
    } while(1);

    if (r <= pred.first) {
      res = dummy(a,r,k);
    } else {
      res = pred.second;
      r -= pred.first;
      res += (r / period.first) * period.second;
      r -= (r / period.first) * period.first;
      res += dummy(b,r,k);
    }

    cout << "Case #" << test << ": " << res << endl;
  }


  #ifdef DEBUG
    fclose(stdin);
    fclose(stdout);
  #endif
  
  return 0;
}
