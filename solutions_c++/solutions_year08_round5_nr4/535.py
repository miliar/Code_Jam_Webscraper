#include<iostream>
#include<vector>
#include<sstream>
#include<map>


using namespace std;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  cin >> t;
  int a[101][101];
  for (int tt = 0; tt < t; tt++)
  {
    int H, W, r;
    cin >> H >> W >> r;
    memset(a,0,sizeof(a));
    for (int i = 0; i < r; i++)
    {
      int x,y;
      cin >> x >> y;
      a[x-1][y-1] = -1;
    }
    a[0][0] = 1;
    for (int i = 0; i < H; i++)
      for (int j = 0; j < W; j++)
      if (a[i][j] != -1)
        {
          if (i-2 >= 0 && j-1 >= 0 && a[i-2][j-1] != -1)
            a[i][j] = (a[i][j] + a[i-2][j-1]) % 10007; 
          if (i-1 >= 0 && j-2 >= 0 && a[i-1][j-2] != -1)
            a[i][j] = (a[i][j] + a[i-1][j-2]) % 10007; 
        }


    cout << "Case #" << tt+1 << ": " << a[H-1][W-1] % 10007 << endl;
  }
  return 0;

}