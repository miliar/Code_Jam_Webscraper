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

int di[] = {-1,0,0,1};
int dj[] = {0,-1,1,0};


int a[200][200];
char label[200][200];
bool v[200][200];
int h,w;
char start = 'a';

char dfs(int i,int j)
{
  if ( label[i][j] == 0 ) {
    int mn_x = -1;
    int mn_y = -1;
    for (int k = 0;k < 4;++k) {
      int x = i + di[k];
      int y = j + dj[k];
      if ( x >= 0 && x < h && y >= 0 && y < w ) {
        if (mn_x == -1 && a[x][y] < a[i][j]) {
          mn_x = x;
          mn_y = y;
        } else if (a[x][y] < a[mn_x][mn_y]) {
          mn_x = x;
          mn_y = y;
        }
      }
    }
    label[i][j] = dfs(mn_x,mn_y);        
  }
  
  return label[i][j];
}

int main()
{
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  
  int test_count;
  cin >> test_count;
  
  for (int test = 1;test <= test_count;++test) {
    cin >> h >> w;
    for (int i = 0;i < h;++i) {
      for (int j = 0;j < w;++j) {
        cin >> a[i][j];
      }
    }
    
    memset(label,0,sizeof(label));
    
    char start = 'a';
    for (int i = 0;i < h;++i) {
      for (int j = 0;j < w;++j) {
        int lower_count = 0;
        for (int k = 0;k < 4;++k) {
          int x = i + di[k];
          int y = j + dj[k];
          if ( x >= 0 && x < h && y >= 0 && y < w ) {
            lower_count += (a[x][y] < a[i][j]);
          }
        }
        if ( lower_count == 0 ) {
          label[i][j] = start++;
        }
      }
    }
    
    for (int i = 0;i < h;++i) {
      for (int j = 0;j < w;++j) {
        if ( label[i][j] == 0 ) {
          dfs(i,j);
        }
      }
    }
    
    string p;
    for (int i = 0;i < h;++i) {
      for (int j = 0;j < w;++j) {
        if (p.find(label[i][j]) == string::npos) {
          p += label[i][j];
        }
      }
    }
    
    map<char,char> m;
    for (int i = 0;i < p.size();++i) {
      m[p[i]] = char('a' + i);
    }
    
    for (int i = 0;i < h;++i) {
      for (int j = 0;j < w;++j) {
        label[i][j] = m[label[i][j]];
      }
    }
    
    cout << "Case #" << test << ":" << endl;
    for (int i = 0;i < h;++i) {
      cout << label[i][0];
      for (int j = 1;j < w;++j) {
        cout << ' ' << label[i][j];
      }
      cout << endl;
    }
  }
  
  fclose(stdin);
  fclose(stdout);
  return 0;
}
