#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
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
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int i=(a);(int)i<(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

void printvec(vector<int> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}


int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("alarge.out","w",stdout);
   
   
   string s;
   getline(cin,s);
   int t; sscanf(s.c_str(),"%d",&t);
   REP(k,t) {
        getline(cin,s);
        stringstream st; st<<s;
        int r, c;
        st>>r>>c;
        vector<string> g;
        REP(i,r) { getline(cin,s); g.PB(s); }

       bool possible = true;
       REP(i,g.size()) {
           REP(j,g[i].size()) {
              if(g[i][j] == '#') {
                 g[i][j]='/';
                 if(i+1>=g.size() || g[i+1][j]!='#') { possible = false; break; } 
                 else g[i+1][j] = '\\';      
                 if(j+1>=g[0].size() || g[i][j+1]!='#') { possible = false; break; }
                 else g[i][j+1]='\\';
                 if(g[i+1][j+1]=='#')g[i+1][j+1] = '/';
                 else { possible = false; break; }            
              }                                   
           }                            
           if(!possible)break;
       }
     
       printf("Case #%d:\n", k + 1);
       if(!possible)printf("Impossible\n");
       else {
            REP(i,g.size()) cout<<g[i]<<endl;     
       }
        
   }   

   
     
     return 0;
}
