#include <iostream>
#include <cmath>

using namespace std;

const int maxn=40;

int n;

int r[maxn], x[maxn], y[maxn];

inline double min3(double a, double b, double c) {
  return min(a, min(b, c));
}

inline double dist(int i, int j) {
  return sqrt((x[i]-x[j])*(x[i]-x[j])+
	      (y[i]-y[j])*(y[i]-y[j]));
}

inline double solve2(int i, int j) {
  double tmp = dist(i, j);
  if(tmp + r[j] < r[i]) return r[i];
  else if(tmp + r[i] < r[j]) return r[j];
  else return (tmp + r[i] + r[j]) / 2;
}

int main() {
  int C;
  cin >> C;
  for(int tcase=1;tcase<=C;tcase++){
    cin >> n;
    for(int i=0;i<n;i++)
      cin >> x[i] >> y[i] >> r[i];
    if(n == 1) cout << "Case #" << tcase << ": " << r[0] << '\n';
    else if(n == 2) cout << "Case #" << tcase << ": " << 
		      max(r[0], r[1]) << '\n';
    else if(n == 3) cout << "Case #" << tcase << ": " << 
		      min3(max(double(r[0]), solve2(1, 2)),
			   max(double(r[1]), solve2(0, 2)),
			   max(double(r[2]), solve2(0, 1))) << '\n';
    else cout << "Case #" << tcase << ": " << -1 << '\n';
  }
}
