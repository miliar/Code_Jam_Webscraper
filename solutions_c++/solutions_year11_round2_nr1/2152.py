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

void pv(vector<double> a)
{
 cout<<"Vecteur:  ";
 REP(i,a.size()) cout<<a[i]<<"  ";
 cout<<endl;
}

vector<double> calcWP(vector<string> m){
     vector<double> WP;          
     REP(i, m.size()) {
         int c = 0;   
         int p = 0;
         REP(j,m[i].size()) {
             if(m[i][j] == '1') c++; 
             if(m[i][j] !='.') p++;                                
         }          
         
         WP.PB(c * 1.0/p);
     }          
     return WP;     
}

string pCase(int k) {
       return "Case #"+i2a(k)+":";       
}

int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("large.out","w",stdout);
   
   string s; getline(cin,s);
   int t; sscanf(s.c_str(),"%d",&t);
   REP(k,t) {
     getline(cin,s); 
     int n; sscanf(s.c_str(),"%d",&n);
     vector<string> m;
     REP(j, n) {
          getline(cin,s); m.PB(s);         
     }                
     vector<double> WP,WPc, OWP, OOWP;
     
    
     
    WP = calcWP(m);
    
    
     REP(i,m.size()) {
          string v = m[i];
          int r = 0,r1 = 0;
          int p = 0;
          string mm;
          REP(j,m.size()) mm.PB(m[j][i]),m[j][i]='.';             
          
          string save = m[i];
          m[i] = v;
          
          vector<double> w = calcWP(m);
          double sum = 0.0;
          REP(j,m.size()) m[j][i] = mm[j];   
          //pv(w);
          int count = 0;
          REP(j,w.size()) if(m[i][j]!='.') count++,sum += w[j];
        //  cout<<endl;
          OWP.PB(sum*1.0/(count));
         
     }
     
     REP(i,m.size()) {
         double c = 0.0;
         int count = 0;
         REP(j, OWP.size()) if(m[i][j]!='.') c+=OWP[j],count++;
         OOWP.PB(c /count);                               
     }
     
     printf("Case #%d:\n", k + 1);
     //cout<<"owp: "; pv(OWP);
     REP(i,WP.size()){
          cout<<0.25*WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]<<endl;

     }
     
   }
     
     
     return 0;
}
