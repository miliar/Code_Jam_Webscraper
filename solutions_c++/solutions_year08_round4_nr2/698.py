#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <numeric>

#include <cassert>
#include <cstdio>

#define REP(i,e) for(int i=0;i<(int)(e);i++)
#define FOR(i,b,e) for(int i=(int)(b);i<(int)(e);i++)

using namespace std;

int cross(int a,int b,int c,int d){
  return a*d-b*c;
}
main(){
  int CT;
  cin >> CT;
  REP(C,CT){
    int n,m,a;
    cin >> n >> m >> a;
    cout << "Case #" << C+1 << ": ";

    n++; m++;
    bool f=false;
    REP(i,n){
      REP(j,m){
	if(f) break;
	REP(ii,n){
	  if(f) break;
	  REP(jj,m){
	    if(f) break;
	    if(a==abs(i*jj-j*ii)){
	      cout << "0 0 " << i << ' ' << j << ' ' << ii << ' ' << jj << endl;
	      f=true;
	    }
	  }
	}
      }
    }
    if(!f) cout << "IMPOSSIBLE" << endl;
  }
}
