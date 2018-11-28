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

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;


int main() {
  string search = "welcome to code jam";
  int ss = s(search);

  int n;
  scanf("%d\n", &n);

  FOT(test, 1, n+1) {
    string s;
    getline(cin, s);
    int ans[ss+1];
    FOR(i, ss+1) ans[i] = 0;
    ans[0] = 1;
    FOR(j, s(s)) {
      FOR(i, ss)
        if(s[j] == search[i]) {
          ans[i+1] = (ans[i] + ans[i+1]) % 1000;
        }
    }
    int a = ans[ss];
    printf("Case #%d: ", test);
    if(a < 1000) printf("0");
    if(a < 100) printf("0");
    if(a < 10) printf("0");
    printf("%d\n", a);    
  }

  return 0;
}
