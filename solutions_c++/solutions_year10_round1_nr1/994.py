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

void pp(vector<string> ss) {cout<<endl;  REP(i,ss.size()) cout<<ss[i]<<endl; cout<<endl; }

int getx(string s, char x) {
   int c = 0;
   int tmpc = 0;
   for(int i = 0; i < s.size(); i++) {
     if(s[i] == x) {
            tmpc++;         
     }             
     else {
          if(tmpc > c) c = tmpc;
          tmpc = 0;     
     } 
   }
    if(tmpc > c) c=tmpc;
    return c;
}

void go(vector<string> br, int k, int& r, int &b) {
                 // --> 
               REP(i,br.size()) {
                   if(getx(br[i],'R') >= k) r = 1;
                   if(getx(br[i],'B') >= k) b = 1;                             
               }
               
               // |
               REP(i,br[0].size()) {
                     string tmp;
                     REP(j,br.size()) tmp.PB(br[j][i]);
                     if(getx(tmp,'R') >= k) r = 1;
                     if(getx(tmp,'B') >= k) b = 1;                                                       
               }
               
               // diag
               REP(j,br[0].size()) {
                   int i = 0;
                   int jj = j;
                   string tmp;
                   while(i < br.size() && jj < br[0].size()) {
                       tmp.PB(br[i][jj]);
                       i++, jj++;            
                   }             
                   //printf("\n");
                  //cout<<"--> "<<tmp<<endl;
                     if(getx(tmp,'R') >= k) r = 1;
                     if(getx(tmp,'B') >= k) b = 1;  
                     
                   i = 0;
                   jj = j;
                   tmp="";
                   while(i < br.size() && jj >=0) {
                       tmp.PB(br[i][jj]);
                       i++, jj--;            
                   }                         
                     if(getx(tmp,'R') >= k) r = 1;
                     if(getx(tmp,'B') >= k) b = 1;                                                         
               }
               
               for(int j = br[0].size() - 1 ; j>=0; j--) {
                   int i = br.size() - 1;
                   int jj = j;
                   string tmp;
                   while(i < br.size() && jj < br[0].size()) {
                       tmp.PB(br[i][jj]);
                       i--, jj++;            
                   }             
                  // cout<<"--> "<<tmp<<endl;
                     if(getx(tmp,'R') >= k) r = 1;
                     if(getx(tmp,'B') >= k) b = 1;  
                     
                   i = br.size() - 1;
                   jj = j;
                   tmp="";
                   while(i >=0 && jj >=0) {
                       tmp.PB(br[i][jj]);
                       i--, jj--;            
                   }                         
                     if(getx(tmp,'R') >= k) r = 1;
                     if(getx(tmp,'B') >= k) b = 1;                                                         
               }                  
}

int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("output-l.out","w",stdout);
   
     int t;
     string s;
     getline(cin,s);
     sscanf(s.c_str(),"%d",&t);
     REP(cc,t) {
               int n,k;
               getline(cin,s);
               stringstream st; st<<s;
               st>>n>>k;
               
               vector<string> br;
               
               REP(i,n) { getline(cin,s); br.PB(s); }
               int b = 0, r = 0;
               

               
               vector<string> save_br;
               REP(i,br.size()) save_br.PB(br[i]);
               
               // <--
               /*
               REP(i,br.size()) {
                 int c = 0;
                 REP(j,br[i].size()) if(br[i][j]=='.') br[i].erase(br[i].begin()+j), c++,j--;
                 REP(v,c) br[i].PB('.');                                
               }
               
               go(br, k, r, b);
               */
               
               // -->
               REP(i,br.size()) br[i] = save_br[i];
               REP(i,br.size()) {
                 int c = 0;
                 string p;
                 REP(j,br[i].size()) if(br[i][j]=='.') br[i].erase(br[i].begin()+j), c++,j--,p.PB('.');
//                 while(br[i][br[i].size() - 1]=='.') br[i].erase(br[i].end() - 1), p.PB('.');
                 br[i] = p + br[i];
               }              
               
               //printf("BR ===\n");
               //REP(i,br.size()) cout<<br[i]<<endl;
               
             //  printf("BR ===\n");
               
               go(br, k, r, b);
               /*
               // up
               REP(i,br.size()) br[i] = save_br[i];
               vector<string> tp_br;
               REP(i,br[0].size()) {
                     string tmp;
                     REP(j,br.size()) tmp.PB(br[j][i]);
                     tp_br.PB(tmp);
               }               
               
               REP(i,tp_br.size()) {
                 int c = 0;
                 REP(j,tp_br[i].size()) if(tp_br[i][j]=='.') tp_br[i].erase(tp_br[i].begin()+j), c++, j--;
                 REP(v,c) tp_br[i].PB('.');                                
               }               
               go(tp_br, k, r, b);
               REP(i,tp_br.size()) {
                 int c = 0;
                 string p;
                 
                 REP(j,tp_br[i].size()) if(tp_br[i][j]=='.') tp_br[i].erase(tp_br[i].begin()+j), c++,j--,p.PB('.');
                 tp_br[i] = p + tp_br[i];
               }                       
               go(tp_br, k, r, b);
               */
               printf("Case #%d: ",cc+1);
               if(r == 1 && b == 1) printf("Both");
               else if(r ==  1 && b == 0) printf("Red");    
               else if(r == 0 && b == 1) printf("Blue");
               else printf("Neither");
               
               printf("\n");
               
               
     }
     return 0;
}
