#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for(int ii=0;ii<t;ii++) {
    int n, m, a;
    cin >> n >> m >> a;
    int x2, y2, x3, y3;
    bool imp = true;
    for(int i=0;i<=n;i++) {
      for(int j=0;j<=m;j++) {
	for(int k=0;k<=n;k++) {
	  for(int l=0;l<=m;l++) {
	    if(abs(i*l-k*j) == a) {
	      x2 = i, y2 = j;
	      x3 = k, y3 = l;
	      imp = false;
	      goto end;
	    }
	  }
	}
      }
    }
  end:

    if(imp)
      cout << "Case #" << ii+1 << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << ii+1 << ": 0 0 " << x2 << ' ' << y2 << ' ' << x3 <<' ' << y3 << ' ' << endl;
  }

  return 0;
}
