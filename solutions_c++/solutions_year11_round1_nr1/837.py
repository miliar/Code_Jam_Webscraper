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


 int gcd( int a,  int b)
{
   if (b==0) return a;
   return gcd(b,a%b);
}
int lcm(int a, int b)
{
   return b*a/gcd(a,b);
}
int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("largeA.out","w",stdout);
   
   /*
     ifstream in("input.in");
     ofstream out("output.out");
     */
     int t; scanf("%d",&t); 
     
     REP(k,t) {
              
              long long n;
              int pd, pg;
              cin>>n>>pd>>pg;
              if(pd == 0 && pg != 100) { printf("Case #%d: Possible\n", k+1); continue; }
              if(pg == 100 && pd != 100 || (pg == 0 && pd != 0)) { printf("Case #%d: Broken\n", k+1); continue; }
              bool found = false;

              
              int v = lcm(pd, 100);
              int x = v/100;
              if(v%pd == 0) if(v/pd <= n) found = true;  
              //if(lcm(pd, 100)/pd <= n) found = true;
              
              if(found) printf("Case #%d: Possible\n", k+1);
              else printf("Case #%d: Broken\n", k+1);
     }
     return 0;
}
