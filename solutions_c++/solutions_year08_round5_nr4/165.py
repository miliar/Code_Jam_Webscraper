#include <iostream>
#include <string>
#include <fstream>

using namespace std;
int c[105][105];
int h, w, r;
int a[105][105];

ofstream out("d.out");

int main()
{
  int i, j, k;
  int t; cin >> t;
  for (int lp=1; lp<=t; lp++)
    {
      cin >> h >> w >> r;
      memset(c, 0, sizeof(c));
      memset(a, 0, sizeof(a));
      for (i=0; i<r; i++)
	{
	  cin >> j >> k;
	  a[j][k] = 1;
	}
      c[h][w] = 1;
      for (i=h; i>=1; i--)
	for (j=w; j>=1; j--)
	  {
	    if (a[i+1][j+2] == 0) c[i][j] = (c[i][j]+c[i+1][j+2]) % 10007;
	    if (a[i+2][j+1] == 0) c[i][j] = (c[i][j]+c[i+2][j+1]) % 10007;
	  }
      c[1][1] = c[1][1] % 10007;
      out << "Case #" << lp << ": " << c[1][1] << endl;
    }
  out.close();
  return 0;
}
