#include <iostream>
#include <cstdio>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <algorithm>
#include <math.h>
using namespace std;
#define For(i,a,b) for (i = a; i != b; ++i)
#define Rep(i,n) For(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define set(a,c) memset(a,c,sizeof(a))
#define pb push_back
int calc(const string& S) {
  int i;
  char ch = S[0];
  int len = 1;
  For(i,1,S.length()) {
    if (S[i] == ch)
      continue;
    ch = S[i];
    len++;
  }
  return len;
}
int main() {
  int t = GI, test;
  int i,j,k;
  Rep(test,t) {
    cout << "Case #" << test+1 << ": ";
    int k = GI;
    vector<int> V;
    V.clear();
    Rep(i,k) {
      V.pb(i);
    }
    string S;
    cin>>S;
    int len = S.length();
    string ans = S;
    int mn = calc(S);
    string tmp = S;
    do
      {
	for (i = 0; i < len; i+=k) {
	  Rep(j,V.size()) {
	    tmp[i+j] = S[V[j] + i];
	  }
	}
	int run = calc(tmp);
	mn <?= run;
      }while (next_permutation(V.begin(),V.end()));
    cout << mn << endl;
  }
}
