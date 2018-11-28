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

vector< vi > perms;
int k;

void generate(vi sofar)
{
  if(s(sofar) == k) perms.pb(sofar);
  else {
    FOR(i, k) {
      bool good = true;
      FOR(j, s(sofar)) good = good && (sofar[j] != i);
      if(good) {
	vi nu = sofar;
	nu.pb(i);
	generate(nu);
      }
    }
  }
}


int main()
{
 
  int tests;
  cin >> tests;
  FOT(_t, 1, tests+1) {
    string st;
    cin >> k;
    cin >> st;
    perms.clear();
    vi empty;
    generate(empty);
    int __answer = 1234567;
    FOR(a, perms.size()) {
      string cur;
      cur.resize(st.size());
      FOR(b, st.size() / k) {
	FOR(c, k) {
	  cur[b * k + c] = st[b * k + perms[a][c]];
	}
      }
      cur += '!';
      int aa = 0;
      FOR(i, s(cur) - 1) aa += (cur[i+1] == cur[i] ? 0 : 1);
      __answer = min(__answer, aa);
    }    
    cout << "Case #" << _t << ": " << __answer << endl;
  }
  return 0;
}
