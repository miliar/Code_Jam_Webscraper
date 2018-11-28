#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define p(a) cout << a << endl;
#define sz(a) (int)(a).size()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define zero(a) memset(a, 0, sizeof(a))
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64

typedef vector<int> vint;

int main()
{
  int n;
  cin >> n;
  vector<char> lis;
  int ncom,nlis;
  forn(_i,n)
  {
   lis.clear();
   map< pair<char,char>, char > combs;
   map< char, char > opo;
   map< char,int > setloco;

   cin >> ncom;
   forn(i,ncom)
   {
    string scom;
    cin >> scom;
    combs[ mp(scom[0],scom[1]) ] = scom[2];
    combs[ mp(scom[1],scom[0]) ] = scom[2];
   }

   cin >> ncom;
   forn(i,ncom)
   {
    string scom;
    cin >> scom;
    opo[ scom[0]] = scom[1];
    opo[ scom[1]] = scom[0];
   }
   
   cin >> nlis;

   forn(i,nlis)
   {
       char X;
       cin >> X;
       if( setloco.find(X) != setloco.end()){
         setloco[X]++;
       }
      else{
        setloco[X] = 1;
      
       }
       lis.pb(X);
       if( sz(lis) > 1 and combs.find( mp(X,lis[ sz(lis)-2 ]) )!= combs.end() ) 
       {
             setloco[lis[last(lis)]]--;
             lis.pop_back(); 
             setloco[lis[last(lis)]]--;
             lis[last(lis)]=combs[mp(lis[last(lis)],X)];
       }
       
       if( sz(lis) > 1 and opo.find( lis[last(lis)] ) != opo.end() ) 
       
       {
            if( setloco[opo[lis[last(lis)]] ] >0 )
            {
              setloco.clear();
              lis.clear();
            }
       }
         
     
   }
   
   cout<<"Case #"<<_i+1<<": [";
   forit(i,lis)
   {
     if(i == lis.end()-1)
      { cout << *i; break;}
     cout << *i << ", ";
   }
   p("]");
    
    
  }
}
