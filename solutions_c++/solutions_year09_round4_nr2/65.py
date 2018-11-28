#include <iostream>
using namespace std;


int DP[50][50][50][50];
char board[50][50];
int R, C, F;

void update(int& ret, int val)
{
     if (ret == -1 || ret > val) ret = val;
}

int dfs(int i, int j, int r1, int r2)
{
    if (r2 == -1) r1++, r2++;
    
    if (i == R-1) return 0;
    
    int &ret = DP[i][j][r1][r2];
    if (ret != -1) return ret;
    
    
    int left = j, right = j;
    while (left > 0 && ((board[i][left-1] == '.' || (left-1 >= r1 && left-1 <= r2)) && board[i+1][left-1] == '#')) left--;
    while (right < C-1 && ((board[i][right+1] == '.' || (right+1 >= r1 && right+1 <= r2)) && board[i+1][right+1] == '#')) right++;
    
    
    //cout << i << " " << j << " " << r1 << " " << r2 << endl;
    if (left > 0 && (board[i+1][left-1] == '.' && (board[i][left-1] == '.' || (left-1 >= r1 && left-1<=r2))))
    {
             for (int i2 = i + 1; i2 < R && i2 - i <= F; i2++) if (i2 == R-1 || board[i2+1][left-1] == '#') 
             { 
                 int t = dfs(i2, left-1, 0, -1); 
                 if (t != -2) update(ret, t);
                 break; 
             }
    }
    if (right < C-1 && (board[i+1][right+1]=='.' && (board[i][right+1] == '.' || (right+1 >= r1 && right+1<=r2))))
    {
             for (int i2 = i + 1; i2 < R && i2 - i <= F; i2++) if (i2 == R-1 || board[i2+1][right+1] == '#') 
             { 
                 int t = dfs(i2, right+1, 0, -1); 
                 if (t != -2) update(ret, t);
                 break; 
             }
    }
   //  if (i == 2 && j == 0 && r1 == 1 && r2 == 0)
   //  cout << ret << endl;
    //dig to left
    for (int j1 = left; j1 <= right-1; j1++)
     for (int j2 = j1; j2 <= right-1; j2++)
     {
              if (i+1 == R-1 || board[i+2][j2] == '#')
              {
                      int t =  dfs(i+1, j2, j1, j2);
                      if (t != -2) update(ret, t + j2 - j1 + 1);
              }
              else for (int i2 = i+2; i2 < R && i2 - i <= F; i2++) if (i2 == R-1 || board[i2+1][j2] == '#')
              { 
                   int t = dfs(i2, j2, 0, -1);
                   if (t != -2) update(ret, t + j2 - j1 + 1);
                   break;
              }
     }
    
    //dig to right
    for (int j1 = left+1; j1 <= right; j1++)
     for (int j2 = j1; j2 <= right; j2++)
     {
             //if (i == 1 && j == 3 && r1 == 3 && r2 == 4)
             // cout << j1 << " " << j2 << endl;
              
              if (i+1 == R-1 || board[i+2][j1] == '#') 
              {
                      int t = dfs(i+1, j1, j1, j2);
                      if (t != -2) update(ret, t + j2 - j1 + 1);
              }
              else for (int i2 = i+2; i2 < R && i2 - i <= F; i2++) if (i2 == R-1 || board[i2+1][j1] == '#')
              {
                   int t = dfs(i2, j1, 0, -1);
                   if (t != -2) update(ret, t + j2 - j1 + 1);
                   break;
              }
     }
    //if (i == 5 && ret+(r2-r1+1) == 15) cout << j << " " << r1 << " " << r2 << endl;
    //if (i == 5 && j == 0 && r2 == 1 && r2 == 0) cout << ret << endl;
//     cout << ret << endl;
    if (ret == -1) ret = -2;
    return ret;
    
}

void solve()
{
    cin >> R >> C >> F;
    memset(DP, -1, sizeof(DP));
    
    for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) cin >> board[i][j];
    
    int t = dfs(0, 0, 0, -1);
    if (t == -2) cout << "No" << endl;
    else cout << "Yes " << t << endl;
    
}
int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
