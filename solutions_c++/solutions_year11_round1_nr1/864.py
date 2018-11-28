#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
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

typedef  long long ll;


using namespace std;


int main(){

  int n;

  cin>>n;
  
  FORN(i,n){
      bool posible=0;
      ll MX,T,A;
      cin>>MX>>T>>A;
      
      //ALL 100%
      if (A==100){
	if (T==100)
	    posible=1;
	else posible=0;
	goto end;
      }
     
      //ALL 100%
      if (T==100){
	if (A>0)
	    posible=1;
	goto end;
      }
 
      if (A==0 && T==0)
      {
	posible=1;
	goto end;
      }
      
     //ALL 100%
      if (MX>=100 ){
	    if (T>0){
	      if (A>0){
		posible=1;
	      }
	      else{
		posible=0;
	      }
	    }
	    else {
	      posible = 1;
	    }
	 goto end;
      }
      
      
      if (T>0 && A==0)
      {
	posible=0;
       goto end;
      }
      
       if (T==0 && A>0)
      {
	posible=1;
       goto end;
      }
      
      if (T>0)
      FORN(j,MX){
	if ( (((j+1)*T)%100==0) && A>0)
	    posible=true;
      }
 
      end:
      cout<<"Case #"<<i+1<<": "<<(posible?"Possible\n":"Broken\n");
  }

}
