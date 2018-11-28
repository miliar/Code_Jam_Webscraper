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

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define DBG(x) cout << #x << " = " << x << endl
#define SZ(c) (int)(c).size()

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector< ii > vii;

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  int l, d, n;
  cin >> l >> d >> n;
    
  vector< string > a(d);
  
  for (int i = 0;i < d;++i) {
    cin >> a[i];
  }
  
  for (int t = 1;t <= n;++t) {
    string p;
    cin >> p;
    vector< string > pat(l);
    {
      int i = 0;
      int j = 0;
      while (i < p.size()) {
        if (p[i] == '(') {
          string tmp;
          ++i;
          while (p[i] != ')') {
            tmp += p[i++];
          }
          ++i;
          pat[j++] = tmp;
        } else {
          pat[j++] = string(1,p[i++]);
        }
      }
    }
      
    int res = 0;
    for (int j = 0;j < d;++j) {
      int k;
      for (k = 0;k < l;++k) {
        if (pat[k].find(a[j][k]) == string::npos) {
          break;
        }
      }
      if (k == l) {
        ++res;
      }
    }
    
    cout << "Case #" <<  t << ": " << res << endl;
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
