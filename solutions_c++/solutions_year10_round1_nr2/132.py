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

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
          int del, ins, m, n;
          int a[110];
          int f[110][256];
          fin >> del >> ins >> m >> n;
          for (int i = 0; i < n; ++i) fin >> a[i];
          int ans = del * n;
          for (int i = 0; i < n; ++i) for (int vi = 0; vi <= 255; ++vi) {
              int bcost = abs(vi - a[i]);
            f[i][vi] = del * i + bcost;
            if (i > 0) {
              int cost = bcost + f[i-1][vi] + del;
              if (cost < f[i][vi]) f[i][vi] = cost;

            for (int vj = 0; vj <= 255; ++vj) {
              int cost = bcost + f[i-1][vj];
              int k = abs(vi - vj);
              if (k > 0) {
                k = (k-1) / m;
              }
              cost += k * ins;
              if (cost < f[i][vi]) f[i][vi] = cost;
            }
            }
            int cost = f[i][vi] + del * (n-1-i);
            if (cost < ans) {
              //cout << ans << ' ' << cost << endl;
              ans = cost;
            }
          }
          fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
