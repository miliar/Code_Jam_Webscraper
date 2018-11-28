/* 
 * 
 * File:   B.cpp
 * Author: Andy Huang
 * Created on April 13, 2012, 7:19 PM
 */

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <fstream>
#include <set>
#include <map>
#include <sstream>
#include <deque>

#define forl(a,b,c) for (int a=b;a<c;a++)
#define ford(a,b,c) for (int a=b;a>=c;a--)
#define gl(s) getline(cin,s)
#define pln(x) cout << (x) << '\n'
#define ve(x) vector<x>
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define ms(x,n) memset(x,n,sizeof(x))

using namespace std;

int x[105];

void solve() {
  int n,s,p,ans = 0;
  cin >> n >> s >> p;
  forl(i,0,n){
    cin >> x[i];
  }
  int a = max(0,p-2);
  int b = max(0,p-1);
  forl(i,0,n){
    if (p+p+p <= x[i] || p+b+b <= x[i] || p+p+b <= x[i])
      ans++;
    else if (s && (a+b+p<=x[i] || a+a+p <= x[i] || a+p+p <= x[i])){
      ans++;
      s--;
    }
  }
  pln(ans);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.out", "w", stdout);
  int t;
  cin >> t;
  forl(i,1,t+1){
    printf("Case #%d: ",i);
    solve();
  }
  return 0;
}

