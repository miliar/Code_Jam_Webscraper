#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

/*
int vz;
ld z[1001] = {};
ld avg[1001] = {};
ld logx[1001];
ld logxf[1001];

void loop(int big, int sum, ld ret, ld sumz) {
  if (big >= sum) {
    z[vz] += exp(-ret) * (sumz + avg[sum]);
    return;
  }
  //if (big >= sum) {
  //  big = sum;
  //}
  if (big <= 0) {
    z[vz] += exp(-ret) * sumz;
    return;
  }
  for (int i = big; i > 1; --i) {
    int k = sum - i;
    for (int j = 1; k >= 0; ++j, k -= i) {
      loop(i-1, k, ret + logxf[j] + j * logx[i], sumz + z[i] * j);
    }
  }
  // all 1
  loop(0, 0, ret + logxf[sum], sumz);
}
*/

int main()
{
/*  for (int i = 1; i <= 1000; ++i) {
    logx[i] = log((ld)i);
    logxf[i] = logxf[i-1] + logx[i];
  }

  z[1] = 0;
  for (vz = 2; vz <= 100; ++vz) {
    loop(vz-1, vz, 0.0, 0.0);
    avg[vz] = z[vz];
    ld p = 1 - 1.0/vz;
    z[vz] /= p;
    z[vz] += 1/p;
    avg[vz] += z[vz] / vz;
    cout << z[vz] << endl;
  }
*/
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
          int n;
          fin >> n;
          int ans = 0;
          for (int i = 1; i <= n; ++i) {
            int j;
            fin >> j;
            if (i != j) ans++;
          }
          fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
