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

#define REP(i,a) for(int i=0;i<(a);i++)
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define ALL(i) i.begin(),i.end()
#define PB push_back

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}





int main()
{

freopen("B-small-attempt8.in","r",stdin);
freopen("output.out","w",stdout);


  string s;
  int n;
  getline(cin,s);
  sscanf(s.c_str(),"%d",&n);
  REP(k,n)
  {
    int t;
    getline(cin,s);
    sscanf(s.c_str(),"%d",&t);
    vs ab, ba;
    int na,nb;
    getline(cin,s);
    stringstream st;
    st<<s;
    st>>na>>nb;
    REP(i,na) 
    {
      getline(cin,s);
      ab.PB(s);          
    }
    REP(i,nb)
    {
      getline(cin,s);
      ba.PB(s);         
    }
     
     vi ab_go,ab_stop, ba_go, ba_stop;
     REP(i,ab.size())
     {
        stringstream st;
        st<<ab[i];
        string x,y;
        st>>x>>y;
        x[2]=' '; y[2]=' ';
        int h,m;
        stringstream stt;
        stt<<x;
        stt>>h>>m;
        ab_go.PB(h*60+m);
        
        stringstream ste;
        ste<<y;
        ste>>h>>m;
        ab_stop.PB(h*60+m);
                       
     }

     REP(i,ba.size())
     {
        stringstream st;
        st<<ba[i];
        string x,y;
        st>>x>>y;
        x[2]=' '; y[2]=' ';
        int h,m;
        stringstream stt;
        stt<<x;
        stt>>h>>m;
        ba_go.PB(h*60+m);
        
        stringstream ste;
        ste<<y;
        ste>>h>>m;
        ba_stop.PB(h*60+m);
                       
     }
     
     

     REP(i,ab.size())
     {
       FOR(j,i+1,ab.size())
       {
         if(ab_go[i]>ab_go[j])
         {
          swap(ab_go[i], ab_go[j]); 
          swap(ab_stop[i], ab_stop[j]);                     
         }                    
       }                
     }
     
     REP(i,ba.size())
     {
       FOR(j,i+1,ba.size())
       {
         if(ba_stop[i]>ba_stop[j])
         {
          swap(ba_go[i], ba_go[j]); 
          swap(ba_stop[i], ba_stop[j]);                     
         }                    
       }                
     }     

     

     
     
     //ab_go = A 
     //ab_stop = B
     //ba_go = B
     //ba_stop = A
     
     int ta=ab.size(),tb=ba.size();
     

     int c = 0;
     
     REP(i,ba_stop.size())
     {
          int p = ba_stop[i]+t;
          REP(j,ab_go.size())
          {
            if(p<=ab_go[j])
            {
              ab_go[j]=-1;
              break;               
            }
                                 
          }                    
     }
     
     REP(i,ab_go.size()) if(ab_go[i]!=-1) c++;
     ta = c;
     c = 0;
     
     
     REP(i,ab_stop.size())
     {
       int p = ab_stop[i]+t;
       REP(j,ba_go.size())
       {
         if(p<=ba_go[j])
         {
           ba_go[j]=-1;
           break;               
         }                   
       }                     
     }
     REP(i,ba_go.size()) if(ba_go[i]!=-1) c++;
     tb = c;
      printf("Case #%d: %d %d\n",k+1,ta,tb);
      
      
      
      
      /*
    printf("ab : \n");
    REP(i,ab.size()) cout<<ab_go[i]<<" "<<ab_stop[i]<<endl;
    printf("ba : \n");
    REP(i,ba.size()) cout<<ba_go[i]<<" "<<ba_stop[i]<<endl;
    */
          
  }
   return 0;
}
