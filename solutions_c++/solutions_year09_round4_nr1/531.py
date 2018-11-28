#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int main() {
  int tests;
  cin >> tests;
  FOT(t, 1, tests+1) {
    int n;
    cin >> n;
    vi v;
    FOR(i, n) {
      string s;
      cin >> s;
      int last = -1;
      FOR(j, n) if(s[j] == '1') last = j;
      v.pb(last);
    }
    int ans = 0;
    for(int i = 0; i < n; i++) {
      for(int j = i; j < n; j++)
	if(v[j] <= i) {
	  ans += j - i;
	  for(int k = j; k > i; k--)
	    v[k] = v[k-1];
	  break;
	}
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
