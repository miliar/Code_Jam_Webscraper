#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

int main()
{
  int tests = GETINT;
  for(int t = 1; t <= tests; t++) {
    int n;
    n = GETINT;
    vi a;
    FOR(i, n) a.pb(GETINT);

    map<int, int > have;
    int other = -1, first;

    int m = (1 << n);
    FOR(i, m) {
      int cur = 0;
      FOR(j, n) if (i & (1 << j)) cur += a[j];
      if(have.find(cur) != have.end()) {
	other = i;
	first = have[cur];
	break;
      }
      have[cur] = i;
    }

    cout << "Case #" << t << ":" << endl;
    if(other == -1) cout << "Impossible" << endl;
    else {
      int common = first & other;
      first ^= common;
      other ^= common;
      FOR(i, n) if(first & (1 << i)) { cout << a[i]; first ^= (1 << i); if(first == 0) cout << endl; else cout << ' '; }
      FOR(i, n) if(other & (1 << i)) { cout << a[i]; other ^= (1 << i); if(other == 0) cout << endl; else cout << ' '; }
    }
  }
  return 0;
}
