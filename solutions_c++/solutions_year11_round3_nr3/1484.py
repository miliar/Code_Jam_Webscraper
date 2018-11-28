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

typedef unsigned long long ull;


using namespace std;


long long GCD(long long a, long long b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}


long long LCM(long long a,long long b)
  {
    return (a*b)/GCD(a,b);
  }

int main(){	 
  freopen("input-C.txt", "r", stdin);
  freopen("output-C.txt", "w", stdout);

  int casos_,total,N,L,H;
  cin>>casos_;

  FORN(casos,casos_){

    cin>>N>>L>>H;
    vector<long long>v(N);
    FORN(i,N)cin>>v[i];
    sort(ALL(v));
    
    int gcd=1;
    int val=-1;
     FOR(i,L,H+1){
      bool ok=1;
	FORN(j,N){
	  ok=ok&&((v[j]%i)==0 || (i%v[j])==0 );
	}
	if (ok){
	   val=i;
	  break;
	}
    }
  if (val!=-1)
 cout<<"Case #"<<(casos+1)<<": "<<val<<endl;
else  cout<<"Case #"<<(casos+1)<<": NO"<<endl;

  }
}

  


