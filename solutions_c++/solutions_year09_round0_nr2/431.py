#include <iostream>
#include <iterator>
#include <algorithm>
#include <cstring>
using namespace std;
#define valid(x, y) (x)>=0 && (x)<h && (y)>=0 && (y)<w
const int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
const int maxn = 110;
int mat[maxn][maxn];
int h, w;
int px[maxn*maxn], py[maxn*maxn], l;
bool vi[maxn][maxn];
int x, y;
char color;
char lab[maxn][maxn];
void init()
{
     cin >> h >> w;
     for (int i=0; i<h; i++)
          for (int j=0; j<w; j++)
               cin >> mat[i][j];
     memset(vi, false, sizeof(vi));
     memset(lab, 0, sizeof(lab));
     color = 'a';
}
void calc()
{
     for (int i=0; i<h; i++)
     {
          for (int j=0; j<w; j++)
          {
               if (!vi[i][j])
               {
                    x = i, y = j;
                    l = 0;
                    while (valid(x, y) && !vi[x][y])
                    {
                         px[l] = x, py[l] = y, l++;
                         vi[x][y] = true;
                         int tmp = mat[x][y], ai;
                         for (int k=0; k<4; k++)
                         {
                              if (valid(x+d[k][0], y+d[k][1]) && mat[x+d[k][0]][y+d[k][1]] < tmp)
                              {
                                   tmp = mat[x+d[k][0]][y+d[k][1]];
                                   ai = k;
                              }
                         }
                         if (tmp != mat[x][y])
                              x += d[ai][0], y += d[ai][1];
                    }
                    if (valid(x, y) && lab[x][y] != 0)
                    {
                         for (int k=0; k<l; k++)
                              lab[px[k]][py[k]] = lab[x][y];
                    }
                    else
                    {
                         for (int k=0; k<l; k++)
                              lab[px[k]][py[k]] = color;
                         color++;
                    }
               }
          }
     }
}
void print(int t)
{
     cout << "Case #" << t << ":" << endl;
     for (int i=0; i<h; i++)
     {
          copy(lab[i], lab[i]+w, ostream_iterator<char>(cout, " "));
          cout << endl;
     }
}
int main()
{
     freopen("B-large.in", "r", stdin);
     freopen("B.out", "w", stdout);
     int t;
     cin >> t;
     for (int i=1; i<=t; i++)
     {
          init();
          calc();
          print(i);
     }
     return 0;
}
