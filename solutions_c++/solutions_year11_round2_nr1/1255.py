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
/*

  RPI =


WP, OWP, and OOWP are defined for each team as follows:

    * WP (Winning Percentage) is the fraction of your games that you have won.
      In the example schedule, team A has WP = 1, team B has WP = 0, team C has WP = 2/3, and team D has WP = 0.5.
    * OWP (Opponents' Winning Percentage) is the average WP of all your opponents, after first throwing out the games they played against you.
      For example, if you throw out games played against team D, then team B has WP = 0 and team C has WP = 0.5. Therefore team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5, team B has OWP = 0.5, and team C has OWP = 2/3.
    * OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents. OWP is exactly the number computed in the previous step.
      For example, team A has OOWP = 0.5 * (0.5 + 2/3) = 7/12. 
      
      

*/
long double   RPI(long double WP,long double OWP, long double OOWP){
return  0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
}

vector<long double> gWP(vector<string>t){
  int total=t.size();    
  vector<long double>WP(total);
      
      FORN(i,total){
      
     long double play=0,won=0;
      FORN(j,total){
	if (t[i][j]!='.'){
	  play++;
	  if (t[i][j]=='1')
	  won++;
	}
      }
      WP[i]=won/play;
   //   cout<<" " <<WP[i]<<endl;
    }
    return WP;
}

int main(){	 
  freopen("input-large.txt", "r", stdin);
  freopen("output-large.txt", "w", stdout);

  int casos_,total;
  cin>>casos_;

  FORN(casos,casos_){
    cin>>total;
    vector<string> t(total);
    FORN(i,total)cin>>t[i];
    
    vector<long double> OWP(total);
    vector<long double> OOWP(total);
    vector<long double> WP =gWP(t);
    
    
 FORN(i,total){
     vector<string> t1(t);
     long double ini=0;
     vector<int>played;
     FORN(j,total){
       if (t1[i][j]!='.')
	 played.PB(j);
	t1[i][j]='.';
	t1[j][i]='.';
     }
     vector<long double> WP1 = gWP(t1);
    long double k1=0;
     FORN(k,played.size())
	k1+=WP1[played[k]];
     OWP[i]=k1/(long double)played.size();
 }
 
 
 
 FORN(i,total){
     long double ini=0;
     vector<int>played;
     FORN(j,total){
       if (t[i][j]!='.')
	 played.PB(j);
     }
   long  double k1=0;
     FORN(k,played.size())
	k1+=OWP[played[k]];
     OOWP[i]=k1/( long double)played.size();
 }
 
 /*
 
   FORN(i,total) cout<<WP[i]<<endl;  
   cout<<"-----"<<endl;
   FORN(i,total) cout<<OWP[i]<<endl;
   cout<<"-----"<<endl;
   FORN(i,total) cout<<OOWP[i]<<endl;
    
  
*/
    cout<<"Case #"<<(casos+1)<<": "<<endl;
    FORN(i,total)
 
    cout<<setprecision(10)<<RPI(WP[i],OWP[i],OOWP[i])<<endl;
  }

  
}

