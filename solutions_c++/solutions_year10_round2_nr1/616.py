#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <vector>
#include <bitset>
#include <algorithm>
#include <functional>
#include <string>
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
typedef  long long ull;

 map<string,bool> M;

int c(string s){
  
  string tmp1=s;
  FORN(i,s.size()) if (tmp1[i]=='/')tmp1[i]=' ';
  stringstream st(tmp1);
  int a=0;
  string tmp;
  string t="";
  while (st>>tmp){
    t+=" ";
    t=t+tmp;
    if (!M[t])a++;
    M[t]=1;

    
  }
return a;


}

int main(){
  ull T,n,m;

  cin >> T;
  int cases=1;
  
  while (T--){
    cin>>n>>m;
    M.clear();
    
    string tmp;
    FORN(i,n){
      cin>>tmp;
	FORN(i,tmp.size()) if (tmp[i]=='/')tmp[i]=' ';
      M[tmp]=1;
    }
   
    int a=0;  
 
    FORN(i,m){
      cin>>tmp;	
      a+=c(tmp);
    }

    printf("Case #%d: %d\n",cases++,a);
  }
}












