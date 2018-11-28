#include <algorithm>
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


int main()
{
  int tests;
  cin >> tests;
  FOT(_t, 1, tests+1) {

    int M, N, A;
    cin >> N >> M >> A;
    N++;
    M++;
    
    int x1, y1, x2, y2;
    x1 = y1 = x2 = y2 = -1;

    FOR(a, N) FOR(b, M) FOR(c, N) FOR(d, M) if(abs(a * d - b * c) == A) {
      x1 = a;
      y1 = b;
      x2 = c;
      y2 = d;
      a = b = c = d = max(N,M);
      break;
    }
    cout << "Case #" << _t << ": ";
    if(x1 == -1) cout << "IMPOSSIBLE";
    else cout << "0 0 " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2;
    cout << endl;
  }
  return 0;
}
