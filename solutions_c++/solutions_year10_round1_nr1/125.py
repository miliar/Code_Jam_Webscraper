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

void check(int& ans, int k, int n, const int a[]) {
  int i = 0;
  while (i < n) {
    if (a[i] == 0) {
      ++i;
      continue;
    }
    int j = i+1;
    while (j < n && a[i] == a[j]) ++j;
    if (j - i >= k) {
      ans |= a[i];
    }
    i = j;
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
          int n, k;
          fin >> n >> k;
          string str;
          int m[51][51];
          mset(m, 0);
          for (int i = 0; i < n; ++i) {
            fin >> str;
            int k = n-1;
            for (int j = n-1; j >= 0; --j) {
              if (str[j] != '.') {
                m[i][k] = (str[j] == 'B') ? 1 : 2;
                --k;
              }
            }
          }
          int ans = 0;
          int p[101];
          for (int i = 0; i < n; ++i) {
            if (ans == 3) break;
            check(ans, k, n, m[i]);
          }
          for (int i = 0; i < n; ++i) {
            if (ans == 3) break;
            for (int j = 0; j < n; ++j) p[j] = m[j][i];
            check(ans, k, n, p);
          }
          for (int i = 0; i < n; ++i) {
            if (ans == 3) break;
            for (int j = 0; j <= i; ++j) p[j] = m[j][i-j];
            check(ans, k, i+1, p);
          }
          for (int i = 1; i < n; ++i) {
            if (ans == 3) break;
            for (int j = 0; j < n-i; ++j) p[j] = m[j+i][n-1-j];
            check(ans, k, n-i, p);
          }
          for (int i = 0; i < n; ++i) {
            if (ans == 3) break;
            for (int j = 0; j < n-i; ++j) p[j] = m[j][i+j];
            check(ans, k, n-i, p);
          }
          for (int i = 1; i < n; ++i) {
            if (ans == 3) break;
            for (int j = 0; j < n-i; ++j) p[j] = m[i+j][j];
            check(ans, k, n-i, p);
          }
          string ss[4];
          ss[0] = "Neither";
          ss[1] = "Blue";
          ss[2] = "Red";
          ss[3] = "Both";
          cout << ans << endl;
          fout << "Case #" << tind << ": " << ss[ans] << endl;
	}
	return 0;
}
