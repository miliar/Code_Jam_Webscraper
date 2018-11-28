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



vector<string> M;
int C,R;


void debug(){
  FORN(i,R)
  cout<<M[i]<<endl;
}
bool solve(){
    FORN(i,R){
      FORN(j,C){
	if (M[i][j]=='#'){
	  if ((j+1)<(C)){
	    M[i][j]='/';
	    M[i][j+1]='\\';
	    if ((i+1)<R){
	      M[i+1][j]='\\';
	      M[i+1][j+1]='/';
	    }
	    else{
// 	      debug();
// 	      cout<<"false xxx en"<<i << " " <<j<<endl;
	      return false;
	    }
	  }
	  else{
// 	      debug();
// 	    cout<<"false yyy en"<<i << " " <<j<<endl;
	    return false;
	  }
	}
      }
    }
    return true;
}

int main(){	 
  freopen("input-A.txt", "r", stdin);
  freopen("output-A.txt", "w", stdout);

  int casos_,total;
  cin>>casos_;

  FORN(casos,casos_){
    cin>>R>>C;
    M=vector<string>(R);
    FORN(i,R)
      cin>>M[i];

    cout<<"Case #"<<(casos+1)<<": "<<endl;
    
    if  (solve()){
      FORN(i,R)
	cout<<M[i]<<endl;	
    }
    else cout<<"Impossible"<<endl;
  }

  
}

