#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>
using namespace std;
#define inf 1000000000
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef double dbl;

ifstream fin("B.in");
ofstream fout("B.out");

dbl AREA(int x1,int y1,int x2,int y2){
  //cross then divide by two
  return dbl(abs(x1*y2-x2*y1))/2;
}

main(){
  int T; fin>>T; REP(i,T){
    fout<<"Case #"<<i+1<<": ";

    int R,C,A;
    fin>>R>>C>>A;

    dbl area=dbl(A)/2;

    bool good=false;

    REP(x1,R+1)
      REP(y1,C+1)
      REP(x2,R+1)
      REP(y2,C+1)
      if((x1!=0 || y1!=0) && (x1!=x2 || y1!=y2) && (x2!=0 || y2!=0))
	if(AREA(x1,y1,x2,y2)==area){
	  fout<<0<<' '<<0<<' '<<x1<<' '<<y1<<' '<<x2<<' '<<y2<<endl;
	  x1=R+1,y1=C+1,x2=R+1,y2=C+1;
	  good|=1;
	}
  
    if(!good) fout<<"IMPOSSIBLE"<<endl;
       
  }
}

