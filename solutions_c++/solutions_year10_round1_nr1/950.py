#include <iostream>
#include <vector>
#include <string>
using namespace std;

int T, N, K;
vector<string> board, rboard;

inline bool check(char c, int row, int col, int dr, int dc)
{
  for (int i = 0; i < K; ++i)
  {
    if (rboard[row][col] != c) return false;
    row += dr;
    col += dc;
  }
  return true;
}

inline bool check(char c, int r_min, int r_max, int c_min, int c_max, int dr, int dc)
{
  for (int row = r_min; row <= r_max; ++row)
    for (int col = c_min; col <= c_max; ++col)
      if (check(c, row, col, dr, dc))
        return true;
  return false;
}

inline bool check(char c)
{
  return
    check(c, 0, N-K, 0, N-1, 1, 0) ||
    check(c, 0, N-1, 0, N-K, 0, 1) ||
    check(c, 0, N-K, 0, N-K, 1, 1) ||
    check(c, K-1, N-1, 0, N-K, -1, 1);
}

int main()
{
  freopen("out.txt", "w", stdout);
  cin >> T;
  for (int x = 1; x <= T; ++x)
  {
    cout << "Case #" << x << ": ";
    cin >> N >> K;
    board = vector<string>(N);
    for (int row = 0; row < N; ++row)
      cin >> board[row];
    rboard = board;
    for (int row = 0; row < N; ++row)
      for (int col = 0; col < N; ++col)
        rboard[col][N-1-row] = board[row][col];
    for (int col = 0; col < N; ++col)
    {
      for (int row = N-1; row >= 0; --row)
      if (rboard[row][col] == '.')
      {
        for (int i = row-1; i >= 0; --i)
        if (rboard[i][col] != '.')
        {
          rboard[row][col] = rboard[i][col];
          rboard[i][col] = '.';
          break;
        }
      }
    }
    
    //cout << "--" << endl;
    //for (int row = 0; row < N; ++row)
    //  cout << rboard[row] << endl;
    //cout << "--" << endl;
    
    bool red = check('R');
    bool blue = check('B');
    if (red && blue) cout << "Both";
    else if (red) cout << "Red";
    else if (blue) cout << "Blue";
    else cout << "Neither";
    cout << endl;
  }
  return 0;
}
