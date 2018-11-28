#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

#define INF 100000000

int main()
{
  int T; cin >> T;

  for(int t = 1; t <= T; ++t)
  {
    vector<string> board(4);
    for(int i = 0; i < 4; ++i)
    {
      cin >> board[i];
      //cout << board[i] << endl;
    }
    //check if finished or not
    bool xwon = false, owon = false;
    for(int i = 0; i < 4; ++i)
    {
      bool xwins = true;
      for(int j = 0; j < 4; ++j)
      {
        if (board[i][j] != 'X' && board[i][j] != 'T') xwins = false;
      }
      if (xwins) xwon = true;
    }
    //cout << xwon << endl;
    for(int i = 0; i < 4; ++i)
    {
      bool xwins = true;
      for(int j = 0; j < 4; ++j)
      {
        if (board[j][i] != 'X' && board[j][i] != 'T') xwins = false;
      }
      if (xwins) xwon = true;
    }
    //cout << xwon << endl;
    bool xwins = true;
    for(int i = 0; i < 4; ++i)
    {
      if (board[i][i] != 'X' && board[i][i] != 'T') xwins = false;
    }
    if (xwins) xwon = true;
    //cout << xwon << endl;
    xwins = true;
    for(int i = 0; i < 4; ++i)
    {
      if (board[3-i][i] != 'X' && board[3-i][i] != 'T') xwins = false;
    }
    if (xwins) xwon = true;
    //cout << xwon << endl;

    for(int i = 0; i < 4; ++i)
    {
      bool owins = true;
      for(int j = 0; j < 4; ++j)
      {
        if (board[i][j] != 'O' && board[i][j] != 'T') owins = false;
      }
      if (owins) owon = true;
    }
    for(int i = 0; i < 4; ++i)
    {
      bool owins = true;
      for(int j = 0; j < 4; ++j)
      {
        if (board[j][i] != 'O' && board[j][i] != 'T') owins = false;
      }
      if (owins) owon = true;
    }
    bool owins = true;
    for(int i = 0; i < 4; ++i)
    {
      if (board[i][i] != 'O' && board[i][i] != 'T') owins = false;
    }
    if (owins) owon = true;
    owins = true;
    for(int i = 0; i < 4; ++i)
    {
      if (board[3-i][i] != 'O' && board[3-i][i] != 'T') owins = false;
    }
    if (owins) owon = true;

    printf("Case #%d: ", t);
    if (xwon)
    {
      printf("X won");
    }
    else if (owon)
    {
      printf("O won");
    }
    else
    {
      bool finished = true;
      for(int i = 0; i < 4; ++i)
      {
        for(int j = 0; j < 4; ++j)
        {
          if (board[i][j] == '.')
            finished = false;
        }
      }
      if (!finished)
      {
        printf("Game has not completed");
      }
      else
      {
        printf("Draw");
      }
    }
    printf("\n");
  }
}

