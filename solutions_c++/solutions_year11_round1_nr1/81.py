#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<map>
#include<set>
#include<queue>
#include<cstdio>
#include<climits>
#include<cmath>
#include<cstring>
#include<string>
#include<sstream>
#include<numeric>
#include<cassert>

#define f first
#define s second
#define mp make_pair

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define rep(i,s,n) for(int i=(s); i<(int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define ALL(c) (c).begin(), (c).end()
#define IN(x,s,g) ((x) >= (s) && (x) < (g))
#define ISIN(x,y,w,h) (IN((x),0,(w)) && IN((y),0,(h)))
#define print(x) printf("%d\n",x)

using namespace std;

typedef unsigned int uint;
typedef long long ll;

const int _dx[] = {0,1,0,-1};
const int _dy[] = {-1,0,1,0};

int getInt(){
  int ret = 0,c;
  c = getchar();
  while(!isdigit(c)) c = getchar();
  while(isdigit(c)){
    ret *= 10;
    ret += c - '0';
    c = getchar();
  }
  return ret;
}

template<class T>
T gcd(T a, T b){
  if(a > b) swap(a, b);
  if(a == 0) return b;
  return gcd(b % a, a);
}

int main(){
  int c; cin>>c;

  REP(cc, c){
    ll n; cin>>n;
    int pd; cin>>pd;
    int pg; cin>>pg;

    int B = pd;
    int A = 100;
    bool ans = true;

    int tmp = gcd(A, B);
    A /= tmp; B /= tmp;
      
    if(A > n) ans = false;
    if((pg == 0 || pg == 100) && pd != pg)
      ans = false;

    printf("Case #%d: %s\n", cc+1, ans ? "Possible" : "Broken");
  }

  return 0;
}
