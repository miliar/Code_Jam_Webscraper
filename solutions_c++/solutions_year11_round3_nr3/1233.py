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
   
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output2.out","w",stdout);
   
     int t; scanf("%d",&t);
     
     REP(k,t) {
              int n, l, h;
              scanf("%d %d %d",&n,&l,&h);
              VI freq;
              REP(i,n) { int tmp; scanf("%d",&tmp); freq.PB(tmp); }
              printf("Case #%d: ", k + 1);
              bool found = false;
              int res;
              for(int i = l; i <= h; i++) {
                      int j = 0;
                     for(j = 0; j < freq.size(); j++) {
                            int f = freq[j];
                            
                            if(f%i != 0 && i%f!=0) break;
                                     
                     }         
                     if(j == freq.size()) { res = i; found = true; break; }
              }
              if(found) printf("%d\n",res);
              else printf("NO\n");
     }
     
     return 0;
}
