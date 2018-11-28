#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++) 
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

//#include "cout.h"

void lower(int x, int& lw, int& k){
  lw=1; k=1;
  while (x > 10) {
    lw*=10; k++; x/=10;
  }
}

int rdg[7] = { 1,10,100,1000,10000,100000,1000000 };
int rot(int x,int k,int r){
  int w = rdg[r];
  int head = x / w, tail = x % w;
  return tail * rdg[k-r] + head;
}

main(){
  int _T; cin>>_T;//50
  rep(_t,_T){
    int A,B; cin>>A>>B; // 1000,2e6
    if (A==B || B < 10) {
      printf("Case #%d: %d\n", 1+_t, 0); continue;
    }

    int lw,k; lower(B,lw,k);
    int cnt = 0;
    //printf("lower(%d) => %d,%d\n", B,lw,k);
    for (int b=lw; b<=B; ++b) {
      set<int> ra;
      for (int r=1; r<k; ++r){
        int a = rot(b,k,r);
        if (a < lw) continue;
        if (a < A) continue;
        if (a >= b) continue;

        if (found(ra,a)) continue;
        ra.insert(a);
        //printf("rot(%d,%d,%d) => %d\n", b,k,r,a);
        //printf("%d <= %d < %d <= %d (rot %d)\n", A,a,b,B, r);
        //if (_t==3) printf("%d %d\n", a,b);
        cnt++;
      }
    }

    printf("Case #%d: %d\n", 1+_t, cnt);
  }
}
