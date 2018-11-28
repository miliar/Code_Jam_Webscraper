#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in("crop.in");
ofstream out("crop.out");

int main() {
  int N;
  in >> N;

  for (int casenum = 1; casenum <= N; casenum++) {
    long long n,a,b,c,d,x0,y0,m,x,y;
    in >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
    
    x = x0;
    y = y0;
    
    // v[j][k] = number of trees with x == j mod 3, y == k mod 3
    vector< vector<long long> > v(3, vector<long long>(3,0));

    for (int i=0; i<n; i++) {
      v[x%3][y%3]++;     
      x = (a*x + b) % m;
      y = (c*y + d) % m;
    }
    
    long long totalsum = 0;

    //count triangles on trees distinct mod 3
    for (int t0x=0; t0x < 3; t0x++) {
      for (int t0y=0; t0y < 3; t0y++) {
	for (int t1x=0; t1x < 3; t1x++) {
	  for (int t1y=0; t1y < 3; t1y++) {
	    int t2x = (6 - t0x - t1x)%3;
	    int t2y = (6 - t0y - t1y)%3;
	    if ((t1x == t0x && t1y == t0y) || (t2x == t0x && t2y == t0y) ||
		(t2x == t1x && t2y == t1y)) {
	      continue;
	    }
	    totalsum +=
	      v[t0x][t0y]*v[t1x][t1y]*v[t2x][t2y];
	  }
	}
      }
    }

    for (int tx=0; tx < 3; tx++) {
      for (int ty=0; ty < 3; ty++) {
	if (v[tx][ty] >= 3) {
	  totalsum +=
	    v[tx][ty] * (v[tx][ty] - 1) * (v[tx][ty] - 2);
	}
      }
    }

    // up to now, totalsum counted the order of vertices
    totalsum /= 6;

    out << "Case #" << casenum << ": " << totalsum << endl;
  }
  return 0;
}
