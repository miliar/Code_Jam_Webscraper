#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

long long n, k, val;

int vec[4][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  int n, k;
  FOR (test, tests){
    cin >> n >> k;
    vector<string> board;
    board.clear();
    string s;
    FOR (i, n){
      cin >> s;
      board.pb(s);
    }
    
    vector<string> nboard;
    nboard.clear();
    
    FOR (i, n){
      string ss = "";
      for (int j = n - 1; j > -1; j--)
        if (board[i][j] != '.')
          ss += string() + board[i][j];
      FOR (j, n - ss.sz)
        ss += ".";
      nboard.pb(ss);
    }
    
    int flag = 0;
    FOR (i, n)
      FOR (j, n)
        FOR (m, 4)
          FOR (p, 2){
            if (flag & (1 << p))
              continue;
            int cnt = 0;
            char ch = 'B';
            if (!p)
              ch = 'R';
            FOR (kk, k){
              int ni = i + kk * vec[m][0];
              int nj = j + kk * vec[m][1];
              if (ni < 0 || nj < 0 || ni >= n || nj >= n || 
                nboard[ni][nj] != ch)
                break;
              cnt++;
            }
            
            if (cnt == k)
              flag |= (1 << p);
          }
    
    cout << "Case #" << (test + 1) << ": ";
    string ret;
    if (!flag)
      ret = "Neither";
    else if (flag == 1)
      ret = "Red";
    else if (flag == 2)
      ret = "Blue";
    else
      ret = "Both";
    cout << ret << "\n";    
  }
  return 0;
}
