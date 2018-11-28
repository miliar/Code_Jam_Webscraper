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
vector<string> comb;
vector<string> opp;

bool isin(string s, char x) { REP(i,s.size()) if(s[i] == x) return true; return false; }

bool areop(char x, char y) {
     REP(i,opp.size()) {
         string p = opp[i];
         if( (x == p[0] && y == p[1]) || (x == p[1] && y == p[0])) return true;
     }     
     
     return false;
}

char docomb(char x, char y) {
    REP(i,comb.size()) {
        string c = comb[i];
        if( (x == c[0] && y == c[1]) || (x == c[1] && y == c[0])) return c[2];                                  
    }      
    return '-';
}


int main()
{
   
    freopen("B-large.in","r",stdin);
    freopen("b-large.out","w",stdout);
    
    int cases;
    cin>>cases;
    
    REP(k,cases) {
       int c; cin>>c;
       
       opp.clear(); comb.clear();
       
       REP(i,c) {string tmp; cin>>tmp; comb.PB(tmp); }
       int d; cin>>d;           
       
       REP(i,d) { string tmp; cin>>tmp; opp.PB(tmp); }
       int n; cin>>n;
       string invoke; cin>>invoke;
       
       string result;
       result.PB(invoke[0]);
       FOR(i,1,invoke.size()) {
         //cout<<"res="<<result<<endl;
         if(result.size() == 0) {result.PB(invoke[i]); continue; }
       
          char r = docomb(invoke[i], result[result.size() - 1]);
         if(r != '-') {result.erase(result.end() - 1), result.PB(r);continue; }
         
           bool opp = false;
         REP(j, result.size()) {
                if(areop(invoke[i], result[j])) { opp = true;result.clear(); break; }       
         } 
        // printf("\nOP = %d\n", opp);
         if(opp)continue;         


         result.PB(invoke[i]);
                                                
       }
        printf("Case #%d: [", k + 1);
        if(result.size() > 0)printf("%c",result[0]);
        FOR(i,1,result.size()) printf(", %c",result[i]);
        printf("]\n");         
    }
    
    
    return 0;
}
