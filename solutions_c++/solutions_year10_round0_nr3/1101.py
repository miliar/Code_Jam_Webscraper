#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
#include <map>
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

int r, k, n;
int g[1001];
int sum[2001] = {};

ll calc() {
  if (sum[n] <= k) return (ll)sum[n] * r;

  ll ans = 0;
  map<int, int> m;
  vector<ll> v;
  m[0] = 0;
  v.push_back(0);
  int r1 = 0;
  int i = 0;
  while (r1 < r) {
    int j = i+1;
    while (sum[j] - sum[i] <= k) ++j;
    --j;
    int j1 = j % n;
    ++r1;
    int ppl = sum[j] - sum[i];
    ans += ppl;
    v.push_back(v[v.size()-1] + ppl);
    if (m.count(j1) > 0) {
      // loop
      int len = r1 - m[j1];
      int loop = (r-r1) / len;
      int residue = (r-r1) % len;
      int r0 = m[j1];
      ans += (ll)loop * (v[r1] - v[r0]);
      ans += v[r0 + residue] - v[r0];
      return ans;
    }
    m[j1] = r1;
    i = j1;
  }
  return ans;
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
          fin >> r >> k >> n;
          for (int i = 1; i <= n; ++i) fin >> g[i];
          sum[0] = 0;
          for (int i = 1; i <= n; ++i) sum[i] = sum[i-1] + g[i];
          for (int i = 1; i <= n; ++i) sum[n+i] = sum[n+i-1] + g[i];
          ll ans = calc();
          fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}
