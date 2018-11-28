
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
  int T, R, k, N;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    long long h = 0;
    cin >> R >> k >> N;
    vector<int> g(N);
    for (int j = 0; j < N; j++) {
      cin >> g[j];
      h += g[j];
    }

    if (h <= k) cout << "Case #" << i << ": " << R*h << "\n";
    else {
      int b = 0;
      map<int,int> m;
      vector<int> v;
      long long z = 0;
      for (int r = 0; m.find(b) == m.end(); r++) {
	m[b] = r;
	long long x = 0;
	for (; x + g[b] <= k; b = (b+1)%N)
	  x += g[b];
	z += x;
	v.push_back(z);
	//cout << b << "," << z << "\n";
      }
      int t = m[b];

      if (R <= v.size()) cout << "Case #" << i << ": " << v[R-1] << "\n";
      else {
	long long s = z;
	if (t > 0) z -= v[t-1];
	R -= v.size();
	int f = R/(v.size()-t), q = R%(v.size()-t);
	//cout << s << "," << R << "," << f << "," << q << "," << z << "\n";
	if (q > 0) s += v[t+q-1] - (t > 0 ? v[t-1] : 0);
	cout << "Case #" << i << ": " << s + z*f << "\n";
      }
    }
  }
}
