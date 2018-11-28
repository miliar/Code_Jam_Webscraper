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
    int N = GETINT;
    vi arr;
  
    FOR(i, N) arr.pb(GETINT);
    sort(ALL(arr));

    int zsum, bsum;
    zsum = bsum = 0;

    FOR(i, N) {
      zsum += arr[i];
      bsum ^= arr[i];
    }

    printf("Case #%d: ", t);

    if(bsum == 0) printf("%d\n", zsum - arr[0]);
    else printf("NO\n");
  }
  return 0;
}
