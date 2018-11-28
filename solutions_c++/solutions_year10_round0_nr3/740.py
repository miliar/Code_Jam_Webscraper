#include <iostream>

using namespace std;

const int maxn = 1000;

long long gsum;
long long g[maxn];
long long profit[maxn];
long long round[maxn];

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    long long r, k, n;
    cin >> r >> k >> n;
    for(int i=0;i<n;i++)
      cin >> g[i];

    long long gsum = 0;
    for(long long i=0;i<n;i++) gsum += g[i];

    for(int i=0;i<n;i++) profit[i] = -1;

    int pos = 0;
    long long cprof = 0;
    for(;r;--r) {
      //cerr << "+" << r << ' ' << pos << ' ' << cprof << '\n';
      if((profit[pos]!=-1) && (round[pos]<=2*r)) {
	long long profper = (cprof - profit[pos]);
	long long rper = round[pos] - r;
	cprof += profper * (r / rper);
	r -= (r / rper) * rper;//r %= rper;
	if(!r) break;
      }
      profit[pos] = cprof;
      round[pos] = r;

      long long size = 0;
      if(k >= gsum)
	size = gsum;
      else 
	for(;size + g[pos] <= k;pos=(pos+1)%n)
	  size += g[pos];
      cprof += size;
    }
    cout << "Case #" << tcase << ": " << cprof << '\n';
  }
}
