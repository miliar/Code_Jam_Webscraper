#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>

using namespace std;
#define REP(i,N) for (int i = 0; i<(N); i++) 
#define ll long long
#define P pair<int, int> 

map<P, bool> mp;

bool win(int a, int b){
  if (a<b) swap(a,b);
  if (a==b) return false;
  if (mp.find(P(a,b)) != mp.end()) return mp[P(a,b)];
  bool &m = mp[P(a,b)];
  m=false;
  for (int i=max(a/b-2, 1); b*i<a; i++){
    if (!win( a-b*i, b)) m = true;
  }
  return m;
}

int main(){
  int T;
  cin >> T;
  for (int iii=0; iii<T; iii++){
    int a,b,c,d;
    cin >> a >> b >> c >> d;
    int ans = 0;
    for (int i=a; i<=b; i++){
      for (int j=c; j<=d; j++){
	if (win(i,j)) ans++;
      }
    }
    printf ("Case #%d: %d\n",iii+1, ans);
  }
  return 0;
}
