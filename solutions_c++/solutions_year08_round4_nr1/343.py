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

#define maxn 20000

int type[maxn], value[maxn];
int canchange[maxn];
int nodes;
int ans[maxn][2];

const int INF = 1234567;

int find(int which, int what)
{
  assert(which < nodes);
  if(ans[which][what] != -1) return ans[which][what];
  //cerr << "in " << which << ' ' << what << endl;
  int& a = ans[which][what];
  if(which >= (nodes - 1) / 2) {
    //    cerr << "here" << endl;
    if(what != value[which]) a = INF;
    else a = 0;
  }
  else {
    int ao, aa;
    ao = aa = INF;
    FOR(i, 2) FOR(j, 2) 
      if((i || j) == what) ao = min(ao, find(2 * which + 1, i) + find(2 * which + 2, j));
    FOR(i, 2) FOR(j, 2) 
      if((i && j) == what) aa = min(aa, find(2 * which + 1, i) + find(2 * which + 2, j));
    if(type[which] == 0) {
      a = ao;
      if(canchange[which]) a = min(a, 1 + aa);
    }
    else {
      a = aa;
      if(canchange[which]) a = min(a, 1 + ao);
    }
  }
  //cerr << "answer for " << which << ' ' << what << ' ' << a << endl;
  return a;
}
      
    
	
	
      
    

int main()
{
  int tests;
  cin >> tests;
  FOT(_t, 1, tests+1) {
    int num, want;
    cin >> num >> want;
    nodes = num;
    FOR(i, (num - 1) / 2) cin >> type[i] >> canchange[i];
    FOR(i, (num + 1) / 2) cin >> value[i + (num - 1) / 2];

    FOR(i, num) FOR(j, 2) ans[i][j] = -1;
    int got = find(0, want);
    cout << "Case #" << _t << ": ";
    if(got >= INF) cout << "IMPOSSIBLE";
    else cout << got;
    cout << endl;
  }
  return 0;
}
