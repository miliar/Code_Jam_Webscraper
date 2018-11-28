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

string w = "welcome to code jam";
string s;
int m;
int res = 0;

void go(int i,int j)
{
  if (j == 19) {
    res = (res + 1) % 10000;
  } else {
    for (int k = i;k < m;++k) {
      if (s[k] == w[j]) {
        go(k + 1,j + 1);
      }
    }
  }
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  int n;
  cin >> n;
  getline(cin,s);
  for (int t = 1;t <= n;++t) {
    getline(cin,s);
    res = 0;
    m = s.size();
    go(0,0);
    stringstream ss;
    ss << res;
    cout << "Case #" << t << ": ";
    if (ss.str().size() < 4) {
      cout << string(4 - ss.str().size(),'0');
    }
    cout << ss.str() << endl;
  }
    
  
  
  fclose(stdin);
  fclose(stdout);
  return 0;
}
