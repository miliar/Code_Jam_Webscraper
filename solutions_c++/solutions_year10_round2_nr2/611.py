#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <vector>
#include <bitset>
#include <algorithm>
#include <functional>
#include <string.h>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FORN(i,n) FOR(i,0,(n))
#define FOR(i,a,n) for(int i=(a);i<(n);i++)
#define sz size()
#define PB push_back
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define PRESENT(container, element) (container.find(element) != container.end())
#define ALL(x) x.begin(), x.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define DIST(x1,y1,x2,y2) sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define ON 1
#define OFF 0
using namespace std;


int position[300];
int vel[300];
int valid[300];




int main(){
  int T,n,k,b,t;
  cin>>T;
  int cases=1;

  while (T--){
    cin>>n>>k>>b>>t;
    FORN(i,n) cin>>position[i];
    FORN(i,n) cin>>vel[i];
    FORN(i,n) valid[i]=0;
    int posibles=0;

  FORN(i,n)
       if  ((position[i]+(vel[i]*t))>=b){
	valid[i]=1;
	posibles++;
      }

    
    int arrives=0;
    int ch=n-1;
    int res=0;

    while (ch>=0 && arrives<k){
      
      if (valid[ch]){
	FOR(i,ch+1,n){
	    if(valid[i]==0) res++;
	}
      arrives++;
      }
      ch--;
    }

    if (arrives<k) 
        printf("Case #%d: IMPOSSIBLE\n",cases++,0);
    else
    printf("Case #%d: %d\n",cases++,res);
  }
}












