#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
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

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;


const int BIGG = 12345678;
const int MODD = 10007;

inline int power(int number)
{
  int ret = 0;
  while(number > 0) {
    ret += number / MODD;
    number /= MODD;
  }
  return ret;
}

int inverse[10007];
int answer[77777777];

ll find(int a, int b)
{
  assert(a >= b);
  if(power(a) > power(b) + power(a - b)) {
    //    cerr << a << ' ' << b << "bad " << endl;
    return 0;
  }
  else {
    assert(power(a) == power(b) + power(a - b));
    //    cerr << a << ' ' << b << ' ' << answer[a] << ' ' << inverse[answer[b]] << endl;
    return ((ll(answer[a]) * ll(inverse[answer[b]])) % MODD * ll(inverse[answer[a-b]])) % MODD;
  }
}


int calc(int x, int y)
{
  int answer = 0;
  if(((ll(2) * ll(x) - ll(y)) % 3 != 0) ||
     ((ll(2) * ll(y) - ll(x)) % 3 != 0)) {
    //    cerr << "mod check failed " << x << ' ' << y << endl;
  }
  else {
    ll a, b;
    a = ((ll(2) * ll(x) - ll(y)) / 3);
    b = ((ll(2) * ll(y) - ll(x)) / 3);
    if(a < 0 || b < 0) return 0;
    //    cerr << "convert " << x << ' ' << y << ' ' << a << ' ' << b << endl;
    answer = find(a+b, b);
  }
  return answer;
}
      
      

int main()
{

  FOT(i, 1, MODD) {
    FOT(j, 1, MODD) {
      if((ll(i) * ll(j)) % MODD == 1) {
	inverse[i] = j;
	break;
      }
    }
  }

  answer[0] = 1;
  //  cerr << "--" << endl;  
  FOT(i, 1, 77777777) {
    int mult = i;
    while(mult % MODD == 0) mult /= MODD;
    answer[i] = (ll(answer[i-1]) * ll(mult)) % MODD;
  }
  cerr << "all done " << endl;
  int tests;
  cin >> tests;
  cerr << tests << endl;
  FOT(_t, 1, tests+1) {
    cerr << _t << endl;
    int H, W, R;
    cin >> H >> W >> R;
    vector< PII > bad;
    FOR(i, R) {
      int a, b;
      cin >> a >> b;
      bad.pb(mp(a-1,b-1));
    }
    int answer = calc(H-1,W-1);
    //    cerr << "prelim " << answer << endl;
    FOR(mask, (1 << R)) {
      if(mask == 0) continue;
      vector< PII > cur;

      cur.pb(mp(0,0));
      cur.pb(mp(H-1,W-1));

      FOR(j, R) if(mask & (1 << j)) cur.pb(bad[j]);
      sort(cur.begin(), cur.end());
      bool good = true;
      FOR(i, cur.size() - 1) if(cur[i].second >= cur[i+1].second) {
	good = false;
	break;
      }
      if(good) {
	ll cc = 1;
	FOT(i, 1, cur.size()) cc = (ll(cc) * ll(calc(cur[i].first - cur[i-1].first, 
						     cur[i].second - cur[i-1].second))) % MODD;
	if(cur.size() % 2 == 1) answer = (answer - cc) % MODD;
	else answer = (answer + cc) % MODD;
      }
    }
    while(answer < 0) answer += MODD;
    cout << "Case #" << _t << ": " << answer % MODD << endl;
    //    cerr << "------------------------" << endl;
    
  }
  return 0;
}
