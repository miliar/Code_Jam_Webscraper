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


int main()
{
   
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
   

   int t;
   scanf("%d",&t);
   REP(cc,t) {
         int n;
         scanf("%d",&n);
         vector<int> a, b;
         REP(i,n) {
                  int aa, bb;
                  scanf("%d %d",&aa,&bb);
                  a.PB(aa); b.PB(bb);
         }         
         
         int c = 0;
         REP(i,a.size()) {
             FOR(j,i+1,a.size()) {
                if( (a[i] < a[j] && b[i] < b[j]) || (a[i]>a[j] && b[i] > b[j]));
                else c++;                                     
             }                            
         }
         printf("Case #%d: %d\n",cc+1,c);
         
   }


     return 0;
}
