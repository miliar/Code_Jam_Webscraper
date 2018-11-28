#include <iostream>
#include <sstream>
#include <cstring>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define For(i,a,b) for (i = a; i != b; i++)
#define Rep(i,n) For(i,0,n)
#define set(a,c) memset(a,c,sizeof(a))
#define pb push_back
#define EACH(it,V) for (__typeof(V) it = V.begin(); it != V.end(); it++)
#define GI ({int t;scanf("%d",&t);t;})
typedef vector<string> vi;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
vi V;
map<vi,int> dp;
map<vi,bool> reach;
queue<vi> Q;
int N;
bool check(vi& V) {
  int i;
  Rep(i,V.size()) {
    string num = V[i];
    int x = N-i;
    for(int j = num.length()-1; j >= 0;j--) {
      if (num[j] == '0') {
	//cout << "x = " << x << endl;
	x--;
	continue;
      }
      break;
    }
    if (x <= 1) {
      continue;
    }
    return false;
  }
  return true;
}

int memo(vi V) {
  reach[V] = 1;
  dp[V] = 0;
  Q.push(V);
  int i;
  while (!Q.empty()) {
    V = Q.front();
    Q.pop();
    /*Rep (i,V.size()) {
      cout << V[i] << " ";
    }
    cout << endl;*/
    if (check(V)) {
      return dp[V];
    }
    vi old = V;
    For(i,1,V.size()) {
      swap(V[i],V[i-1]);
      if (!reach[V]) {
	Q.push(V);
	reach[V] = 1;
	dp[V] = dp[old] + 1;
      }
      swap(V[i],V[i-1]);
    }
  }
  return dp[V];
}
main() {
  int t, cas;
  cin >> t;
  For(cas,1,t+1) {
    dp.clear();
    V.clear();
    reach.clear();
    while (!Q.empty())
      Q.pop();
    cout << "Case #" << cas << ": ";
    cin >> N;
    int i;
    Rep(i,N) {
      string str;
      cin >> str;
      V.pb(str);
    }
    cout << memo(V) << endl;
  }
}
