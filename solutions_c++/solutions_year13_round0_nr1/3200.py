#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define foreach(i,x) for (__typeof(x.begin()) i = x.begin();i!=x.end();++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int maxn = (int)1e5+9;
const int inf = (int)1e9+7;

int main(){
  #ifdef LOCAL
  freopen("err","w",stderr);
  #endif
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; tc++) {
    char a[4][4];
    const int n = 4;
    bool emp = 0;
    string winner = "";
    for (int i=0;i<n;++i)
      for (int j=0;j<n;++j){
        cin >> a[i][j];
        if (a[i][j]=='.')
          emp = true;
      }
    for (int i=0;i<n;++i){
      bool fX = 0, fO = 0, e = false;
      for (int j=0;j<n;++j) {
        if (a[i][j] == 'X')
          fX = true;
        if (a[i][j] == 'O')
          fO = true;
        if (a[i][j] == '.')
          e = true;
      }
      if (fX && !fO && !e)
        winner = "X"; else
      if (fO && !fX && !e)
        winner = "O";
    }

    for (int j=0;j<n;++j){
      bool fX = 0, fO = 0, e = false;
      for (int i=0;i<n;++i) {
        if (a[i][j] == 'X')
          fX = true;
        if (a[i][j] == 'O')
          fO = true;
        if (a[i][j] == '.')
          e = true;
      }
      if (fX && !fO && !e)
        winner = "X"; else
      if (fO && !fX && !e)
        winner = "O";
    }

    bool fX = 0, fO = 0, e = 0;
    for (int i=0;i<n;++i){
      if (a[i][i] == 'X')
        fX = true;
      if (a[i][i] == 'O')
        fO = true;
      if (a[i][i] == '.')
        e = true;
    }

    if (fX && !fO && !e)
      winner = "X"; else
    if (fO && !fX && !e)
      winner = "O";

    fX = 0, fO = 0, e = 0;
    for (int i=0;i<n;++i){
      int j = n - 1 - i;
      if (a[i][j] == 'X')
        fX = true;
      if (a[i][j] == 'O')
        fO = true;
      if (a[i][j] == '.')
        e = true;
    }

    if (fX && !fO && !e)
      winner = "X"; else
    if (fO && !fX && !e)
      winner = "O";


    if (winner != "")
      winner += " won";
    if (winner == "" && !emp)
      winner = "Draw";
    else
      if (winner == "" && emp)
        winner = "Game has not completed";
    cout << "Case #" << tc << ": " << winner << "\n";
  }
	return 0;
}

