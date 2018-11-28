#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

long double f[1001];
int n;

int main() {
  f[0] = 0;
  f[1] = 0;
  long double s = 0;
  
  for(int i=2;i<=1000;i++){
    f[i] = (s+1) * 2 / (i-1);
    s += f[i];
  }

  //for(int i=0;i<100;i++)cerr << f[i] << ' ';cerr << '\n';

  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    cout << "Case #" << tcase << ": ";

    cin >> n;
    vector<int> p(n);

    for(int i=0;i<n;i++)
      cin >> p[i];
    
    long double res = 0;
    for(int i=0;i<n;i++)
      if(p[i]) {
	int cur = i, clen = 0;
	for(;p[cur];clen++) {
	  int last = cur;
	  cur = p[cur]-1;
	  p[last] = 0;
	}
	//cerr << clen << ' ';
	res += f[clen];
      }
    //cerr << '\n';
    cout << res << '\n';
  }
}
