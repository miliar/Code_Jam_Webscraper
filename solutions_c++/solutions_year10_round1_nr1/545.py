#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef long long ll;


#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-8)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}

char matf[100][100];
char mats[100][100];
char mat[100][100];
bool vis[100][100];

int n,k;

void print(char m[100][100]) {
  cout << "--" << endl;

  FOR(i,n) {
    cout << m[i] << endl;
  }
  cout << "--" << endl;

}

#define OK(y,x) (y >= 0 && y < n && x >= 0 && x < n)

int dx[] = { 0, 1, -1, 1};
int dy[] = { -1, 0, -1, -1};

bool check(int y, int x, char c) {
  FOR(d,4) {
    int i = 0;
    while(i < k) {
      int yy = y + i*dy[d];
      int xx = x + i*dx[d];
      if (!OK(yy,xx) || mat[yy][xx] != c) break;
      i++;
    }
    if (i == k) return true;
  }
  return false;
}


int main() {
  int ncases;
  scanf("%d",&ncases);
  for (int kk = 1; kk <= ncases; kk++) {
    printf("Case #%d: ",kk);
    scanf("%d %d",&n,&k);
    memset(matf,0,sizeof(matf));
    memset(mats,0,sizeof(matf));
    memset(mat,0,sizeof(matf));
    FOR(i,n) {
      cin >> matf[i];
    }
    //print(matf);
    FOR(i,n) {
      FOR(j,n) {
        mats[j][n-i-1] = matf[i][j];
      }
    }
    //print(mats);
    FOR(j,n) {
      int k = n-1;
      for (int i = n-1; i >= 0; i--) {
        mat[i][j] = '.';
        if (mats[i][j] != '.') {
          mat[k--][j] = mats[i][j];
        }
      }
    }
    bool r = false;
    bool b = false;
    FOR(i,n) {
      FOR(j,n) {
        if (mat[i][j] == 'R') {
          r |= check(i,j,'R');
        }
        if (mat[i][j] == 'B') {
          b |= check(i,j,'B');
        }
      }
    }
    if (r && b) cout << "Both" << endl;
    else if (r) cout << "Red" << endl;
    else if (b) cout << "Blue" << endl;
    else cout << "Neither" << endl;
  }  
  return 0;
}
