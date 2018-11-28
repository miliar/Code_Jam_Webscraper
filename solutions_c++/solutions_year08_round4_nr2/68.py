#include<iostream>
#include<string.h>

using namespace std;

int n,m,a;

int cross(int x0, int y0, int x1, int y1)
{
  return x0*y1-x1*y0;
}

int solve()
{
  int x0,y0,x1,y1;

  cin >> n >> m >> a;

  for (x0=0; x0<=n; x0++)
    for (y0=0; y0<=m; y0++)
      for (x1=0; x1<=n; x1++)
	for (y1=0; y1<=m; y1++)
	  if (cross(x0, y0, x1, y1)==a) {
	    cout << 0 << " " << 0 << " " << x0 << " " << y0 << " " << x1 << " " << y1 << endl;
	    return 0;
	  }

  cout << "IMPOSSIBLE" << endl;

  return 0;
}

main()
{
  int t, c=0;
  cin >> t;
  while (t--) {
    cout << "Case #" << ++c << ": ";
    solve();
  }
  return 0;
}
