#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;


string board[100];
int R, C;

bool can()
{
  
  FOR(i, R) FOR(j, C) 
    if(board[i][j] == '#') {
      if(i >= R - 1 || j >= C - 1) return false;
      if(board[i+1][j] != '#' ||
         board[i+1][j+1] != '#' ||
         board[i][j+1] != '#') return false;
      
      board[i][j] = '/';
      board[i][j+1] = '\\';
      board[i+1][j] = '\\';
      board[i+1][j+1] = '/';      
    }
  return true;
}

int main() 
{

  int tests;
  cin >> tests;

  FOT(t, 1, tests + 1) {

    cin >> R >> C;

    FOR(i, R) cin >> board[i];

    cout << "Case #" << t << ": " << endl;
    if(can()) {
      FOR(i, R) cout << board[i] << endl;
    }
    else {
      cout << "Impossible" << endl;
    }    
  }

  return 0;
}
