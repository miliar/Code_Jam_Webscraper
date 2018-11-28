#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

double interp(double x, double X, double y1, double y2) {
  return y1 * (X-x)/X + y2 * x/X;
}

double area(double x, double y1, double y2) {
  return x * (y1+y2) / 2;
}

int main(void)
{
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    int W, num_lower, num_upper, pieces;
    cin >> W >> num_lower >> num_upper >> pieces;
    vector <int> lower_x(num_lower), lower_y(num_lower),
      upper_x(num_upper), upper_y(num_upper);
    set <int> x_set;
    for (int i = 0; i < num_lower; i++) {
      cin >> lower_x[i] >> lower_y[i];
      x_set.insert(lower_x[i]);
    }
    for (int i = 0; i < num_upper; i++) {
      cin >> upper_x[i] >> upper_y[i];
      x_set.insert(upper_x[i]);
    }
    int num_all = x_set.size();
    vector <int> x(x_set.begin(), x_set.end());
    vector <double> y(num_all);
    for (int i = 0; i < num_all; i++) {
      for (int j = 0; j < num_lower; j++)
	if (lower_x[j] == x[i])
	  for (int k = 0; k+1 < num_upper; k++)
	    if (upper_x[k] <= x[i] && x[i] <= upper_x[k+1])
	      y[i] = interp(x[i]-upper_x[k], upper_x[k+1]-upper_x[k],
			    upper_y[k]-lower_y[j], upper_y[k+1]-lower_y[j]);
      for (int k = 0; k < num_upper; k++)
	if (upper_x[k] == x[i])
	  for (int j = 0; j+1 < num_lower; j++)
	    if (lower_x[j] <= x[i] && x[i] <= lower_x[j+1])
	      y[i] = interp(x[i]-lower_x[j], lower_x[j+1]-lower_x[j],
			    upper_y[k]-lower_y[j], upper_y[k]-lower_y[j+1]);
      //cerr << x[i] << " " << y[i] << endl;
    }


    printf("Case #%d:\n", test);
    vector <double> cum_area(num_all);
    for (int i = 1; i < num_all; i++) {
      cum_area[i] = cum_area[i-1] + area(x[i]-x[i-1], y[i-1], y[i]);
      //cerr << cum_area[i] << endl;
    }
    for (int p = 1; p < pieces; p++) {
      double want_area = cum_area[num_all-1] * p / pieces;
      for (int i = 0; i+1 < num_all; i++)
	if (cum_area[i] <= want_area && want_area <= cum_area[i+1]) {
	  want_area -= cum_area[i];
	  //cerr << "want_area: " << want_area << endl;
	  double lo = 0, hi = x[i+1]-x[i], X = hi, mid = (lo+hi)/2;
	  double y1 = y[i], y2 = y[i+1];
	  //cerr << "hi: "<< hi << " y1: " << y1 << " y2: " << y2 << endl;
	  for (int iters = 0; iters < 100; iters++) {
	    double y = interp(mid, X, y1, y2);
	    if (area(mid, y1, y) < want_area)
	      lo = mid;
	    else
	      hi = mid;
	    mid = (lo+hi)/2;
	  }
	  printf("%.6lf\n", x[i] + mid);
	  break;
	}
    }
  }
}
