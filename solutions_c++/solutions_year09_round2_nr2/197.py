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

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define DBG(x) cout << #x << " = " << x << endl

typedef pair<int,int> ii;
typedef pair<ii,int> iii;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector< ii > vii;

#define DEBUG

int main()
{
  #ifdef DEBUG
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
  #endif
  
  int T;
  cin >> T;
  string s;
  getline(cin,s);
  for (int test = 1;test <= T;++test) {
    getline(cin,s);
    vector< char > a(s.size());
    for (int i = 0;i < s.size();++i) {
      a[i] = s[i];
    }
    
    cout << "Case #" << test << ": ";
    
    if (!next_permutation(a.begin(),a.end())) {
      sort(ALL(a));
      int mn = 0;
      char val = '9';
      for (int i = 0;i < a.size();++i) {
        if (a[i] > '0' && a[i] <= val) {
          val = a[i];
          mn = i;
        }
      }
      
      cout << a[mn] << '0';
      a.erase( a.begin() + mn ); 
      for (int i = 0;i < a.size();++i) {
        cout << a[i];
      }
    } else {
      for (int i = 0;i < a.size();++i) {
        cout << a[i];
      }
    }
    cout << endl;
  }
  
  #ifdef DEBUG
    fclose(stdin);
    fclose(stdout);
  #endif
  return 0;
}
