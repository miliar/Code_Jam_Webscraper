#include <iostream>
#include <complex>
using namespace std;

typedef complex<int> point;

int main() {
  int C;
  cin >> C;
  for (int casenum=1; casenum<=C; casenum++) {
    int N, M, A;
    cin >> N >> M >> A;
    
    cout << "Case #" << casenum << ": ";

    bool found = false;
    for (int x1=0; (x1<=N) && !found; x1++) {
      for (int y2=0; (y2<=M) && !found; y2++) {
	for (int x3=0; (x3<=N) && !found; x3++) {
	  for (int y3=0; (y3<=M) && !found; y3++) {
	    
	    point p1(x1, 0);
	    point p2(0, y2);
	    point p3(x3, y3);

	    point a = p2-p1;
	    point b = p3-p1;

	    int area = abs(imag(conj(a)*b));
	    //cout << area << " " << A << endl;
	    if (area == A) {
	      cout << x1 << " 0 0 " << y2 << " " << x3 << " " << y3 << endl;
	      found = true;
	    }
	  }
	}
      }
    }

    if (!found) {
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
