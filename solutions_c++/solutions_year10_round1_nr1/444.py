#include <iostream>
#include <cstring>
using namespace std;
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define For(i,a,b) for (int i=(a); i<(b); i++)
#define Rep(i,n) For((i),0,(n))
#define Fore(it,x) for (typeof((x).begin()) it=(x).begin(); it!=(x).end(); it++)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define Clear(x,with) memset((x), (with), sizeof((x)))
#define sz size()
typedef long long ll;

const int maxn = 100;
char board[maxn][maxn];
int n, k;
bool red, blue;
const int dir[4][2] = {{1, 0}, {1, 1}, {0, 1}, {-1, 1}};
void init()
{
     red = blue = false;
     cin >> n >> k;
     // for (int i=n-1; i>=0; i--)
     Rep (i, n)
     {
          Clear(board[i], 0);
          Rep (j, n)
          {
               cin >> board[i][j];
          }
     }
}

void calc()
{
     char tmp;
     Rep (i, n)
     {
          int p = n-1;
          for (int j=n-1; j>=0; j--)
          {
               if (board[i][j] != '.')
               {
                    tmp = board[i][j];
                    board[i][j] = '.';
                    board[i][p--] = tmp;
               }
          }
     }
     // Rep (i, n) {Rep(j, n) cout << board[i][j]; cout << endl;}
     bool flag;
     int x, y;
     Rep (i, n)
     {
          Rep (j, n)
          {
               if (board[i][j] == '.') continue;
               Rep (d, 4)
               {
                    flag = true;
                    x = i, y = j;
                    for (int l=0; l<k; l++,x+=dir[d][0],y+=dir[d][1])
                    {

                         if(x < 0 || x >= n || y >= n || y < 0 ||
                            board[x][y] != board[i][j])
                         {
                              flag = false;
                              break;
                         }
                    }
                    if (flag == true)
                    {
                         if (board[i][j] == 'R') red = true;
                         else blue = true;
                    }
               }
          }
     }
}

int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     for (int i=1; i<=t; i++)
     {
          init();
          calc();
          cout << "Case #" << i << ": ";
          if (blue && red)
               cout << "Both" << endl;
          else if (blue)
               cout << "Blue" << endl;
          else if (red)
               cout << "Red" << endl;
          else
               cout << "Neither" << endl;
     }
     return 0;
}
