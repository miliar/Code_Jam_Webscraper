#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;

int main()
{
  int N;
  cin >> N;
  for (int a = 1; a <= N; a++) {
    long long n, A, B, C, D, x0, y0, M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

    long long x[n], y[n];
    x[0] = x0;
    y[0] = y0;

    for (int i = 1; i < n; i++) {
      x[i] = (A * x[i-1] + B) % M;
      y[i] = (C * y[i-1] + D) % M;
    }

    int ans = 0;
    for (int i = 0; i < n-2; i++) {
      for (int j = i+1; j < n-1; j++) {
	for (int k = j+1; k < n; k++) {
	  if (((x[i] + x[j] + x[k]) / 3) * 3 == (x[i] + x[j] + x[k]) && ((y[i] + y[j] + y[k]) / 3) * 3 == (y[i] + y[j] + y[k])) {
	    ans++;
	  }
	}
      }
    }

    cout << "Case #" << a << ": " << ans << endl;
  }

  return 0;
}
