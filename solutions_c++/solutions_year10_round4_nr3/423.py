#include <iostream>
using namespace std;

int G[1000][1000];

void solve()
{
     int R;
     cin >> R;
     
     memset(G, 0, sizeof(G));
     
     int minx = 1002, maxx = -1, miny = 1002, maxy = -1;
     for (int i = 0; i < R; i++)
     {
         int x1, y1, x2, y2;
         cin >> x1 >> y1 >> x2 >> y2;
         
         minx = min(minx, x1), maxx = max(maxx, x2);
         miny = min(miny, y1), maxy = max(maxy, y2);
         
         for (int i1 = y1; i1 <= y2; i1++)
          for (int j1 = x1; j1 <= x2; j1++) 
           G[i1][j1] = 1;
     }   
     
     int ans = 0;
     while (1)
     {
           int nminx = 1002, nmaxx = -1, nminy = 1002, nmaxy = -1;
           
           bool flag = 0;
           for (int i = maxy; i >= miny; i--)   
           {
               for (int j = maxx; j >= minx; j--)
                if (G[i][j] == 0)
                {
                     if (G[i-1][j] && G[i][j-1]) 
                     {
                           G[i][j] = 1;
                           nminx = min(nminx, j), nmaxx = max(nmaxx, j);
                           nminy = min(nminy, i), nmaxy = max(nmaxy, i);
                     }
                }
                else
                {
                     flag = 1;
                     if (G[i-1][j] == 0 && G[i][j-1] == 0) G[i][j] = 0;
                     else 
                     {
                           nminx = min(nminx, j), nmaxx = max(nmaxx, j);
                           nminy = min(nminy, i), nmaxy = max(nmaxy, i);
                     }
                }
           }
           
           if (flag == 0) break;
           
           
           ans++;
           minx = nminx, miny = nminy, maxx = nmaxx, maxy = nmaxy;
     }
     
     cout << ans << endl;
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
