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

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    int N; cin>>N; // 1-3-100
    int sup; cin>>sup; // 0-N
    int p; cin>>p; // 0-10
    vector<int> tj(N); rep(n,N) cin>>tj[n];

    int gog=0;
    //vector<int> tw,on;
    int tw=0;
    rep(n,N){
      int a=tj[n]/3, b=tj[n]%3;
      switch (b) {
        case 0:
          if (a >= p) gog++;
          else if (a>0 && a+1 >= p)tw++;
          break;
        case 1:
          if (a+1 >= p) gog++;
          break;
        case 2:
          if (a+1 >= p) gog++;
          else if (a>0 && a+2 >= p)tw++;
          break;
      }
    }

    //cout << sup << " " << p << tj << endl;
    //printf("%d %d\n", gog,tw);
    if (tw <= sup) gog += tw;
    else/* if (tw > sup)*/ gog += sup;


    printf("Case #%d: %d\n", 1+_t, gog);

  }
  return 0;
}
