#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <math.h>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef deque<string> DS;

DS split( string s, string c )
{
  DS ret;
  for (int i=0, n; i <= s.length(); i=n+1 ) {
    n = s.find_first_of( c, i );
    if( n == string::npos ) n = s.length();
    string tmp = s.substr( i, n-i );
    ret.push_back(tmp);
  }
  return ret;
}

int main () {
  int i,j;
  int test, T;

  cin >> T;
  REP (test, T) {
    int n,k;
    cin >> n;
    cin >> k;
    //cout << n << endl;
    //cout << k << endl;
    vector<string> data(n+2);
    data[0] = string(n+2, '.');
    REP (i, n) {
      cin >> data[i+1];
      data[i+1] = "."+data[i+1]+".";
      //cout << i << data[i+1] << endl;
    }
    data[n+1] = string(n+2, '.');

    vector< vector < vector < int > > > count;
    count.resize(n+2);
    REP(i,n+2) {
      count[i].resize(n+2);
      REP(j,n+2) {
        count[i][j].resize(4);
      }
    }
    for (i=1; i<=n; i++) {
        string s = data[i];
        string::size_type loc = string::npos+1;
        while (loc != string::npos) {
          loc = s.find( ".", 0 );
          if( loc != string::npos ) {
            s.erase(loc, 1);
          }
        }
        int l = s.size();
        l = 1+n-l;
        data[i] = string(l, '.') + s + ".";
        //cout << i << ":" << data[i] << endl;
    }

    for (i=1; i<=n; i++) {
      for (j=n; j>=1; j--) {
        char c = data[i][j];
        if (c == '.') {
        } else {
          if (data[i][j+1] == c) {
            count[i][j][0] = count[i][j+1][0]+1;
            count[i][j+1][0] = 1;
          } else {
            count[i][j][0] = 1;
          }
          if (data[i-1][j] == c) {
            count[i][j][1] = count[i-1][j][1]+1;
            count[i-1][j][1] = 1;
          } else {
            count[i][j][1] = 1;
          }
          if (data[i-1][j+1] == c) {
            count[i][j][2] = count[i-1][j+1][2]+1;
            count[i-1][j+1][2] = 1;
          } else {
            count[i][j][2] = 1;
          }
        }
      }
    }

    for (i=n; i>=1; i--) {
      for (j=n; j>=1; j--) {
        char c = data[i][j];
        if (c == '.') {
        } else {
          if (data[i+1][j+1] == c) {
            count[i][j][3] = count[i+1][j+1][3]+1;
            count[i+1][j+1][3] = 1;
          } else {
            count[i][j][3] = 1;
          }
        }
      }
    }
    bool bwin = false;
    bool rwin = false;

    int mm;
    for (i=1; i<=n; i++) {
      for (j=1; j<=n; j++) {
        REP(mm,4) {
          if (k <= count[i][j][mm]) {
            char c = data[i][j];
            if (c == 'R') {
              rwin = true;
            } else if (c == 'B') {
              bwin = true;
            }
          }
        }
      }
    }
    string rs;
    if (rwin && bwin) rs = "Both";
    else if (rwin) rs = "Red";
    else if (bwin) rs = "Blue";
    else rs = "Neither";
    gp(rs);
  }
  return 0;
}

