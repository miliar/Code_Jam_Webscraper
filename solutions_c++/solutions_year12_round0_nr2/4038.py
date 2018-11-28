#include <iostream>

using namespace std;

int solve()
{
  int n,s,p;
  cin >> n >> s >> p;

  int r = 0;

  for(int i=0; i<n; i++) {
    int sc;
    cin >> sc;
    int cmax = (sc+2) / 3;
    if(cmax >= p) {
      r++;
      continue;
    }
    if(s==0)
      continue;

    if(cmax + 1 < p)
      continue;

    if((sc % 3 == 2) || ((sc % 3 ==0) && (sc > 0))) {
      r++;
      s--;
    }
  }
  return r;
}

main()
{
  int t;
  cin >> t;
  for(int tt=0; tt<t; tt++)
    cout << "Case #" << (tt+1) << ": " << solve() << endl;
}
