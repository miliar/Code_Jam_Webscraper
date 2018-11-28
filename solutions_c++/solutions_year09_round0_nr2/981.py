#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <numeric>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long ll;

PII dir[4]={PII(-1,0),
       PII(0,-1),PII(0,1),
            PII(1,0)};

int h,w;
VVI alt;
vector<string> label;

#define CORRECT(i,j) ((i)>=0&&(i)<h&&(j)>=0&&(j)<w)

PII sink(int i,int j) {
     int minh=alt[i][j];
     REP(d,4)
          if(CORRECT(i+dir[d].X,j+dir[d].Y))
               minh=min(minh,alt[i+dir[d].X][j+dir[d].Y]);
     if(minh>=alt[i][j])return PII(i,j);
     REP(d,4)
          if(CORRECT(i+dir[d].X,j+dir[d].Y)&&
             alt[i+dir[d].X][j+dir[d].Y]==minh)
               return PII(i+dir[d].X,j+dir[d].Y);
     return PII(i,j); //avoid warnings
}

void set_label(int i,int j,char lab) {
     if(!CORRECT(i,j)||label[i][j]!=' ')return;
     label[i][j]=lab;
     REP(d,4)
          if(CORRECT(i+dir[d].X,j+dir[d].Y)&&sink(i+dir[d].X,j+dir[d].Y)==PII(i,j))
               set_label(i+dir[d].X,j+dir[d].Y,lab);
     PII nxt=sink(i,j);
     set_label(nxt.X,nxt.Y,lab);
}

int main() {
     int n,test;
     char cur_label;
     
     for(cin>>n,test=1;test<=n;++test) {
          scanf("%d%d",&h,&w);
          alt=VVI(h,VI(w));
          REP(i,h)REP(j,w)scanf("%d",&alt[i][j]);

          label=vector<string>(h,string(w,' '));
          cur_label='a';
          REP(i,h)REP(j,w)
               if(label[i][j]==' ')set_label(i,j,cur_label++);

          printf("Case #%d:\n",test);
          REP(i,h)REP(j,w)printf("%c%c",label[i][j],j+1<w?' ':'\n');
     }
	
     fprintf(stderr,"running time=%.3lf\n",clock()/(double)CLOCKS_PER_SEC);
     return 0;
} 
