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
  int tests;
  cin >> tests;
  FOT(t, 1, tests + 1) {
    int n, l, h;
    cin >> n >> l >> h;
    vi v;
    FOR(i, n) {
      int d;
      cin >> d;
      v.pb(d);
    }

    int what = -1;
    FOT(f, l, h + 1) {
      bool cur = true;
          
      FOR(i, s(v))
        if((v[i] % f != 0) && (f % v[i] != 0)) {
          cur = false;
          break;
        }
      if(cur) {
        what = f;
        break;
      }
    }
    
    cout << "Case #" << t << ": ";
    if(what > 0) cout << what << endl;
    else cout << "NO" << endl;    
  }
  
  
  return 0;
}
