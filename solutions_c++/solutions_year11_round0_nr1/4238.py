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
  FOT(t, 1, (tests + 1)) {
    int N;
    cin >> N;
    
    int w[2], a[2];

    FOR(i, 2) {
      w[i] = 1;
      a[i] = 0;
    }
    
    
    FOR(zz, N) {
      char c;
      int p;
      cin >> c >> p;
      int who = (c == 'O');
      FOR(i, 2)
        if(i == who) {
          a[i] = 1 + max(a[i] + abs(w[i] - p), a[1-i]);
          w[i] = p;
          cerr << i << ' ' << a[i] << ' ' << w[i] << endl;
        }
    }
    
    cout << "Case #" << t << ": " << max(a[0], a[1]) << endl;
  }
  
  
  return 0;
}
