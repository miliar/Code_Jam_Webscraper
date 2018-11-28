#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for((a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))

typedef vector<int> vi;
typedef vector <string> vs;


int main()
{
    int ntest;
    cin >> ntest;    
    RP(t, ntest)
    {
          int p, l, k;
          cin >> p >> k >> l;
          vi a(l);
          RP(i, l)
          {
                cin >> a[i];
          }
          
          long long idx = 1;
          
          sort(a.rbegin(), a.rend());
          
          long long s = 0;
          long long res = 0;
          long long tmp = 0;
          while(s < l)
          {
                  res += a[s]*idx;
                  tmp++;
                  s++;
                  if (tmp == k)
                  {
                          tmp = 0;
                          idx++;
                  }
          }
          
          cout << "Case #" << t+1 << ": " << res << endl;
    }
    return 0;
}
