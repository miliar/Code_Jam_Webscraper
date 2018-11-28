/* 
 * 
 * File:   A.cpp
 * Author: Andy Huang
 * Created on April 13, 2012, 7:00 PM
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
#define pln(x) cout << (x) << endl;
#define ve(x) vector<x>
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define ms(x,n) memset(x,n,sizeof(x))

using namespace std;

const char x[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b',
'k','r','z','t','n','w','j','p','f','m','a','q'};

void solve() {
  string s;
  gl(s);
  forl(i,0,s.length()){
    if (s[i] >= 'a'){
      cout << x[s[i]-'a'];
    }
    else
      cout << s[i];
  }
}

int main() {
  #ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  #endif
  int t;
  cin >> t;
  string s;
  gl(s);
  forl(i,1,t+1){
    printf("Case #%d: ",i);
    solve();
  }
  return 0;
}

