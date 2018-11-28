#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cmath>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::sort;

using std::map;

int main() {

  int T;

  cin >> T;
  cin.ignore();

  for (int i=0; i < T; ++i) {
    int N;
    cin >> N;
    cin.ignore();

    long double fly_data[N][6];

    for (int j=0; j < N; ++j) {
      for (int k=0; k < 6; ++k) {
	cin >> fly_data[j][k];
      }
      cin.ignore();
    }

    long double xc, yc, zc, vxc, vyc, vzc;
    xc = yc = zc = vxc = vyc = vzc = 0.0;
    for (int j=0; j < N; ++j) {
      xc += fly_data[j][0];
      yc += fly_data[j][1];
      zc += fly_data[j][2];
      vxc += fly_data[j][3];
      vyc += fly_data[j][4];
      vzc += fly_data[j][5];
    }
    xc = xc / N;
    yc = yc / N;
    zc = zc / N;
    vxc = vxc / N;
    vyc = vyc / N;
    vzc = vzc / N;

    // calculate distance
    // differentiate to find t at minimum distance
    // if such t is negative, take t=0
    long double t_min = 0.0;
    if ( vxc * vxc + vyc * vyc + vzc * vzc != 0 ) {
      t_min = 
	-1.0 * (xc * vxc + yc * vyc + zc * vzc) 
	/ (vxc * vxc + vyc * vyc + vzc * vzc);
    }
    if (t_min < 0.0)
      t_min = 0.0;
    long double d_min 
      = sqrt( (xc + t_min * vxc ) * (xc + t_min * vxc )
	      + (yc + t_min * vyc ) * (yc + t_min * vyc )
	      + (zc + t_min * vzc ) * (zc + t_min * vzc ) );

    cout << "Case #" << i+1 << ": " << d_min << " " << t_min << endl;
  }

  return 0;
}
