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
    int A = GETINT;
    int B = GETINT;
    int d = 0, e = A, p = 1;
    for(; e > 0; e /= 10, d++, p *= 10); p /= 10;
    set < PII > pairs;
    FOT(i, A, B + 1) {
      int e = i;
      FOR(j, d) {
	int l = e % 10;
	e = l * p + e / 10;
	if((l > 0) && (A <= e) && (e <= B) && (e < i)) pairs.insert(PII(i, e));
      }
    }
    cout << "Case #" << t << ": " << pairs.size() << endl;
  }
  return 0;
}
