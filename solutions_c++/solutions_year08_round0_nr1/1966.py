#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define SZ size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30

using namespace std;

string s;
int N,Q,S;
vector<string> NAMES,QUERYS;

map<string,int> Nm,Qu;

int T[1001][101];

void act(){
memset(T,0,sizeof (T));
   FORN(i,Q)
      FORN(j,S){
        int total=0;
	int posx=i;
	while (posx!=Q && NAMES[j]!=QUERYS[posx]){total++;posx++;}
         T[i][j]=total;
      }
}

int main(){

    cin>>N;
    getline(cin,s);
   FOR(cas,1,N+1){
      cin>>S;

      
      getline(cin,s);
      NAMES.clear();
      QUERYS.clear();
      FORN(i,S){
	 getline(cin,s);
	 NAMES.PB(s);
      }
      cin>>Q;
      getline(cin,s);
      FORN(i,Q){
	 getline(cin,s);
	 QUERYS.PB(s);
      }
      int mm=INF;
      act();
      int best=INF;
      int actual=0;
      int llevo=0;   
      while (actual!=Q){
      int mxx=0;
          FORN(j,S) mxx=max(mxx,T[actual][j]);
      actual+=mxx;
      if (actual!=Q)llevo++;
      }
      printf("Case #%d: %d\n",cas,llevo);
    }
    return 0;
}
