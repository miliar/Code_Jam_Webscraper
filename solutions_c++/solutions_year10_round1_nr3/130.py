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

long double dd = (sqrt(5.0)-1) / 2;

ll calc(int a, int b) {
  if (b == 0) return 0;
  ll ret = 0;
  if (b >= a * 2) {
    ret += b - (a*2-1);
    b = a*2-1;
  }
  if (b <= a) {
    int k = (int)(a * dd);
    ret += min(k, b);
    return ret;
  }
  if (b > a) {
    ret += (int)(a * dd);
    ret += (b-a) - calc(a, b-a);
    return ret;
  }
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
          ll ans = 0;
          int a1, a2, b1, b2;
          fin >> a1 >> a2 >> b1 >> b2;
          for (int a = a1; a <= a2; ++a) {
            ans += calc(a, b2) - calc(a, b1-1);
          }

          fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
